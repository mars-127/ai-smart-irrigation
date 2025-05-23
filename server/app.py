#FLASK SERVER FOR DATA LOGGING
from flask import Flask, request, jsonify
from pymongo import MongoClient
import smtplib
from email.mime.text import MIMEText
from datetime imimportport datetime
import os

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['irrigation']
collection = db['sensor_data']

# Email config
EMAIL_FROM = os.getenv('EMAIL_FROM')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_TO = os.getenv('EMAIL_TO')

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    data['timestamp'] = datetime.utcnow()
    
    # Store in MongoDB
    collection.insert_one(data)
    
    # Check for alerts
    if data.get('soil_moisture', 100) < 25:
        send_alert(f"Low soil moisture: {data['soil_moisture']}%")
    
    return jsonify({"status": "success"})

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'Irrigation System Alert'
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_FROM, EMAIL_PASS)
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)