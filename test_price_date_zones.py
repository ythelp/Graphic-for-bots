#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Тестовий файл для перевірки виділення зон ціни та дати
"""

import sys
import os
import re

def test_price_date_zones():
    """
    Тестуємо виділення зон ціни та дати іншим кольором та рамкою
    """
    print("=== Тест виділення зон ціни та дати ===")
    
    try:
        # Перевіряємо CSS файл
        css_file = "static/css/style.css"
        if os.path.exists(css_file):
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            # Перевіряємо наявність стилів для зон осей
            zone_styles = [
                '#chart .plotly .xaxis',
                '#chart .plotly .yaxis',
                '#chart .plotly .xaxislayer',
                '#chart .plotly .yaxislayer'
            ]
            
            found_styles = []
            for style in zone_styles:
                if style in css_content:
                    found_styles.append(style)
                    print(f"✅ CSS: Знайдено стиль {style}")
                else:
                    print(f"❌ CSS: Стиль {style} не знайдено!")
                    return False
            
            # Перевіряємо наявність border та background
            if 'border: 3px solid #00d4aa' in css_content:
                print("✅ CSS: Знайдено рамки 3px solid #00d4aa")
            else:
                print("❌ CSS: Рамки 3px solid #00d4aa не знайдено!")
                return False
            
            if 'background: rgba(0, 212, 170, 0.08)' in css_content:
                print("✅ CSS: Знайдено фон rgba(0, 212, 170, 0.08)")
            else:
                print("❌ CSS: Фон rgba(0, 212, 170, 0.08) не знайдено!")
                return False
            
            print(f"\n🎯 Результат виділення зон:")
            print(f"   ✅ Зона дати (X-вісь): Рамка та фон")
            print(f"   ✅ Зона ціни (Y-вісь): Рамка та фон")
            print(f"   ✅ Кольори: #00d4aa (зелений)")
            print(f"   ✅ Фон: rgba(0, 212, 170, 0.08)")
            print(f"   ✅ Рамки: 3px solid #00d4aa")
            
            return True
        else:
            print("❌ CSS файл не знайдено!")
            return False
        
    except Exception as e:
        print(f"❌ Помилка: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_price_date_zones()
    if success:
        print("\n🎉 Тест пройшов успішно! Зони ціни та дати виділені.")
        print("🎨 Зони тепер мають рамки та фон!")
    else:
        print("\n⚠️ Тест не пройшов. Потрібно виправити код.")
