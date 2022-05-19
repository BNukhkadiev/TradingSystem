"""
Trading System module
-----------------------
Это модуль автоматической торговой системы

"""


import ccxt
from trading_system import config

Band0 = 100
Band1 = -100
in_possition = False

exchange = ccxt.binance({
    'apiKey': config.BINANCE_API_KEY,
    'secret': config.BINANCE_SECRET_KEY
})

from trading_system import bot
