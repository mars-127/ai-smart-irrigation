#AI MODEL TRAINING SCRIPT
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['irrigation']
collection = db['sensor_data']

# Load data
data = pd.DataFrame(list(collection.find()))

# Feature engineering
data['needs_water'] = (data['soil_moisture'] < 30).astype(int)
features = data[['temperature', 'humidity', 'soil_moisture']]
target = data['needs_water']

# Train model
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'irrigation_model.pkl')
print(f"Model accuracy: {model.score(X_test, y_test):.2f}")