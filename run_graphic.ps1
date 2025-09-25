# TradingView-подібний графік свічок - Веб-версія (PowerShell скрипт)
Write-Host "=== TradingView-подібний графік свічок - Веб-версія ===" -ForegroundColor Green
Write-Host ""

# Перевірка наявності Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python знайдено: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Помилка: Python не знайдено!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Спробуйте:" -ForegroundColor Yellow
    Write-Host "1. Встановити Python з python.org" -ForegroundColor White
    Write-Host "2. Додати Python до PATH" -ForegroundColor White
    Write-Host "3. Перезапустити PowerShell" -ForegroundColor White
    Write-Host ""
    Read-Host "Натисніть Enter для виходу"
    exit 1
}

Write-Host ""

# Перевірка наявності залежностей
Write-Host "Перевірка залежностей..." -ForegroundColor Yellow
try {
    python -c "import pandas, plotly, flask" 2>$null
    Write-Host "✅ Залежності вже встановлено" -ForegroundColor Green
} catch {
    Write-Host "📦 Встановлення залежностей..." -ForegroundColor Yellow
    try {
        python -m pip install -r requirements.txt
        Write-Host "✅ Залежності встановлено успішно" -ForegroundColor Green
    } catch {
        Write-Host "❌ Помилка встановлення залежностей!" -ForegroundColor Red
        Write-Host "Спробуйте встановити вручну:" -ForegroundColor Yellow
        Write-Host "python -m pip install pandas plotly flask flask-cors backtesting pyarrow" -ForegroundColor White
        Read-Host "Натисніть Enter для виходу"
        exit 1
    }
}

Write-Host ""

# Запуск веб-сервера
Write-Host "🚀 Запуск веб-сервера..." -ForegroundColor Cyan
Write-Host ""
Write-Host "📱 Відкрийте браузер та перейдіть на: http://localhost:5002/" -ForegroundColor Yellow
Write-Host "⏹️  Для зупинки натисніть Ctrl+C" -ForegroundColor Yellow
Write-Host ""

try {
    python graphic.py
    Write-Host ""
    Write-Host "✅ Веб-сервер зупинено успішно!" -ForegroundColor Green
} catch {
    Write-Host "❌ Помилка запуску веб-сервера!" -ForegroundColor Red
    Write-Host "Перевірте помилки вище" -ForegroundColor Yellow
}

Write-Host ""
Read-Host "Натисніть Enter для виходу"
