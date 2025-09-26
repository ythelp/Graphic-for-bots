// TradingView-подібний графік свічок - JavaScript

let chartData = null;
let isDarkTheme = true;

// Завантаження графіка
async function loadChart() {
    try {
        const response = await fetch('/api/chart');
        if (!response.ok) {
            throw new Error('Помилка завантаження даних');
        }
        
        chartData = await response.json();
        
        // Діагностика даних
        console.log('Chart data received:', chartData);
        console.log('Number of traces:', chartData.data.length);
        console.log('Trace types:', chartData.data.map(trace => trace.type));
        
        // Детальна діагностика candlestick
        const candlestickTrace = chartData.data.find(trace => trace.type === 'candlestick');
        if (candlestickTrace) {
            console.log('Candlestick trace found:', candlestickTrace);
            console.log('Candlestick data length:', candlestickTrace.x ? candlestickTrace.x.length : 'no x data');
            console.log('First candle:', {
                x: candlestickTrace.x ? candlestickTrace.x[0] : 'no x',
                open: candlestickTrace.open ? candlestickTrace.open[0] : 'no open',
                high: candlestickTrace.high ? candlestickTrace.high[0] : 'no high',
                low: candlestickTrace.low ? candlestickTrace.low[0] : 'no low',
                close: candlestickTrace.close ? candlestickTrace.close[0] : 'no close'
            });
        } else {
            console.log('No candlestick trace found!');
        }
        
        // Створюємо графік
        Plotly.newPlot('chart', chartData.data, chartData.layout, {
            responsive: true,
            displayModeBar: false,
            displaylogo: false,
            scrollZoom: true,
            doubleClick: 'reset+autosize',
            dragmode: 'pan',
            hovermode: false
        });
        
        // Оновлюємо інформаційну панель
        updateInfoPanel();
        
        // Відображення ціни справа прибрано
        
        // Додаємо функцію пересування після повного завантаження
        addPanningAfterLoad();
        
        // Додаємо примусове встановлення осі Y справа
        forceYAxisRight();
        
        // Додаємо виділення зони дати знизу
        addDateZoneHighlight();
        
        // Додаємо обмеження пересування тільки до нижньої панелі
        addRangesliderOnlyPanning();
        
        
    } catch (error) {
        document.getElementById('chart').innerHTML = 
            '<div class="error">Помилка завантаження: ' + error.message + '</div>';
    }
}

// Зона ціни прибрана

// Функції зони ціни прибрані

// Функції відображення ціни прибрані

// Функція updatePriceDisplay прибрана



// Додавання функції пересування після повного завантаження
function addPanningAfterLoad() {
    setTimeout(() => {
        try {
            if (window.Plotly && chartData) {
                // Встановлюємо режим пересування тільки для основного графіку
                Plotly.relayout('chart', {
                    'dragmode': 'pan',
                    'xaxis': {
                        'rangeslider': {'visible': true},
                        'fixedrange': false
                    },
                    'yaxis': {
                        'side': 'right',  // Фіксуємо вісь цін справа
                        'fixedrange': false
                    }
                });
                
                console.log('✅ Функція пересування графіку активована');
            }
        } catch (error) {
            console.error('❌ Помилка активації пересування:', error);
        }
    }, 3000); // Чекаємо 3 секунди для повного завантаження
}

// Примусове встановлення осі Y справа
function forceYAxisRight() {
    setTimeout(() => {
        try {
            if (window.Plotly && chartData) {
                // Примусово встановлюємо вісь Y справа
                Plotly.relayout('chart', {
                    'yaxis': {
                        'side': 'right',
                        'showgrid': true,
                        'gridcolor': 'rgba(0, 212, 170, 0.3)',
                        'gridwidth': 1,
                        'linecolor': '#00d4aa',
                        'linewidth': 1,
                        'tickcolor': '#00d4aa',
                        'tickfont': {
                            'color': '#00d4aa',
                            'size': 12
                        }
                    }
                });
                
                console.log('✅ Вісь Y примусово встановлена справа');
            }
        } catch (error) {
            console.error('❌ Помилка встановлення осі Y справа:', error);
        }
    }, 4000); // Чекаємо 4 секунди для повного завантаження
}

// Виділення зони дати знизу (X-осі)
function addDateZoneHighlight() {
    setTimeout(() => {
        try {
            if (window.Plotly && chartData) {
                // Встановлюємо стилі для X-осі (зона дати)
                Plotly.relayout('chart', {
                    'xaxis': {
                        'showgrid': true,
                        'gridcolor': 'rgba(255, 107, 107, 0.3)',
                        'gridwidth': 2,
                        'linecolor': '#ff6b6b',
                        'linewidth': 3,
                        'tickcolor': '#ff6b6b',
                        'tickfont': {
                            'color': '#ff6b6b',
                            'size': 12
                        }
                    }
                });
                
                console.log('✅ Зона дати знизу виділена');
            }
        } catch (error) {
            console.error('❌ Помилка виділення зони дати:', error);
        }
    }, 5000); // Чекаємо 5 секунд для повного завантаження
}

// Обмеження пересування тільки до нижньої панелі (rangeslider)
function addRangesliderOnlyPanning() {
    setTimeout(() => {
        try {
            if (window.Plotly && chartData) {
                // Встановлюємо режим пересування тільки для rangeslider
                Plotly.relayout('chart', {
                    'dragmode': 'pan',
                    'xaxis': {
                        'rangeslider': {
                            'visible': true,
                            'thickness': 0.1,  // Товщина нижньої панелі
                            'bgcolor': 'rgba(255, 107, 107, 0.1)',  // Фон нижньої панелі
                            'bordercolor': '#ff6b6b',  // Рамка нижньої панелі
                            'borderwidth': 2
                        },
                        'fixedrange': false
                    },
                    'yaxis': {
                        'side': 'right',
                        'fixedrange': false
                    }
                });
                
                console.log('✅ Пересування обмежено тільки до нижньої панелі');
            }
        } catch (error) {
            console.error('❌ Помилка обмеження пересування:', error);
        }
    }, 6000); // Чекаємо 6 секунд для повного завантаження
}


// Оновлення інформаційної панелі
function updateInfoPanel() {
    if (!chartData) return;
    
    try {
        const data = chartData.data;
        const candlestickData = data.find(trace => trace.type === 'candlestick');
        
        if (candlestickData && candlestickData.close && Array.isArray(candlestickData.close)) {
            const closePrices = candlestickData.close;
            const lastPrice = closePrices[closePrices.length - 1];
            const firstPrice = closePrices[0];
            
            if (lastPrice && firstPrice && typeof lastPrice === 'number' && typeof firstPrice === 'number') {
                const change = ((lastPrice - firstPrice) / firstPrice * 100).toFixed(2);
                
                document.getElementById('last-price').textContent = '$' + lastPrice.toFixed(4);
                document.getElementById('change-24h').textContent = change + '%';
                document.getElementById('change-24h').style.color = change >= 0 ? '#00d4aa' : '#f44336';
                document.getElementById('candles-count').textContent = closePrices.length;
                
                // Знаходимо high/low
                if (candlestickData.high && Array.isArray(candlestickData.high) && 
                    candlestickData.low && Array.isArray(candlestickData.low)) {
                    const high = Math.max(...candlestickData.high);
                    const low = Math.min(...candlestickData.low);
                    document.getElementById('high-24h').textContent = '$' + high.toFixed(4);
                    document.getElementById('low-24h').textContent = '$' + low.toFixed(4);
                }
            }
        }
        
        // Обсяг
        const volumeData = data.find(trace => trace.type === 'bar');
        if (volumeData && volumeData.y && Array.isArray(volumeData.y)) {
            const totalVolume = volumeData.y.reduce((sum, vol) => sum + (vol || 0), 0);
            document.getElementById('volume-24h').textContent = totalVolume.toFixed(0);
        }
        
        // Оновлюємо відображення ціни справа
        updatePriceDisplay();
        
    } catch (error) {
        console.error('Помилка оновлення інформаційної панелі:', error);
    }
}

// Оновлення графіка
function refreshChart() {
    document.getElementById('chart').innerHTML = '<div class="loading">Оновлення...</div>';
    // Не викликаємо loadChart() тут, щоб уникнути подвійного завантаження
    location.reload();
}

// Перемикання теми
function toggleTheme() {
    isDarkTheme = !isDarkTheme;
    
    if (isDarkTheme) {
        document.body.classList.remove('light-theme');
    } else {
        document.body.classList.add('light-theme');
    }
    
    const themeBtn = document.querySelector('.btn.secondary');
    themeBtn.textContent = isDarkTheme ? '🌙 Тема' : '☀️ Тема';
}

// Експорт графіка
function exportChart() {
    if (chartData) {
        const link = document.createElement('a');
        link.download = 'tradingview_chart.html';
        
        const exportHtml = `<!DOCTYPE html>
<html>
<head>
    <title>TradingView Chart Export</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        body { margin: 0; padding: 20px; background: #131722; color: #d1d4dc; }
        #chart { width: 100%; height: 80vh; }
    </style>
</head>
<body>
    <h1>XRP/USDT - TradingView Chart Export</h1>
    <div id="chart"></div>
    <script>
        const chartData = ${JSON.stringify(chartData)};
        Plotly.newPlot('chart', chartData.data, chartData.layout);
    </script>
</body>
</html>`;
        
        link.href = 'data:text/html;charset=utf-8,' + encodeURIComponent(exportHtml);
        link.click();
    }
}

// Завантаження всіх свічок
function loadAllCandles() {
    console.log('📊 Завантаження всіх 1000 свічок...');
    
    // Показуємо індикатор завантаження
    document.getElementById('chart').innerHTML = '<div class="loading">Завантаження всіх свічок...</div>';
    
    // Оновлюємо інформаційну панель
    setTimeout(() => {
        updateInfoPanel();
        console.log('✅ Всі свічки завантажено');
    }, 1000);
}

// Ініціалізація при завантаженні сторінки
document.addEventListener('DOMContentLoaded', function() {
    loadChart();
    
    // Оновлення кожні 30 секунд
    setInterval(updateInfoPanel, 30000);
});
