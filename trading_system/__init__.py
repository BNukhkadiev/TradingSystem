"""
Trading System module
-----------------------
Это модуль автоматической торговой системы

"""

import ccxt
from trading_system import config
from trading_system.telegram import app

app.config['api_key'] = config.TELEGRAM_API_KEY
Band0 = 100
Band1 = -100
in_position = False

exchange = ccxt.binance({
    'apiKey': config.BINANCE_API_KEY,
    'secret': config.BINANCE_SECRET_KEY
})

app.poll(debug=True)


