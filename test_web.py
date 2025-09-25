#!/usr/bin/env python3
"""
Тестовий скрипт для перевірки веб-версії графіка
"""

import requests
import time
import sys

def test_web_server():
    """Тестування веб-сервера"""
    base_url = "http://localhost:5002"
    
    print("=== ТЕСТ ВЕБ-СЕРВЕРА ===")
    print(f"Тестуємо: {base_url}")
    print()
    
    # Тест 1: Перевірка доступності
    print("1. Перевірка доступності сервера...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Сервер доступний")
            print(f"   Відповідь: {response.json()}")
        else:
            print(f"❌ Сервер відповідає з кодом: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("❌ Сервер недоступний")
        print("   Переконайтеся, що graphic.py запущено")
        return False
    except Exception as e:
        print(f"❌ Помилка: {e}")
        return False
    
    print()
    
    # Тест 2: Головна сторінка
    print("2. Перевірка головної сторінки...")
    try:
        response = requests.get(base_url, timeout=5)
        if response.status_code == 200:
            print("✅ Головна сторінка завантажується")
            print(f"   Розмір: {len(response.text)} символів")
        else:
            print(f"❌ Помилка завантаження: {response.status_code}")
    except Exception as e:
        print(f"❌ Помилка: {e}")
    
    print()
    
    # Тест 3: API графіка
    print("3. Перевірка API графіка...")
    try:
        response = requests.get(f"{base_url}/api/chart", timeout=10)
        if response.status_code == 200:
            print("✅ API графіка працює")
            data = response.json()
            if 'data' in data and 'layout' in data:
                print("   ✅ Структура даних коректна")
                print(f"   📊 Кількість trace: {len(data['data'])}")
            else:
                print("   ❌ Некоректна структура даних")
        else:
            print(f"❌ Помилка API: {response.status_code}")
    except Exception as e:
        print(f"❌ Помилка: {e}")
    
    print()
    
    # Тест 4: API інформації про дані
    print("4. Перевірка API даних...")
    try:
        response = requests.get(f"{base_url}/api/data", timeout=5)
        if response.status_code == 200:
            print("✅ API даних працює")
            data = response.json()
            print(f"   📊 Розмір: {data.get('shape', 'N/A')}")
            print(f"   📅 Період: {data.get('first_date', 'N/A')} - {data.get('last_date', 'N/A')}")
            print(f"   🕯️  Свічок: {data.get('total_candles', 'N/A')}")
        else:
            print(f"❌ Помилка API: {response.status_code}")
    except Exception as e:
        print(f"❌ Помилка: {e}")
    
    print()
    print("=== ТЕСТ ЗАВЕРШЕНО ===")
    return True

def main():
    """Головна функція"""
    print("Тестування веб-версії TradingView-подібного графіка")
    print("=" * 60)
    print()
    
    # Перевіряємо наявність requests
    try:
        import requests
    except ImportError:
        print("❌ Бібліотека 'requests' не встановлена")
        print("Встановіть: python -m pip install requests")
        return
    
    # Тестуємо сервер
    success = test_web_server()
    
    if success:
        print()
        print("🎉 Всі тести пройшли успішно!")
        print("🌐 Відкрийте браузер та перейдіть на: http://localhost:5002/")
    else:
        print()
        print("❌ Деякі тести не пройшли")
        print("🔧 Перевірте налаштування та спробуйте знову")

if __name__ == "__main__":
    main()

