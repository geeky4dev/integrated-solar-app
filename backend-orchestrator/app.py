# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Proxy endpoints (puedes expandirlos más adelante)
@app.route('/api/ai-designer/<path:path>', methods=["GET", "POST"])
def proxy_ai_designer(path):
    target_url = f'https://solar-ai-designer-backend.onrender.com/{path}'
    response = requests.request(method=request.method, url=target_url, headers=request.headers, json=request.json)
    return (response.content, response.status_code, response.headers.items())

@app.route('/api/radiation-dashboard/<path:path>', methods=["GET", "POST"])
def proxy_radiation_dashboard(path):
    target_url = f'https://solar-dashboard-ar8s.onrender.com/{path}'
    response = requests.request(method=request.method, url=target_url, headers=request.headers, json=request.json)
    return (response.content, response.status_code, response.headers.items())

@app.route('/api/optimizer/<path:path>', methods=["GET", "POST"])
def proxy_optimizer(path):
    target_url = f'https://solar-optimizer-backend.onrender.com/{path}'
    response = requests.request(method=request.method, url=target_url, headers=request.headers, json=request.json)
    return (response.content, response.status_code, response.headers.items())

@app.route('/api/savings/<path:path>', methods=["GET", "POST"])
def proxy_savings(path):
    target_url = f'https://solar-savings-app-backend.onrender.com/{path}'
    response = requests.request(method=request.method, url=target_url, headers=request.headers, json=request.json)
    return (response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(debug=True, port=5000)