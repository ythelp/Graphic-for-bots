@echo off
echo === TradingView-подібний графік свічок - Веб-версія ===
echo.

REM Перевірка наявності Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Помилка: Python не знайдено!
    echo.
    echo Спробуйте:
    echo 1. Встановити Python з python.org
    echo 2. Додати Python до PATH
    echo 3. Перезапустити командний рядок
    echo.
    pause
    exit /b 1
)

echo Python знайдено!
echo.

REM Перевірка наявності залежностей
echo Перевірка залежностей...
python -c "import pandas, plotly, flask" >nul 2>&1
if %errorlevel% neq 0 (
    echo Встановлення залежностей...
    python -m pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo Помилка встановлення залежностей!
        echo Спробуйте встановити вручну:
        echo python -m pip install pandas plotly flask flask-cors backtesting pyarrow
        pause
        exit /b 1
    )
)

echo Залежності встановлено!
echo.

REM Запуск веб-сервера
echo Запуск веб-сервера...
echo.
echo 📱 Відкрийте браузер та перейдіть на: http://localhost:5002/
echo ⏹️  Для зупинки натисніть Ctrl+C
echo.

python graphic.py

echo.
echo Веб-сервер зупинено!
pause
