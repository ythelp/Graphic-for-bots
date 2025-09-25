#!/usr/bin/env python3
"""
Простий запуск сервера для тестування
"""

import sys
import os

# Додаємо поточну директорію до шляху
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from graphic import app
    print("=== Запуск сервера ===")
    app.run(host='0.0.0.0', port=5002, debug=False)
except Exception as e:
    print(f"Помилка запуску сервера: {e}")
    import traceback
    traceback.print_exc()




