import os
import flask
from flask import request, jsonify
from stellar_sentry import ThreatAnalysis, AnomalyDetector, CosmicEvents, AlertSystem

app = flask.Flask(__name__)

@app.route('/api/threat_analysis', methods=['POST'])
def threat_analysis():
    data = request.get_json()
    threat_analysis = ThreatAnalysis(data)
    predictions = threat_analysis.analyze()
    return jsonify({'predictions': predictions.tolist()})

@app.route('/api/anomaly_detection', methods=['POST'])
def anomaly_detection():
    data = request.get_json()
    anomaly_detector = AnomalyDetector(data)
    anomalies = anomaly_detector.detect_anomalies()
    return jsonify({'anomalies': anomalies.tolist()})

@app.route('/api/cosmic_events', methods=['GET'])
def cosmic_events():
    cosmic_events = CosmicEvents('cosmic_events_topic')
    events = cosmic_events.process_events()
    return jsonify({'events': events.to_dict('records')})

@app.route('/api/alert_system', methods=['POST'])
def alert_system():
    message = request.get_json()['message']
    alert_system = AlertSystem({'TWILIO_ACCOUNT_SID': 'your_account_sid', 'TWILIO_AUTH_TOKEN': 'your_auth_token'})
    alert_system.send_alert(message)
    return jsonify({'message': 'Alert sent successfully'})

if __name__ == '__main__':
    app.run(debug=True)
