@echo off
title Vahan Mitra - Odisha Ride Booking Backend Server
cd /d "%~dp0"
echo ========================================================
echo       VAHAN MITRA ODISHA - BACKEND & DATABASE SERVER
echo ========================================================
echo.
echo Starting SQLite database and REST API server on port 8080...
echo.
python server.py
pause
