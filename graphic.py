"""
TradingView-подібний графік свічок - Веб-версія
Автор: AI Assistant
Дата: 2024
"""

import os
import sys
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from chart_display import create_chart_display

app = Flask(__name__)
CORS(app)

# Створюємо глобальний екземпляр графіка
chart = None

@app.route('/')
def index():
    """
    Головна сторінка з графіком
    """
    return render_template('index.html')

@app.route('/api/chart')
def get_chart():
    """
    API endpoint для отримання даних графіка
    """
    global chart
    
    try:
        if chart is None:
            data_path = "data/spot/1d/XRPUSDT.parquet"
            if not os.path.exists(data_path):
                return jsonify({'error': 'Файл даних не знайдено'}), 404
            
            chart = create_chart_display(data_path)
        
        chart_json = chart.get_chart_json()
        return chart_json, 200, {'Content-Type': 'application/json'}
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data')
def get_data_info():
    """
    API endpoint для отримання інформації про дані
    """
    global chart
    
    try:
        if chart is None:
            return jsonify({'error': 'Дані не завантажені'}), 400
        
        data_info = chart.get_data_info()
        return jsonify(data_info)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    """
    Перевірка стану сервера
    """
    return jsonify({'status': 'healthy', 'message': 'TradingView Chart Server is running'})

def main():
    """
    Головна функція для запуску веб-сервера
    """
    global chart
    
    print("=== TradingView-подібний графік свічок - Веб-версія ===")
    
    # Шлях до даних
    data_path = "data/spot/1d/XRPUSDT.parquet"
    
    # Перевіряємо наявність файлу
    if not os.path.exists(data_path):
        print(f"Помилка: Файл {data_path} не знайдено!")
        print("Переконайтеся, що файл знаходиться у правильній папці.")
        return
    
    try:
        # Створюємо графік
        chart = create_chart_display(data_path)
        print("✅ Дані успішно завантажено")
        
        # Отримуємо інформацію про дані
        data_info = chart.get_data_info()
        print(f"📊 Розмір даних: {data_info['shape']}")
        print(f"📅 Період: {data_info['first_date']} - {data_info['last_date']}")
        
        # Запускаємо веб-сервер
        print("\n🚀 Запуск веб-сервера...")
        print("📱 Відкрийте браузер та перейдіть на: http://localhost:5002/")
        print("⏹️  Для зупинки натисніть Ctrl+C")
        
        app.run(host='0.0.0.0', port=5002, debug=False)
        
    except Exception as e:
        print(f"❌ Помилка запуску: {e}")

if __name__ == "__main__":
    main()
