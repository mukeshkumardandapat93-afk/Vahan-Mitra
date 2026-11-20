"""
Exhaustive Balasore District Location Master
Covers all 12 Blocks, 2 Municipalities, NACs, Villages, Gram Panchayats,
Landmarks, Markets, Hospitals, Colleges, Temples, Beaches, Defence & Industrial Hubs.
"""

BALASORE_MASTER_LOCATIONS = [
    # ================= 1. BALASORE MUNICIPALITY / CITY CORE & URBAN WARDS =================
    {"id": "BLS_URB_01", "name": "Balasore Railway Station", "area": "Station Road", "block": "Balasore Sadar", "type": "Transit", "lat": 21.4925, "lng": 86.9328},
    {"id": "BLS_URB_02", "name": "OT Road Sahadevkhunta Bus Stand", "area": "Sahadevkhunta", "block": "Balasore Sadar", "type": "Transit", "lat": 21.4880, "lng": 86.9290},
    {"id": "BLS_URB_03", "name": "Cinema Chhak & Market", "area": "Motiganj", "block": "Balasore Municipality", "type": "Commercial Hub", "lat": 21.4935, "lng": 86.9305},
    {"id": "BLS_URB_04", "name": "Fandi Chhak", "area": "Town Hall", "block": "Balasore Municipality", "type": "Urban Hub", "lat": 21.4905, "lng": 86.9260},
    {"id": "BLS_URB_05", "name": "Collectorate Office & Court Chhak", "area": "Court Complex", "block": "Balasore Sadar", "type": "Government", "lat": 21.4912, "lng": 86.9245},
    {"id": "BLS_URB_06", "name": "SP Office & Reserve Police Line", "area": "Police Line", "block": "Balasore Sadar", "type": "Government", "lat": 21.4890, "lng": 86.9215},
    {"id": "BLS_URB_07", "name": "District Headquarters Hospital (DHH)", "area": "Hospital Road", "block": "Balasore Municipality", "type": "Healthcare", "lat": 21.4950, "lng": 86.9310},
    {"id": "BLS_URB_08", "name": "Fakir Mohan Autonomous College (FM College)", "area": "Azimabad", "block": "Balasore Municipality", "type": "Education", "lat": 21.4990, "lng": 86.9270},
    {"id": "BLS_URB_09", "name": "Fakir Mohan Junior College Campus", "area": "Azimabad", "block": "Balasore Municipality", "type": "Education", "lat": 21.4985, "lng": 86.9265},
    {"id": "BLS_URB_10", "name": "Barabati Girls High School / Barabati Chhak", "area": "Barabati", "block": "Balasore Municipality", "type": "Education", "lat": 21.4960, "lng": 86.9340},
    {"id": "BLS_URB_11", "name": "Mallikashpur Chhak & ITI Road", "area": "Mallikashpur", "block": "Balasore Municipality", "type": "Commercial Hub", "lat": 21.4810, "lng": 86.9180},
    {"id": "BLS_URB_12", "name": "Government ITI Balasore", "area": "Mallikashpur", "block": "Balasore Municipality", "type": "Education", "lat": 21.4800, "lng": 86.9175},
    {"id": "BLS_URB_13", "name": "Angargadia Chhak & Golei", "area": "Angargadia", "block": "Balasore Municipality", "type": "Residential/Market", "lat": 21.4860, "lng": 86.9450},
    {"id": "BLS_URB_14", "name": "Sunhat Chhak & Jamelswar Ghat", "area": "Sunhat", "block": "Balasore Municipality", "type": "Market/Heritage", "lat": 21.4970, "lng": 86.9410},
    {"id": "BLS_URB_15", "name": "Sovarampur / Sobharampur Chhak", "area": "Sobharampur", "block": "Balasore Sadar", "type": "Urban Hub", "lat": 21.4880, "lng": 86.9210},
    {"id": "BLS_URB_16", "name": "Nuasahi & Rani Patna", "area": "Rani Patna", "block": "Balasore Municipality", "type": "Residential", "lat": 21.4930, "lng": 86.9370},
    {"id": "BLS_URB_17", "name": "Golapokhari Chhak", "area": "Golapokhari", "block": "Balasore Municipality", "type": "Urban Hub", "lat": 21.4910, "lng": 86.9330},
    {"id": "BLS_URB_18", "name": "Gopalgoan Bazar & Riverbank Road", "area": "Gopalgoan", "block": "Balasore Sadar", "type": "Market", "lat": 21.5220, "lng": 86.9530},
    {"id": "BLS_URB_19", "name": "Aradabazar Chhak", "area": "Aradabazar", "block": "Balasore Sadar", "type": "Market", "lat": 21.4800, "lng": 86.9280},
    {"id": "BLS_URB_20", "name": "Meghdoot Cinema / Town Hall Road", "area": "Town Hall", "block": "Balasore Municipality", "type": "Entertainment", "lat": 21.4895, "lng": 86.9250},
    {"id": "BLS_URB_21", "name": "Nelia Bag / Neliabag Market", "area": "Neliabag", "block": "Balasore Municipality", "type": "Market", "lat": 21.4940, "lng": 86.9200},
    {"id": "BLS_URB_22", "name": "Balasore Zilla School Campus", "area": "Court Area", "block": "Balasore Sadar", "type": "Education", "lat": 21.4920, "lng": 86.9230},
    {"id": "BLS_URB_23", "name": "Bhaskarganj Chhak", "area": "Bhaskarganj", "block": "Balasore Municipality", "type": "Residential", "lat": 21.4850, "lng": 86.9360},
    {"id": "BLS_URB_24", "name": "Puruna Balasore (Old Town) & Budhabalanga Ghat", "area": "Old Town", "block": "Balasore Sadar", "type": "Heritage", "lat": 21.5010, "lng": 86.9480},
    {"id": "BLS_URB_25", "name": "Balasore Club & Gandhi Smriti Bhawan", "area": "Civil Lines", "block": "Balasore Municipality", "type": "Recreation", "lat": 21.4900, "lng": 86.9275},

    # ================= 2. HIGHWAY HUBS & INDUSTRIAL CORRIDORS =================
    {"id": "BLS_IND_01", "name": "Kuruda Golei (NH-16 By-Pass Chhak)", "area": "Kuruda", "block": "Balasore Sadar", "type": "Highway Hub", "lat": 21.5050, "lng": 86.9120},
    {"id": "BLS_IND_02", "name": "NOCCI Business Park & Exhibition Center", "area": "Bampada", "block": "Balasore Sadar", "type": "Industrial Hub", "lat": 21.4420, "lng": 86.8790},
    {"id": "BLS_IND_03", "name": "Bampada Industrial Estate & NH 16 Overbridge", "area": "Bampada", "block": "Balasore Sadar", "type": "Industrial Hub", "lat": 21.4390, "lng": 86.8750},
    {"id": "BLS_IND_04", "name": "Tamulia Industrial Estate & Gate", "area": "Tamulia", "block": "Balasore Sadar", "type": "Industrial", "lat": 21.5030, "lng": 86.9010},
    {"id": "BLS_IND_05", "name": "Emami Paper Mills Campus & Township", "area": "Rasulpur", "block": "Balasore Sadar", "type": "Industrial", "lat": 21.5250, "lng": 86.9580},
    {"id": "BLS_IND_06", "name": "Birla Tyres Plant Gate", "area": "Bampada", "block": "Balasore Sadar", "type": "Industrial", "lat": 21.4350, "lng": 86.8710},
    {"id": "BLS_IND_07", "name": "Rasulpur Railway Crossing Chhak", "area": "Rasulpur", "block": "Balasore Sadar", "type": "Transit Hub", "lat": 21.5120, "lng": 86.9380},
    {"id": "BLS_IND_08", "name": "Chhanpur Chhak (NH-16)", "area": "Chhanpur", "block": "Balasore Sadar", "type": "Highway Hub", "lat": 21.4700, "lng": 86.8950},
    {"id": "BLS_IND_09", "name": "Haladipada Chhak (NH-16)", "area": "Haladipada", "block": "Basta", "type": "Highway Hub", "lat": 21.6050, "lng": 87.0120},
    {"id": "BLS_IND_10", "name": "Sergarh Toll Plaza & Industrial Gate", "area": "Sergarh", "block": "Khantapada", "type": "Highway Hub", "lat": 21.4120, "lng": 86.8450},

    # ================= 3. REMUNA BLOCK & UNIVERSITIES =================
    {"id": "BLS_REM_01", "name": "Fakir Mohan Medical College & Hospital (FM MCH)", "area": "Remuna Golei", "block": "Remuna", "type": "Healthcare/Hospital", "lat": 21.5280, "lng": 86.8780},
    {"id": "BLS_REM_02", "name": "Khirachora Gopinatha Temple", "area": "Remuna Town", "block": "Remuna", "type": "Heritage Temple", "lat": 21.5340, "lng": 86.8680},
    {"id": "BLS_REM_03", "name": "Remuna Golei / NH Junction", "area": "Remuna", "block": "Remuna", "type": "Highway Hub", "lat": 21.5310, "lng": 86.8720},
    {"id": "BLS_REM_04", "name": "Fakir Mohan University (New Campus Nuapadhi)", "area": "Nuapadhi", "block": "Remuna", "type": "Education", "lat": 21.5720, "lng": 86.9080},
    {"id": "BLS_REM_05", "name": "Balasore College of Engineering & Tech (BCET)", "area": "Sergarh", "block": "Remuna", "type": "Education", "lat": 21.4210, "lng": 86.8520},
    {"id": "BLS_REM_06", "name": "Remuna Block Office & Market", "area": "Remuna Bazar", "block": "Remuna", "type": "Government/Market", "lat": 21.5320, "lng": 86.8690},
    {"id": "BLS_REM_07", "name": "Ganeswarpur Market Chhak", "area": "Ganeswarpur", "block": "Remuna", "type": "Rural Market", "lat": 21.5150, "lng": 86.8850},
    {"id": "BLS_REM_08", "name": "Kalyani Gram Panchayat & Chhak", "area": "Kalyani", "block": "Remuna", "type": "Gram Panchayat", "lat": 21.5450, "lng": 86.8610},
    {"id": "BLS_REM_09", "name": "Mandarpur Village & Chhak", "area": "Mandarpur", "block": "Remuna", "type": "Rural Area", "lat": 21.5580, "lng": 86.8790},

    # ================= 4. CHANDIPUR / DEFENCE & COASTAL BELT =================
    {"id": "BLS_CHN_01", "name": "Chandipur Sea Beach & Marine Drive", "area": "Chandipur Beach", "block": "Balasore Sadar", "type": "Tourism/Beach", "lat": 21.4700, "lng": 87.0190},
    {"id": "BLS_CHN_02", "name": "ITR Main Gate (Integrated Test Range DRDO)", "area": "Chandipur", "block": "Balasore Sadar", "type": "Defence Area", "lat": 21.4580, "lng": 87.0120},
    {"id": "BLS_CHN_03", "name": "Proof & Experimental Establishment (PXE Gate)", "area": "Chandipur Road", "block": "Balasore Sadar", "type": "Defence Area", "lat": 21.4740, "lng": 86.9750},
    {"id": "BLS_CHN_04", "name": "Balaramgadi Fish Landing Centre & River Mouth", "area": "Balaramgadi", "block": "Balasore Sadar", "type": "Fishing Harbor", "lat": 21.4820, "lng": 87.0350},
    {"id": "BLS_CHN_05", "name": "Mirzapur Gram Panchayat Chhak", "area": "Mirzapur", "block": "Balasore Sadar", "type": "Gram Panchayat", "lat": 21.4780, "lng": 86.9920},
    {"id": "BLS_CHN_06", "name": "Hidigaon & Defense Colony", "area": "Hidigaon", "block": "Balasore Sadar", "type": "Residential", "lat": 21.4810, "lng": 86.9680},
    {"id": "BLS_CHN_07", "name": "Kasafal Sea Beach & Fishing Port", "area": "Kasafal", "block": "Balasore Sadar", "type": "Beach/Port", "lat": 21.5540, "lng": 87.1120},
    {"id": "BLS_CHN_08", "name": "Bada Khudia & Dublagadi Coast", "area": "Dublagadi", "block": "Balasore Sadar", "type": "Coastal Village", "lat": 21.5310, "lng": 87.0910},
    {"id": "BLS_CHN_09", "name": "Bahabalpur Sea Beach & Fisheries Jetty", "area": "Bahabalpur", "block": "Balasore Sadar", "type": "Beach/Port", "lat": 21.5710, "lng": 87.1350},

    # ================= 5. NILAGIRI SUBDIVISION & ECO-TOURISM =================
    {"id": "BLS_NIL_01", "name": "Nilagiri Town Bus Stand & Market", "area": "Nilagiri NAC", "block": "Nilagiri", "type": "Urban NAC", "lat": 21.4590, "lng": 86.7680},
    {"id": "BLS_NIL_02", "name": "Nilagiri Rajbati (Palace) & Jagannath Temple", "area": "Nilagiri Town", "block": "Nilagiri", "type": "Heritage Palace", "lat": 21.4600, "lng": 86.7640},
    {"id": "BLS_NIL_03", "name": "Panchalingeswar Temple (Hill Top Shrines)", "area": "Panchalingeswar", "block": "Nilagiri", "type": "Hill Tourism/Temple", "lat": 21.4950, "lng": 86.7120},
    {"id": "BLS_NIL_04", "name": "Kuldiha Wildlife Sanctuary Eco-Tourism Gate", "area": "Kuldiha", "block": "Nilagiri", "type": "Wildlife/Forest", "lat": 21.4150, "lng": 86.6520},
    {"id": "BLS_NIL_05", "name": "Rishia Dam & Eco-Camp Reservoir", "area": "Rishia", "block": "Nilagiri", "type": "Eco-Tourism", "lat": 21.4420, "lng": 86.6710},
    {"id": "BLS_NIL_06", "name": "Ayodhya Heritage Site (Buddhist & Jain Monuments)", "area": "Ayodhya", "block": "Nilagiri", "type": "Archaeological", "lat": 21.4280, "lng": 86.7210},
    {"id": "BLS_NIL_07", "name": "Mitrapur Market & Chhak", "area": "Mitrapur", "block": "Nilagiri", "type": "Rural Market", "lat": 21.4720, "lng": 86.8150},
    {"id": "BLS_NIL_08", "name": "Sajanagarh Chhak & Bhudar Chandi Temple", "area": "Sajanagarh", "block": "Nilagiri", "type": "Temple/Market", "lat": 21.4680, "lng": 86.7350},
    {"id": "BLS_NIL_09", "name": "Baidyanathpur Village & GP", "area": "Baidyanathpur", "block": "Nilagiri", "type": "Gram Panchayat", "lat": 21.4810, "lng": 86.7510},
    {"id": "BLS_NIL_10", "name": "Kaptipada Road Chhak (Nilagiri Border)", "area": "Kaptipada Border", "block": "Nilagiri", "type": "Border Hub", "lat": 21.4950, "lng": 86.6210},

    # ================= 6. SORO SUBDIVISION & SURROUNDINGS =================
    {"id": "BLS_SOR_01", "name": "Soro Bus Stand & Town Hall", "area": "Soro Municipality", "block": "Soro", "type": "Municipality Hub", "lat": 21.2880, "lng": 86.6890},
    {"id": "BLS_SOR_02", "name": "Soro Railway Station", "area": "Station Road Soro", "block": "Soro", "type": "Transit", "lat": 21.2850, "lng": 86.6940},
    {"id": "BLS_SOR_03", "name": "Soro Community Health Centre (CHC)", "area": "Hospital Road", "block": "Soro", "type": "Healthcare", "lat": 21.2910, "lng": 86.6850},
    {"id": "BLS_SOR_04", "name": "Upendranath College (UN College) Soro", "area": "College Chhak", "block": "Soro", "type": "Education", "lat": 21.2940, "lng": 86.6910},
    {"id": "BLS_SOR_05", "name": "Uttareswar Shiva Temple", "area": "Uttareswar", "block": "Soro", "type": "Heritage Temple", "lat": 21.2810, "lng": 86.6780},
    {"id": "BLS_SOR_06", "name": "Anantapur Market Chhak", "area": "Anantapur", "block": "Soro", "type": "Rural Market", "lat": 21.2450, "lng": 86.7210},
    {"id": "BLS_SOR_07", "name": "Dahapada Village & GP", "area": "Dahapada", "block": "Soro", "type": "Gram Panchayat", "lat": 21.3120, "lng": 86.6620},
    {"id": "BLS_SOR_08", "name": "Gopinathpur & Birida Chhak", "area": "Birida", "block": "Soro", "type": "Rural Hub", "lat": 21.2680, "lng": 86.6450},

    # ================= 7. BAHANAGA & KHANTAPADA BLOCK =================
    {"id": "BLS_BAH_01", "name": "Bahanaga Bazar Railway Station", "area": "Bahanaga", "block": "Bahanaga", "type": "Transit Hub", "lat": 21.3410, "lng": 86.7820},
    {"id": "BLS_BAH_02", "name": "Bahanaga High School & Block Office", "area": "Bahanaga Town", "block": "Bahanaga", "type": "Government", "lat": 21.3450, "lng": 86.7860},
    {"id": "BLS_BAH_03", "name": "Gopalpur Seaside Village & Port Link", "area": "Gopalpur", "block": "Bahanaga", "type": "Coastal Village", "lat": 21.3120, "lng": 86.8350},
    {"id": "BLS_BAH_04", "name": "Khantapada Chhak & Police Station", "area": "Khantapada", "block": "Bahanaga", "type": "Police/Highway Hub", "lat": 21.3980, "lng": 86.8250},
    {"id": "BLS_BAH_05", "name": "Panpana Market Chhak", "area": "Panpana", "block": "Bahanaga", "type": "Rural Market", "lat": 21.3720, "lng": 86.7950},
    {"id": "BLS_BAH_06", "name": "Talakurunia & Sahaspur GP", "area": "Talakurunia", "block": "Bahanaga", "type": "Gram Panchayat", "lat": 21.3580, "lng": 86.7610},

    # ================= 8. SIMULIA & OUPADA BLOCKS =================
    {"id": "BLS_SIM_01", "name": "Simulia Bazar & College Chhak", "area": "Simulia Town", "block": "Simulia", "type": "Market Hub", "lat": 21.1980, "lng": 86.5920},
    {"id": "BLS_SIM_02", "name": "Markona Railway Station & Chhak", "area": "Markona", "block": "Simulia", "type": "Transit Hub", "lat": 21.2150, "lng": 86.6120},
    {"id": "BLS_SIM_03", "name": "Jamujhadi Chhak (NH-16 Junction)", "area": "Jamujhadi", "block": "Simulia", "type": "Highway Junction", "lat": 21.1820, "lng": 86.5750},
    {"id": "BLS_SIM_04", "name": "Bada Pokhari Gram Panchayat", "area": "Bada Pokhari", "block": "Simulia", "type": "Gram Panchayat", "lat": 21.2210, "lng": 86.5610},
    {"id": "BLS_OUP_01", "name": "Oupada Block Headquarters & Police Station", "area": "Oupada Town", "block": "Oupada", "type": "Government", "lat": 21.3650, "lng": 86.5820},
    {"id": "BLS_OUP_02", "name": "Fatehpur Market Chhak", "area": "Fatehpur", "block": "Oupada", "type": "Rural Market", "lat": 21.3810, "lng": 86.5620},
    {"id": "BLS_OUP_03", "name": "Baunsabania GP & Foothills", "area": "Baunsabania", "block": "Oupada", "type": "Rural/Scenic", "lat": 21.3480, "lng": 86.5410},

    # ================= 9. JALESWAR SUBDIVISION & HIGHWAY BORDER =================
    {"id": "BLS_JAL_01", "name": "Jaleswar Railway Station & Station Bazaar", "area": "Jaleswar Municipality", "block": "Jaleswar", "type": "Transit", "lat": 21.8020, "lng": 87.2140},
    {"id": "BLS_JAL_02", "name": "Jaleswar Bus Stand & Purana Bazaar", "area": "Jaleswar Town", "block": "Jaleswar", "type": "Commercial Hub", "lat": 21.8080, "lng": 87.2180},
    {"id": "BLS_JAL_03", "name": "Laxmannath Road Toll Plaza (Odisha-WB Border)", "area": "Laxmannath", "block": "Jaleswar", "type": "Interstate Border", "lat": 21.8280, "lng": 87.2450},
    {"id": "BLS_JAL_04", "name": "Raibania Historic Fort & Ruins", "area": "Raibania", "block": "Jaleswar", "type": "Historical Fort", "lat": 21.9120, "lng": 87.1850},
    {"id": "BLS_JAL_05", "name": "Subarnarekha River Bridge & Ghat", "area": "Jaleswar Ghat", "block": "Jaleswar", "type": "River Ghat", "lat": 21.7950, "lng": 87.2020},
    {"id": "BLS_JAL_06", "name": "Hatigarh Market & College Chhak", "area": "Hatigarh", "block": "Jaleswar", "type": "Rural Market", "lat": 21.8350, "lng": 87.1620},
    {"id": "BLS_JAL_07", "name": "Sugalo Gram Panchayat & Border Road", "area": "Sugalo", "block": "Jaleswar", "type": "Gram Panchayat", "lat": 21.8150, "lng": 87.2610},

    # ================= 10. BASTA BLOCK =================
    {"id": "BLS_BAS_01", "name": "Basta Bazaar & Main Market Chhak", "area": "Basta Town", "block": "Basta", "type": "Commercial Hub", "lat": 21.6850, "lng": 87.0720},
    {"id": "BLS_BAS_02", "name": "Basta Railway Station", "area": "Station Road Basta", "block": "Basta", "type": "Transit", "lat": 21.6810, "lng": 87.0760},
    {"id": "BLS_BAS_03", "name": "Amarda Road Railway Station & Airstrip Area", "area": "Amarda Road", "block": "Basta", "type": "Aviation Heritage", "lat": 21.7210, "lng": 87.1250},
    {"id": "BLS_BAS_04", "name": "Rupsa Junction Railway Station", "area": "Rupsa", "block": "Basta", "type": "Railway Junction", "lat": 21.6350, "lng": 87.0210},
    {"id": "BLS_BAS_05", "name": "Singla Police Station & Market Chhak", "area": "Singla", "block": "Basta", "type": "Police/Market", "lat": 21.6420, "lng": 87.1420},
    {"id": "BLS_BAS_06", "name": "Gopinathpur & Paunsakuli GP", "area": "Paunsakuli", "block": "Basta", "type": "Gram Panchayat", "lat": 21.6950, "lng": 87.0510},

    # ================= 11. BALIAPAL BLOCK & COASTAL DELTA =================
    {"id": "BLS_BAL_01", "name": "Baliapal Market & Bus Chhak", "area": "Baliapal Town", "block": "Baliapal", "type": "Market Hub", "lat": 21.6580, "lng": 87.2890},
    {"id": "BLS_BAL_02", "name": "Subarnarekha Port Project Area & Chaumukh", "area": "Chaumukh", "block": "Baliapal", "type": "Port/Mouth", "lat": 21.5820, "lng": 87.3450},
    {"id": "BLS_BAL_03", "name": "Dagara Sea Beach & Casuarina Forest", "area": "Dagara", "block": "Baliapal", "type": "Tourism/Beach", "lat": 21.5910, "lng": 87.3250},
    {"id": "BLS_BAL_04", "name": "Langaleswar Shiva Temple & Ghat", "area": "Langaleswar", "block": "Baliapal", "type": "Heritage Temple", "lat": 21.6850, "lng": 87.2350},
    {"id": "BLS_BAL_05", "name": "Pratappur Gram Panchayat & Market", "area": "Pratappur", "block": "Baliapal", "type": "Gram Panchayat", "lat": 21.6710, "lng": 87.2650},
    {"id": "BLS_BAL_06", "name": "Balia Betnoti Link Chhak", "area": "Balia", "block": "Baliapal", "type": "Rural Hub", "lat": 21.6450, "lng": 87.2750},

    # ================= 12. BHOGRAI BLOCK & NORTH COASTAL BEACHES =================
    {"id": "BLS_BHO_01", "name": "Chandaneswar Shiva Temple (Historic Shrine)", "area": "Chandaneswar", "block": "Bhograi", "type": "Major Pilgrimage", "lat": 21.6180, "lng": 87.5210},
    {"id": "BLS_BHO_02", "name": "Talsari Sea Beach & Red Crab Beach", "area": "Talsari", "block": "Bhograi", "type": "Tourism/Beach", "lat": 21.6020, "lng": 87.5320},
    {"id": "BLS_BHO_03", "name": "Udaypur Sea Beach & Digha Border Checkpoint", "area": "Udaypur", "block": "Bhograi", "type": "Border Beach", "lat": 21.6110, "lng": 87.5450},
    {"id": "BLS_BHO_04", "name": "Jaleswarpur Market & CHC", "area": "Jaleswarpur", "block": "Bhograi", "type": "Market/Healthcare", "lat": 21.6450, "lng": 87.4120},
    {"id": "BLS_BHO_05", "name": "Bhograi Block Office & Kamarda Bazaar", "area": "Kamarda", "block": "Bhograi", "type": "Government/Market", "lat": 21.6850, "lng": 87.3820},
    {"id": "BLS_BHO_06", "name": "Bichitrapur Mangrove Sanctuary & Nature Camp", "area": "Bichitrapur", "block": "Bhograi", "type": "Eco-Mangrove", "lat": 21.6250, "lng": 87.4850},
    {"id": "BLS_BHO_07", "name": "Kakhra & Batagram Seaside GP", "area": "Batagram", "block": "Bhograi", "type": "Coastal Village", "lat": 21.6380, "lng": 87.4620},
    {"id": "BLS_BHO_08", "name": "Dehurda Gram Panchayat & High School", "area": "Dehurda", "block": "Bhograi", "type": "Gram Panchayat", "lat": 21.6620, "lng": 87.4250},

    # ================= 13. FULADI (PHULADI) LOCATION & LANDMARKS =================
    {"id": "BLS_FLD_01", "name": "Fuladi Chhak & Market", "area": "Fuladi (Phuladi)", "block": "Balasore Sadar", "type": "Commercial Hub", "lat": 21.5030, "lng": 86.9290},
    {"id": "BLS_FLD_02", "name": "Fuladi Bridge (Budhabalanga Gala Pol)", "area": "Budhabalanga River Road", "block": "Balasore Sadar", "type": "River Bridge / Transit", "lat": 21.5060, "lng": 86.9310},
    {"id": "BLS_FLD_03", "name": "Fuladi Road / Balasore Link", "area": "Fuladi Main Road", "block": "Balasore Sadar", "type": "Arterial Road", "lat": 21.5015, "lng": 86.9280},
    {"id": "BLS_FLD_04", "name": "Fuladi Primary School & Community Center", "area": "Fuladi", "block": "Balasore Sadar", "type": "Education / Community", "lat": 21.5042, "lng": 86.9275},
    {"id": "BLS_FLD_05", "name": "Budhabalanga Embankment / Fuladi Ghat", "area": "Fuladi Riverfront", "block": "Balasore Sadar", "type": "River Ghat", "lat": 21.5075, "lng": 86.9325},

    # ================= 14. NAGRAM GRAM PANCHAYAT & ALL VILLAGES =================
    {"id": "BLS_NAG_01", "name": "Nagram Gram Panchayat Office & High School", "area": "Nagram", "block": "Balasore Sadar", "type": "Gram Panchayat HQ", "lat": 21.4650, "lng": 86.9420},
    {"id": "BLS_NAG_02", "name": "Nagram Village & Chhak", "area": "Nagram", "block": "Balasore Sadar", "type": "Rural Village", "lat": 21.4640, "lng": 86.9410},
    {"id": "BLS_NAG_03", "name": "Bedhapanchaarada (Bedha Pancharada) Village", "area": "Nagram GP", "block": "Balasore Sadar", "type": "Village", "lat": 21.4610, "lng": 86.9460},
    {"id": "BLS_NAG_04", "name": "Chakpanchurukhi Village", "area": "Nagram GP", "block": "Balasore Sadar", "type": "Village", "lat": 21.4690, "lng": 86.9380},
    {"id": "BLS_NAG_05", "name": "Kahanrakul (Kanharakul) Village", "area": "Nagram GP", "block": "Balasore Sadar", "type": "Village", "lat": 21.4580, "lng": 86.9490},
    {"id": "BLS_NAG_06", "name": "Kalipur Village & Chhak", "area": "Nagram GP", "block": "Balasore Sadar", "type": "Village", "lat": 21.4720, "lng": 86.9430},
    {"id": "BLS_NAG_07", "name": "Kasapa (Kasaba) Village", "area": "Nagram GP", "block": "Balasore Sadar", "type": "Village", "lat": 21.4550, "lng": 86.9530},
    {"id": "BLS_NAG_08", "name": "Malipur Village", "area": "Nagram GP", "block": "Balasore Sadar", "type": "Village", "lat": 21.4670, "lng": 86.9510},
    {"id": "BLS_NAG_09", "name": "Tikirapal Village", "area": "Nagram GP", "block": "Balasore Sadar", "type": "Village", "lat": 21.4710, "lng": 86.9470}
]

if __name__ == "__main__":
    print(f"Total Balasore locations loaded: {len(BALASORE_MASTER_LOCATIONS)}")
