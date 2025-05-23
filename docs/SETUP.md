HARDWARE SETUP GUIDE
# Hardware Setup Guide

## Components
1. ESP32 Development Board
2. DHT11 Temperature/Humidity Sensor
3. Soil Moisture Sensor
4. Relay Module
5. Solenoid Valve
6. Power Supply

## Wiring Diagram
ESP32 Pinout:

GPIO4 → DHT11 Data

GPIO34 → Soil Moisture

GPIO23 → Relay Control

3.3V → Sensors VCC

GND → Sensors GND


## Installation
1. Flash MicroPython to ESP32
2. Upload `main.py`
3. Power the system

## Bash installation instructions
- Clone the repository
git clone 
cd smart-irrigation-system

- Set up Python virtual environment (for server)
python -m venv venv
source venv/bin/activate  # Linux/Mac
 or .\venv\Scripts\activate  # Windows

- Install server dependencies
cd server
pip install -r requirements.txt

- Install MongoDB (for data storage)
Ubuntu:
sudo apt-get install mongodb
Mac:
brew install mongodb-community

- Set environment variables for email
echo "EMAIL_FROM=your@gmail.com" >> .env
echo "EMAIL_PASS=yourpassword" >> .env
echo "EMAIL_TO=recipient@example.com" >> .env

- Run the server
python app.py

For ESP32 setup:
1. Install esptool: pip install esptool
2. Flash MicroPython firmware
.py`
3. Power the system
- Bash installation instructions
 pp.py

- For ESP32 setup:
 1. Install esptool: pip install esptool
 2. Flash MicroPython firmware
