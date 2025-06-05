import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the EdgeGuardian API!"

@app.route('/logs')
def get_logs():
    try:
      df = pd.read_csv('packets.csv')
      if df.empty:
            return jsonify({"message": "No packets captured yet."})
      logs = df.to_dict(orient='records')
      return jsonify(logs)
    except FileNotFoundError:
      return jsonify({"error": "packets.csv not found."}), 404
    except Exception as e:
      return jsonify({"error": str(e)}), 500

@app.route('/count')
def count_packets():
    try:
        df = pd.read_csv('packets.csv')
        return jsonify({"count": len(df)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

