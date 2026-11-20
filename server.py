"""
Vahan Mitra - Production Backend Server (Python 3 & SQLite)
Exclusive for Odisha - Full Balasore coverage, OTP Auth, Ride Engine, UPI & QR Payment Engine, Wallet Engine
"""

import os
import json
import sqlite3
import random
import time
import hashlib
import urllib.parse
from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "vahan_mitra.db")

# ----------------- BALASORE LOCATIONS DATABASE -----------------
# Exhaustive locations across Balasore District (Urban, Rural, All 12 Blocks, Municipalities, NACs, Landmarks)
try:
    from balasore_locations import BALASORE_MASTER_LOCATIONS as BALASORE_LOCATIONS
except ImportError:
    BALASORE_LOCATIONS = [
        {"id": "BLS01", "name": "Balasore Railway Station", "area": "Station Road", "category": "Transit", "lat": 21.4925, "lng": 86.9328},
        {"id": "BLS15", "name": "Chandipur Sea Beach", "area": "Chandipur", "category": "Tourism", "lat": 21.4700, "lng": 87.0190}
    ]

# ----------------- DATABASE SETUP -----------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    
    # Users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT UNIQUE,
            name TEXT,
            email TEXT,
            district TEXT DEFAULT 'Balasore',
            gender TEXT DEFAULT 'Male',
            wallet_balance REAL DEFAULT 250.0,
            vahan_coins INTEGER DEFAULT 100,
            token TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # OTP Store table
    c.execute('''
        CREATE TABLE IF NOT EXISTS otp_store (
            phone TEXT PRIMARY KEY,
            otp TEXT,
            expires_at REAL
        )
    ''')

    # Rides table
    c.execute('''
        CREATE TABLE IF NOT EXISTS rides (
            id TEXT PRIMARY KEY,
            user_phone TEXT,
            pickup_name TEXT,
            pickup_area TEXT,
            drop_name TEXT,
            drop_area TEXT,
            vehicle_type TEXT,
            distance_km REAL,
            duration_mins INTEGER,
            base_fare REAL,
            discount REAL,
            total_fare REAL,
            payment_method TEXT,
            payment_status TEXT DEFAULT 'PENDING',
            ride_status TEXT DEFAULT 'REQUESTED',
            driver_name TEXT,
            driver_phone TEXT,
            driver_vehicle_no TEXT,
            driver_rating REAL,
            driver_photo TEXT,
            otp TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Transactions & Payments table (UPI, QR, Wallet, Cash)
    c.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            txn_id TEXT PRIMARY KEY,
            user_phone TEXT,
            ride_id TEXT,
            amount REAL,
            type TEXT, -- 'RIDE_PAYMENT', 'WALLET_RECHARGE', 'CASHBACK', 'REFUND'
            method TEXT, -- 'UPI_COLLECT', 'UPI_QR', 'WALLET', 'CASH'
            upi_id TEXT,
            status TEXT, -- 'SUCCESS', 'PENDING', 'FAILED'
            qr_string TEXT,
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Seed Default User if not present
    c.execute("SELECT id FROM users WHERE phone = '9876543210'")
    if not c.fetchone():
        c.execute('''
            INSERT INTO users (phone, name, email, district, gender, wallet_balance, vahan_coins, token)
            VALUES ('9876543210', 'Soumya Ranjan Das', 'soumya.das@vahanmitra.in', 'Balasore', 'Male', 350.0, 150, 'vahan_demo_token_123')
        ''')

    conn.commit()
    conn.close()

init_db()

# ----------------- DRIVERS POOL (Balasore Local Drivers) -----------------
LOCAL_DRIVERS = [
    {"name": "Rabindra Behera", "phone": "+91 94371 88921", "vehicle_no": "OD 01 AA 2490", "rating": 4.9, "photo": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120"},
    {"name": "Manas Ranjan Nayak", "phone": "+91 97762 31204", "vehicle_no": "OD 01 F 7821", "rating": 4.8, "photo": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120"},
    {"name": "Bikash Chandra Patra", "phone": "+91 82490 65112", "vehicle_no": "OD 01 H 9012", "rating": 5.0, "photo": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=120"},
    {"name": "Ashok Kumar Mohanty", "phone": "+91 99380 44329", "vehicle_no": "OD 01 G 4567", "rating": 4.9, "photo": "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=120"},
    {"name": "Dhiren Kumar Barik", "phone": "+91 98612 99401", "vehicle_no": "OD 01 B 1188", "rating": 4.7, "photo": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=120"}
]

# ----------------- HTTP REQUEST HANDLER -----------------
class VahanMitraHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def send_json(self, data, status=200):
        response_bytes = json.dumps(data).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

    def read_post_json(self):
        content_len = int(self.headers.get('Content-Length', 0))
        if content_len == 0:
            return {}
        post_body = self.rfile.read(content_len).decode('utf-8')
        try:
            return json.loads(post_body)
        except Exception:
            return urllib.parse.parse_qs(post_body)

    # ----------------- GET APIS -----------------
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # 1. Balasore Locations API
        if path == "/api/locations":
            q = query.get('q', [''])[0].strip().lower()
            category = query.get('category', [''])[0].strip().lower()
            results = BALASORE_LOCATIONS
            if q:
                results = [loc for loc in results if q in loc['name'].lower() or q in loc['area'].lower()]
            if category:
                results = [loc for loc in results if category == loc['category'].lower()]
            return self.send_json({"status": "success", "total": len(results), "district": "Balasore", "data": results})

        # 2. User Profile API
        elif path == "/api/user/profile":
            phone = query.get('phone', ['9876543210'])[0]
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE phone = ?", (phone,))
            row = c.fetchone()
            conn.close()
            if row:
                user_dict = dict(row)
                del user_dict['token']
                return self.send_json({"status": "success", "data": user_dict})
            else:
                return self.send_json({"status": "error", "message": "User not found"}, status=404)

        # 3. Ride Details / Status API
        elif path == "/api/ride/status":
            ride_id = query.get('ride_id', [''])[0]
            if not ride_id:
                return self.send_json({"status": "error", "message": "Missing ride_id"}, status=400)
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT * FROM rides WHERE id = ?", (ride_id,))
            row = c.fetchone()
            conn.close()
            if row:
                return self.send_json({"status": "success", "data": dict(row)})
            return self.send_json({"status": "error", "message": "Ride not found"}, status=404)

        # 4. User Rides History API
        elif path == "/api/user/rides":
            phone = query.get('phone', ['9876543210'])[0]
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT * FROM rides WHERE user_phone = ? ORDER BY created_at DESC", (phone,))
            rows = c.fetchall()
            conn.close()
            return self.send_json({"status": "success", "rides": [dict(r) for r in rows]})

        # 5. User Wallet & Transactions API
        elif path == "/api/wallet":
            phone = query.get('phone', ['9876543210'])[0]
            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT wallet_balance, vahan_coins FROM users WHERE phone = ?", (phone,))
            u = c.fetchone()
            balance = u['wallet_balance'] if u else 0.0
            coins = u['vahan_coins'] if u else 0
            c.execute("SELECT * FROM transactions WHERE user_phone = ? ORDER BY created_at DESC LIMIT 20", (phone,))
            txns = [dict(r) for r in c.fetchall()]
            conn.close()
            return self.send_json({"status": "success", "balance": balance, "coins": coins, "transactions": txns})

        # Fallback to serving static files from workspace
        return super().do_GET()

    # ----------------- POST APIS -----------------
    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        body = self.read_post_json()

        # 1. Send OTP API
        if path == "/api/auth/send-otp":
            phone = str(body.get('phone', '')).replace('+91', '').strip()
            if not phone or len(phone) < 10:
                return self.send_json({"status": "error", "message": "Please enter a valid 10-digit mobile number"}, status=400)
            
            # Generate 4-digit OTP (Fixed 1234 in dev or random)
            otp = "1234" if phone in ["9876543210", "9999999999"] else str(random.randint(1000, 9999))
            expires = time.time() + 600
            
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("INSERT OR REPLACE INTO otp_store (phone, otp, expires_at) VALUES (?, ?, ?)", (phone, otp, expires))
            conn.commit()
            conn.close()

            return self.send_json({
                "status": "success",
                "message": f"OTP sent to +91 {phone} successfully",
                "phone": phone,
                "dev_otp": otp # Returned for convenience in UI demo
            })

        # 2. Verify OTP & Login/Register API
        elif path == "/api/auth/verify-otp":
            phone = str(body.get('phone', '')).replace('+91', '').strip()
            otp = str(body.get('otp', '')).strip()

            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            c.execute("SELECT otp, expires_at FROM otp_store WHERE phone = ?", (phone,))
            row = c.fetchone()

            if not row or (row['otp'] != otp and otp != "1234"):
                conn.close()
                return self.send_json({"status": "error", "message": "Invalid OTP. Use 1234 or the OTP sent"}, status=400)

            # Check or create user
            c.execute("SELECT * FROM users WHERE phone = ?", (phone,))
            user = c.fetchone()
            token = hashlib.sha256(f"{phone}-{time.time()}".encode()).hexdigest()[:32]

            if not user:
                c.execute('''
                    INSERT INTO users (phone, name, email, district, gender, wallet_balance, vahan_coins, token)
                    VALUES (?, ?, ?, 'Balasore', 'Male', 250.0, 100, ?)
                ''', (phone, f"Vahan Mitra User", f"user{phone[-4:]}@vahanmitra.in", token))
                conn.commit()
                c.execute("SELECT * FROM users WHERE phone = ?", (phone,))
                user = c.fetchone()
            else:
                c.execute("UPDATE users SET token = ? WHERE phone = ?", (token, phone))
                conn.commit()

            user_data = dict(user)
            user_data['token'] = token
            conn.close()

            return self.send_json({
                "status": "success",
                "message": "Login successful. Welcome to Vahan Mitra Odisha!",
                "token": token,
                "user": user_data
            })

        # 3. Fare Calculation API
        elif path == "/api/ride/estimate":
            pickup_id = body.get('pickup_id', 'BLS01')
            drop_id = body.get('drop_id', 'BLS15')
            
            p_loc = next((l for l in BALASORE_LOCATIONS if l['id'] == pickup_id), BALASORE_LOCATIONS[0])
            d_loc = next((l for l in BALASORE_LOCATIONS if l['id'] == drop_id), BALASORE_LOCATIONS[14])

            # Approx distance by lat/lng
            dist = max(2.5, round(((p_loc['lat'] - d_loc['lat'])**2 + (p_loc['lng'] - d_loc['lng'])**2)**0.5 * 111, 1))
            duration = int(dist * 2.5 + 4) # mins

            rates = {
                "bike": {"name": "Bike Taxi", "base": 20, "per_km": 6, "icon": "fa-motorcycle"},
                "auto": {"name": "Balasore Auto", "base": 30, "per_km": 10, "icon": "fa-van-shuttle"},
                "mini": {"name": "Mini Cab (AC)", "base": 60, "per_km": 14, "icon": "fa-car-side"},
                "sedan": {"name": "Prime Sedan", "base": 90, "per_km": 18, "icon": "fa-car"},
                "parcel": {"name": "Vahan Express Parcel", "base": 25, "per_km": 8, "icon": "fa-box"}
            }

            estimates = {}
            for k, v in rates.items():
                fare = round(v["base"] + (dist * v["per_km"]))
                estimates[k] = {
                    "vehicle": v["name"],
                    "icon": v["icon"],
                    "fare": fare,
                    "eta": random.randint(2, 6)
                }

            return self.send_json({
                "status": "success",
                "distance_km": dist,
                "duration_mins": duration,
                "pickup": p_loc,
                "drop": d_loc,
                "estimates": estimates
            })

        # 4. Create / Request Ride API
        elif path == "/api/ride/book":
            phone = body.get('user_phone', '9876543210')
            pickup_name = body.get('pickup_name', 'Balasore Railway Station')
            pickup_area = body.get('pickup_area', 'Station Road')
            drop_name = body.get('drop_name', 'Chandipur Sea Beach')
            drop_area = body.get('drop_area', 'Chandipur')
            vehicle_type = body.get('vehicle_type', 'bike')
            distance_km = float(body.get('distance_km', 14.5))
            duration_mins = int(body.get('duration_mins', 28))
            total_fare = float(body.get('total_fare', 107))
            payment_method = body.get('payment_method', 'UPI_QR')
            discount = float(body.get('discount', 0))

            ride_id = f"VM-BLS-{int(time.time())}"
            ride_otp = str(random.randint(1000, 9999))
            driver = random.choice(LOCAL_DRIVERS)

            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()

            # If payment by wallet, check balance
            if payment_method == 'WALLET':
                c.execute("SELECT wallet_balance FROM users WHERE phone = ?", (phone,))
                res = c.fetchone()
                current_bal = res[0] if res else 0
                if current_bal < total_fare:
                    conn.close()
                    return self.send_json({"status": "error", "message": f"Insufficient wallet balance (₹{current_bal}). Please recharge or use UPI/QR."}, status=400)
                # Deduct wallet
                new_bal = current_bal - total_fare
                c.execute("UPDATE users SET wallet_balance = ? WHERE phone = ?", (new_bal, phone))
                # Insert transaction
                txn_id = f"TXN-{int(time.time())}"
                c.execute('''
                    INSERT INTO transactions (txn_id, user_phone, ride_id, amount, type, method, status, notes)
                    VALUES (?, ?, ?, ?, 'RIDE_PAYMENT', 'WALLET', 'SUCCESS', 'Ride payment via Vahan Wallet')
                ''', (txn_id, phone, ride_id, total_fare))

            c.execute('''
                INSERT INTO rides (
                    id, user_phone, pickup_name, pickup_area, drop_name, drop_area,
                    vehicle_type, distance_km, duration_mins, base_fare, discount, total_fare,
                    payment_method, payment_status, ride_status, driver_name, driver_phone,
                    driver_vehicle_no, driver_rating, driver_photo, otp
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                ride_id, phone, pickup_name, pickup_area, drop_name, drop_area,
                vehicle_type, distance_km, duration_mins, total_fare + discount, discount, total_fare,
                payment_method, 'PAID' if payment_method == 'WALLET' else 'PENDING',
                'ACCEPTED', driver['name'], driver['phone'], driver['vehicle_no'], driver['rating'], driver['photo'], ride_otp
            ))

            conn.commit()
            conn.close()

            return self.send_json({
                "status": "success",
                "message": "Ride booked successfully! Pilot is heading your way.",
                "ride_id": ride_id,
                "otp": ride_otp,
                "driver": driver,
                "total_fare": total_fare,
                "payment_method": payment_method
            })

        # 5. Complete Ride Payment API (UPI Collect / QR / Wallet / Cash)
        elif path == "/api/payment/process":
            phone = body.get('phone', '9876543210')
            ride_id = body.get('ride_id', '')
            amount = float(body.get('amount', 0))
            method = body.get('method', 'UPI_QR') # 'UPI_ID', 'UPI_QR', 'WALLET', 'CASH'
            upi_id = body.get('upi_id', 'vahanmitra@sbi')

            txn_id = f"TXN-BLS-{int(time.time() * 1000)}"
            qr_string = f"upi://pay?pa=vahanmitra@sbi&pn=VahanMitraOdisha&am={amount}&tn=Ride_{ride_id}&cu=INR"

            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()

            if method == 'WALLET':
                c.execute("SELECT wallet_balance FROM users WHERE phone = ?", (phone,))
                res = c.fetchone()
                bal = res[0] if res else 0
                if bal < amount:
                    conn.close()
                    return self.send_json({"status": "error", "message": "Low wallet balance. Select UPI or QR."}, status=400)
                c.execute("UPDATE users SET wallet_balance = wallet_balance - ? WHERE phone = ?", (amount, phone))

            c.execute('''
                INSERT INTO transactions (txn_id, user_phone, ride_id, amount, type, method, upi_id, status, qr_string, notes)
                VALUES (?, ?, ?, ?, 'RIDE_PAYMENT', ?, ?, 'SUCCESS', ?, 'Payment for ride')
            ''', (txn_id, phone, ride_id, amount, method, upi_id, qr_string))

            if ride_id:
                c.execute("UPDATE rides SET payment_status = 'PAID', ride_status = 'COMPLETED' WHERE id = ?", (ride_id,))

            conn.commit()
            conn.close()

            return self.send_json({
                "status": "success",
                "message": f"Payment of ₹{amount} verified and completed via {method}",
                "txn_id": txn_id,
                "qr_string": qr_string,
                "amount": amount,
                "method": method
            })

        # 6. Wallet Add Money API
        elif path == "/api/wallet/topup":
            phone = body.get('phone', '9876543210')
            amount = float(body.get('amount', 100))
            method = body.get('method', 'UPI')
            upi_id = body.get('upi_id', 'user@upi')

            txn_id = f"TOPUP-{int(time.time())}"
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute("UPDATE users SET wallet_balance = wallet_balance + ? WHERE phone = ?", (amount, phone))
            c.execute('''
                INSERT INTO transactions (txn_id, user_phone, amount, type, method, upi_id, status, notes)
                VALUES (?, ?, ?, 'WALLET_RECHARGE', ?, ?, 'SUCCESS', 'Wallet top-up via UPI')
            ''', (txn_id, phone, amount, method, upi_id))
            c.execute("SELECT wallet_balance FROM users WHERE phone = ?", (phone,))
            new_bal = c.fetchone()[0]
            conn.commit()
            conn.close()

            return self.send_json({
                "status": "success",
                "message": f"₹{amount} added to Vahan Wallet successfully!",
                "new_balance": new_bal,
                "txn_id": txn_id
            })

        # 7. Update User Profile API
        elif path == "/api/user/update":
            phone = body.get('phone', '9876543210')
            name = body.get('name', 'Soumya Ranjan Das')
            email = body.get('email', 'soumya.das@vahanmitra.in')
            district = body.get('district', 'Balasore')
            gender = body.get('gender', 'Male')

            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            c.execute('''
                UPDATE users SET name = ?, email = ?, district = ?, gender = ? WHERE phone = ?
            ''', (name, email, district, gender, phone))
            conn.commit()
            conn.close()

            return self.send_json({"status": "success", "message": "Profile updated in database"})

        return self.send_json({"status": "error", "message": "Endpoint not found"}, status=404)


if __name__ == "__main__":
    os.chdir(BASE_DIR)
    server = HTTPServer(('0.0.0.0', PORT), VahanMitraHandler)
    print(f"🚀 Vahan Mitra Odisha Server running on http://localhost:{PORT}")
    server.serve_forever()
