"""
Trading System module
-----------------------
Это модуль автоматической торговой системы

"""

from trading_system import config
from telebot import TeleBot

app = TeleBot(__name__)
app.config['api_key'] = config.TELEGRAM_API_KEY
from trading_system import routes
