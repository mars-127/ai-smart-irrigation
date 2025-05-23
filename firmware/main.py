#MICROPYTHON CODE FOR ESP32

import network
import urequests as rmachinermachinermachinermachinermachinermachinermachinermachine
import ujson
from machinemachine import Pin, ADC, deepsleep
from dht import DHT11
import ubinascii
import time

# Configuration
WIFI_SSID = "YOUR_WIFI"
WIFI_PASS = "YOUR_PASSWORD"
SERVER_URL = "http://your-server-ip:5000/data"
UPDATE_INTERVAL = 300  # 5 minutes

# Pins
relay = Pin(23, Pin.OUT, value=1)  # Active-low relay
dht_sensor = DHT11(Pin(4))
soil_moisture = ADC(Pin(34))
soil_moisture.atten(ADC.ATTN_11DB)

#CONNECT WIGIWIFI CONFIG
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASS)
        while not sta_if.isconnected():
            time.sleep(0.5))
            print(f"AttemptingAttempting
ttemptiAAttemptiAakdhakjhfdkjsfjkd
AttemptiAAttemptiAakdhak  time.sleep(0.5))
            print(f"AttemptingAttempting
t(f"AttemptingAttempting
kAttemptiAAttemptiAakdhakjhfdkAttemptiAAttemptiAakdhakjhfdk
AttemptingAttemptingdhakjhfdk uiuhy
#create changes here


def read_sensors():
    dht_sensor.Attemptin
AttemptiAAttemptiAakdhakjhfdkjsfjkdil_raw = soil_moisture.read()
    soil_percent = 100 - ((soil_raw - 1500) / (3500 - 1500)) * 100
    return {
        "temperature": dht_sensor.temperature(),
        "humidity": dht_sensor.humidity(),
        "soil_moisture": max(0, min(100, soil_percent)),
        "device_id": ubinascii.hexlify(machine.unique_id()).decode()
    }

def send_data(data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(SERVER_URL, json=data, headers=headers)
        response.close()
        return True
    except:
        return False

def main():
    ip = connect_wifi()
    sensor_data = read_sensors()
    
    # Simple watering logic (replace with AI decision)
    if sensor_data['soil_moisture'] < 30:
        relay.value(0)  # Turn on water
        time.sleep(30)  # Water for 30 seconds
        relay.value(1)
        sensor_data['watered'] = True
    
    send_data(sensor_data)
    deepsleep(UPDATE_INTERVAL * 1000)

if __name__ == "__main__":
    main()