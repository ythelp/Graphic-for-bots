# TradingView-подібний графік свічок - Веб-версія

Цей проект створює професійний веб-графік свічок з функціоналом, подібним до TradingView, використовуючи Python, Flask та Plotly.

## 🌐 Веб-доступ

Після запуску графік доступний за адресою: **http://localhost:5002/**

## ✨ Функції

- 📊 **Candlestick графіки** - відображення японських свічок
- 🔍 **Зум та панорамування** - інтерактивна навігація по графіку
- 📈 **Технічні індикатори** - SMA 20 та SMA 50
- 📱 **Обсяг торгів** - окрема панель для обсягу
- 🎯 **TradingView-подібний UI** - темна тема, професійний вигляд
- 🌙 **Перемикання теми** - темна/світла тема
- 💾 **Експорт графіка** - збереження у HTML формат
- 📊 **Інформаційна панель** - статистика в реальному часі
- 🔄 **Автооновлення** - дані оновлюються автоматично

## 🚀 Встановлення

### 1. Встановлення Python
Переконайтеся, що у вас встановлений Python 3.8 або новіше.

**Windows:**
- Завантажте Python з [python.org](https://www.python.org/downloads/)
- Під час встановлення обов'язково поставте галочку "Add Python to PATH"

**Перевірка встановлення:**
```bash
python --version
```

### 2. Встановлення залежностей
```bash
# Встановлення pip якщо потрібно
python -m ensurepip --upgrade

# Встановлення залежностей
python -m pip install -r requirements.txt
```

### 3. Альтернативне встановлення (якщо виникають проблеми)
```bash
# Встановлення кожної залежності окремо
python -m pip install pandas
python -m pip install plotly
python -m pip install flask
python -m pip install flask-cors
python -m pip install backtesting
python -m pip install pyarrow
```

## 🏗️ Структура проекту

```
Graphic/
├── data/
│   └── spot/
│       └── 1d/
│           └── XRPUSDT.parquet    # Дані свічок
├── graphic.py                      # Веб-сервер Flask
├── requirements.txt                # Залежності
├── README.md                       # Цей файл
├── run_graphic.bat                 # Запуск для Windows
├── run_graphic.ps1                 # Запуск для PowerShell
└── ЗАПУСК.txt                     # Короткі інструкції
```

## 🚀 Запуск

### Основний запуск
```bash
python graphic.py
```

### Альтернативні способи запуску
```bash
# Якщо python не працює
py graphic.py

# Якщо встановлено Python 3
python3 graphic.py

# Через batch файл (Windows)
run_graphic.bat

# Через PowerShell скрипт
run_graphic.ps1
```

## 🌐 Використання

1. **Запустіть сервер** - `python graphic.py`
2. **Відкрийте браузер** та перейдіть на `http://localhost:5002/`
3. **Графік завантажиться** автоматично
4. **Використовуйте мишку** для:
   - Зуму (scroll wheel)
   - Панорамування (drag)
   - Hover для інформації про свічки
5. **Кнопки управління**:
   - 🔄 Оновити - перезавантаження графіка
   - 🌙 Тема - перемикання темної/світлої теми
   - 💾 Експорт - збереження графіка

## 🔧 API Endpoints

- **`/`** - Головна сторінка з графіком
- **`/api/chart`** - Дані графіка у форматі JSON
- **`/api/data`** - Інформація про завантажені дані
- **`/health`** - Перевірка стану сервера

## 📱 Адаптивність

Веб-інтерфейс автоматично адаптується до різних розмірів екрану:
- **Desktop** - повноцінний графік з усіма функціями
- **Tablet** - оптимізований для планшетів
- **Mobile** - компактний вигляд для смартфонів

## 🎨 Налаштування

### Зміна даних
Для роботи з іншими даними змініть шлях у `graphic.py`:
```python
data_path = "path/to/your/data.parquet"
```

### Зміна порту
Для зміни порту відредагуйте `graphic.py`:
```python
app.run(host='0.0.0.0', port=5002, debug=False)
```

### Формат даних
Parquet файл повинен містити колонки:
- `open` - ціна відкриття
- `high` - максимальна ціна
- `low` - мінімальна ціна  
- `close` - ціна закриття
- `volume` - обсяг (опціонально)
- `timestamp`/`time`/`date` - часова мітка

## 🔌 Розширення функціоналу

### Додавання нових індикаторів
Додайте нові індикатори у метод `add_technical_indicators()`:
```python
# RSI
rsi = calculate_rsi(close_prices, period=14)
self.fig.add_trace(
    go.Scatter(x=self.data.index, y=rsi, name='RSI 14'),
    row=1, col=1
)
```

### Додавання нових API endpoints
```python
@app.route('/api/custom')
def custom_endpoint():
    return jsonify({'message': 'Custom endpoint'})
```

### Інтеграція з backtesting.py
```python
from backtesting import Backtest, Strategy

class MyStrategy(Strategy):
    def init(self):
        # Ваша логіка стратегії
        pass

# Запуск бектесту
bt = Backtest(data, MyStrategy)
result = bt.run()
```

## 🛠️ Вирішення проблем

### Помилка "python не розпізнається"
- Перезапустіть командний рядок після встановлення Python
- Перевірте, чи Python додано до PATH
- Спробуйте `py` замість `python`

### Помилка імпорту модулів
```bash
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools wheel
python -m pip install -r requirements.txt
```

### Порт 5002 зайнятий
```bash
# Знайдіть процес, який використовує порт
netstat -ano | findstr :5002

# Зупиніть процес або змініть порт у graphic.py
```

### Проблеми з TA-Lib
```bash
# Windows - завантажте wheel файл
python -m pip install TA_Lib-0.4.25-cp39-cp39-win_amd64.whl

# Або використовуйте альтернативу
python -m pip install ta
```

## 🔒 Безпека

- Сервер запускається тільки на localhost (127.0.0.1)
- CORS налаштований для локальної розробки
- Відсутній доступ до файлової системи через веб-інтерфейс

## 📊 Технічні деталі

- **Backend**: Python + Flask
- **Візуалізація**: Plotly.js
- **Обробка даних**: Pandas
- **Формат даних**: Parquet
- **Бектестинг**: backtesting.py
- **Технічні індикатори**: TA-Lib
- **Порт**: 5002
- **Протокол**: HTTP

## 🌟 Особливості веб-версії

- **Real-time оновлення** - дані оновлюються автоматично
- **Responsive дизайн** - працює на всіх пристроях
- **Кешування** - швидке завантаження при повторних відвідуваннях
- **API-first архітектура** - легко інтегрувати з іншими системами
- **Логування** - детальна інформація про роботу сервера

## 📝 Ліцензія

Цей проект створено для навчальних цілей.

## 🆘 Підтримка

Якщо виникли питання або проблеми:
1. Перевірте консоль сервера для помилок
2. Перегляньте README.md та ЗАПУСК.txt
3. Переконайтеся, що всі залежності встановлено
4. Перевірте, чи порт 5002 не зайнятий іншими процесами
#   G r a p h i c - f o r - b o t s  
 