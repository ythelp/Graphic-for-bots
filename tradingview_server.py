#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Сервер для TradingView-подібного графіка
Використовує офіційний TradingView Widget API
"""

import http.server
import socketserver
import webbrowser
import os
from pathlib import Path

def main():
    # Налаштування сервера
    PORT = 5006
    DIRECTORY = Path(__file__).parent
    
    # Змінити поточну директорію
    os.chdir(DIRECTORY)
    
    # Створити HTTP сервер
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🚀 TradingView сервер запущено на порту {PORT}")
        print(f"📁 Директорія: {DIRECTORY}")
        print(f"🌐 URL: http://localhost:{PORT}")
        print(f"📊 Графік: http://localhost:{PORT}/tradingview_chart.html")
        print("\n" + "="*50)
        print("📋 Інструкції:")
        print("1. Відкрийте браузер")
        print(f"2. Перейдіть на: http://localhost:{PORT}/tradingview_chart.html")
        print("3. Перевірте роботу TradingView графіка")
        print("4. Спробуйте змінити торгові пари")
        print("5. Для зупинки сервера натисніть Ctrl+C")
        print("="*50 + "\n")
        
        # Автоматично відкрити графік
        try:
            webbrowser.open(f'http://localhost:{PORT}/tradingview_chart.html')
            print("✅ Графік відкрито в браузері")
        except:
            print("⚠️ Не вдалося автоматично відкрити браузер")
            print(f"   Відкрийте вручну: http://localhost:{PORT}/tradingview_chart.html")
        
        print("\n⏳ Сервер працює... (Ctrl+C для зупинки)")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Сервер зупинено")
            httpd.shutdown()

if __name__ == "__main__":
    main()
