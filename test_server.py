#!/usr/bin/env python3
"""
Тестовий сервер на порту 5003
"""

import sys
import os

# Додаємо поточну директорію до шляху
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from graphic import app
    print("=== Запуск тестового сервера на порту 5003 ===")
    app.run(host='127.0.0.1', port=5003, debug=False)
except Exception as e:
    print(f"Помилка запуску сервера: {e}")
    import traceback
    traceback.print_exc()





