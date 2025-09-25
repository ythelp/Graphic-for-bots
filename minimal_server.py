#!/usr/bin/env python3
"""
Мінімальний тестовий сервер
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Test server is running!"

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("=== Запуск мінімального сервера ===")
    app.run(host='127.0.0.1', port=5004, debug=False)




