"""
Модуль для відображення графіка свічок
"""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
from datetime import datetime
import os
import sys
import json

class ChartDisplay:
    """
    Клас для створення та відображення графіка свічок
    """
    
    def __init__(self, data_path):
        """
        Ініціалізація графіка
        
        Args:
            data_path (str): Шлях до parquet файлу з даними
        """
        self.data_path = data_path
        self.data = None
        self.fig = None
        self.load_data()
    
    def load_data(self):
        """
        Завантаження даних з parquet файлу
        """
        try:
            print(f"Завантаження даних з: {self.data_path}")
            self.data = pd.read_parquet(self.data_path)
            
            # Перевіряємо структуру даних
            print(f"Розмір даних: {self.data.shape}")
            print(f"Колонки: {self.data.columns.tolist()}")
            
            # Перетворюємо індекс на datetime
            if 'open_time' in self.data.columns:
                self.data['open_time'] = pd.to_datetime(self.data['open_time'])
                self.data.set_index('open_time', inplace=True)
            elif 'close_time' in self.data.columns:
                self.data['close_time'] = pd.to_datetime(self.data['close_time'])
                self.data.set_index('close_time', inplace=True)
            
            # Сортуємо за часом
            self.data.sort_index(inplace=True)
            
            print(f"✅ Дані успішно завантажено")
            print(f"📊 Розмір даних: {self.data.shape}")
            print(f"📅 Період: {self.data.index[0]} - {self.data.index[-1]}")
            print(f"💰 Діапазон цін: {self.data['close_price'].min():.4f} - {self.data['close_price'].max():.4f}")
            print(f"📈 Перша свічка: O={self.data['open_price'].iloc[0]:.4f}, H={self.data['high_price'].iloc[0]:.4f}, L={self.data['low_price'].iloc[0]:.4f}, C={self.data['close_price'].iloc[0]:.4f}")
            
        except Exception as e:
            print(f"Помилка завантаження даних: {e}")
            sys.exit(1)
    
    def create_candlestick_chart(self):
        """
        Створення базового candlestick графіка
        """
        if self.data is None:
            print("Дані не завантажені!")
            return
        
        # Створюємо підграфіки
        self.fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.03,
            subplot_titles=('Ціна XRP/USDT', 'Обсяг'),
            row_width=[0.7, 0.3]
        )
        
        # Перетворюємо дані в списки для правильної серіалізації
        x_data = self.data.index.tolist()
        open_data = self.data['open_price'].tolist()
        high_data = self.data['high_price'].tolist()
        low_data = self.data['low_price'].tolist()
        close_data = self.data['close_price'].tolist()
        
        # Додаємо candlestick графік з правильними назвами колонок
        candlestick_trace = go.Candlestick(
            x=x_data,
            open=open_data,
            high=high_data,
            low=low_data,
            close=close_data,
            name='XRP/USDT',
            increasing_line_color='#26A69A',
            decreasing_line_color='#EF5350',
            increasing_fillcolor='#26A69A',
            decreasing_fillcolor='#EF5350',
            line=dict(width=1),
            showlegend=True,
            visible=True
        )
        
        self.fig.add_trace(candlestick_trace, row=1, col=1)
        
        # Діагностика candlestick даних
        print(f"📊 Candlestick дані:")
        print(f"   - Кількість свічок: {len(self.data)}")
        print(f"   - Перша свічка: O={self.data['open_price'].iloc[0]:.4f}, H={self.data['high_price'].iloc[0]:.4f}, L={self.data['low_price'].iloc[0]:.4f}, C={self.data['close_price'].iloc[0]:.4f}")
        print(f"   - Остання свічка: O={self.data['open_price'].iloc[-1]:.4f}, H={self.data['high_price'].iloc[-1]:.4f}, L={self.data['low_price'].iloc[-1]:.4f}, C={self.data['close_price'].iloc[-1]:.4f}")
        
        # Додаємо обсяг
        if 'volume' in self.data.columns:
            volume_data = self.data['volume'].tolist()
            self.fig.add_trace(
                go.Bar(
                    x=x_data,
                    y=volume_data,
                    name='Обсяг',
                    marker_color='#42A5F5',
                    opacity=0.7,
                    showlegend=True
                ),
                row=2, col=1
            )
        
        # Налаштування осей
        self.fig.update_xaxes(
            title_text="Час",
            rangeslider_visible=False,
            row=2, col=1
        )
        
        self.fig.update_yaxes(
            title_text="Ціна (USDT)",
            row=1, col=1
        )
        
        self.fig.update_yaxes(
            title_text="Обсяг",
            row=2, col=1
        )
        
        # Налаштування layout
        self.fig.update_layout(
            title={
                'text': 'XRP/USDT - TradingView-подібний графік',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            xaxis_rangeslider_visible=False,
            height=800,
            showlegend=True,
            template='plotly_dark',
            hovermode='x unified'
        )
    
    def add_technical_indicators(self):
        """
        Додавання технічних індикаторів
        """
        if self.data is None or self.fig is None:
            return
        
        try:
            # Простий ковзний середній (SMA) на основі close_price
            close_prices = self.data['close_price']
            
            # SMA 20
            sma_20 = close_prices.rolling(window=20).mean()
            sma_20_data = sma_20.tolist()
            self.fig.add_trace(
                go.Scatter(
                    x=x_data,
                    y=sma_20_data,
                    name='SMA 20',
                    line=dict(color='#FF9800', width=2),
                    opacity=0.8
                ),
                row=1, col=1
            )
            
            # SMA 50
            sma_50 = close_prices.rolling(window=50).mean()
            sma_50_data = sma_50.tolist()
            self.fig.add_trace(
                go.Scatter(
                    x=x_data,
                    y=sma_50_data,
                    name='SMA 50',
                    line=dict(color='#9C27B0', width=2),
                    opacity=0.8
                ),
                row=1, col=1
            )
            
        except Exception as e:
            print(f"Помилка додавання індикаторів: {e}")
    
    def add_tradingview_features(self):
        """
        Додавання TradingView-подібних функцій
        """
        if self.fig is None:
            return
        
        # Налаштування hover через layout (для candlestick)
        self.fig.update_layout(
            hovermode='x unified',
            hoverlabel=dict(
                bgcolor="rgba(0,0,0,0.8)",
                font_size=12,
                font_family="Arial"
            )
        )
        
        # Додавання кнопок для навігації
        self.fig.update_layout(
            updatemenus=[
                dict(
                    type="buttons",
                    direction="left",
                    pad={"r": 10, "t": 87},
                    showactive=False,
                    x=0.1,
                    xanchor="right",
                    y=0,
                    yanchor="top",
                    buttons=list([
                        dict(
                            args=[{"xaxis.range": [self.data.index[0], self.data.index[-1]]}],
                            label="Весь період",
                            method="relayout"
                        ),
                        dict(
                            args=[{"xaxis.range": [self.data.index[-100], self.data.index[-1]]}],
                            label="Останні 100 свічок",
                            method="relayout"
                        ),
                        dict(
                            args=[{"xaxis.range": [self.data.index[-50], self.data.index[-1]]}],
                            label="Останні 50 свічок",
                            method="relayout"
                        )
                    ])
                )
            ]
        )
    
    def get_chart_json(self):
        """
        Отримання графіка у форматі JSON для веб-версії
        """
        if self.fig is None:
            self.create_candlestick_chart()
            self.add_technical_indicators()
            self.add_tradingview_features()
        
        # Використовуємо to_json() з правильними параметрами
        return self.fig.to_json(validate=False, pretty=False)
    
    def get_data_info(self):
        """
        Отримання інформації про дані
        """
        if self.data is None:
            return None
        
        return {
            'shape': self.data.shape,
            'columns': self.data.columns.tolist(),
            'first_date': str(self.data.index[0]),
            'last_date': str(self.data.index[-1]),
            'total_candles': len(self.data)
        }

def create_chart_display(data_path):
    """
    Функція для створення екземпляра ChartDisplay
    
    Args:
        data_path (str): Шлях до parquet файлу з даними
        
    Returns:
        ChartDisplay: Екземпляр класу ChartDisplay
    """
    return ChartDisplay(data_path)

if __name__ == "__main__":
    # Тестування модуля
    data_path = "data/spot/1d/XRPUSDT.parquet"
    chart = create_chart_display(data_path)
    
    # Тестуємо отримання JSON
    chart_json = chart.get_chart_json()
    print(f"✅ JSON отримано, розмір: {len(chart_json)} символів")
    
    # Тестуємо отримання інформації про дані
    data_info = chart.get_data_info()
    print(f"✅ Інформація про дані: {data_info}")
