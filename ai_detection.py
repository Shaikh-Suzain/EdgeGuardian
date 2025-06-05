import pandas as pd
from sklearn.ensemble import IsolationForest

# Step 1: Load packets
df = pd.read_csv('packets.csv')

# Step 2: Preprocess
df['proto'] = df['proto'].astype('category').cat.codes
features = df[['length', 'proto']]

# Step 3: Train & Predict
model = IsolationForest(contamination=0.05, random_state=42)
model.fit(features)
df['anomaly'] = model.predict(features)

# Step 4: Save
df.to_csv('packets_with_anomalies.csv', index=False)
print("Anomaly detection done! Check 'packets_with_anomalies.csv'.")
