import ccxt

from trading_system import app
from trading_system.config import BINANCE_API_KEY
from trading_system.config import BINANCE_SECRET_KEY
import requests
from trading_system.models import get_ohcv, get_cci, get_atr, get_macd

# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol="


@app.route('/ohlcv ?(.*)')
def ohlcv_command(message, cmd):
    chat_dest = message['chat']['id']
    table = get_ohcv(cmd)
    for row in table:
        app.send_message(chat_dest, row)


@app.route('/cci ?(.*)')
def cci_command(message, cmd):
    chat_dest = message['chat']['id']
    try:
        table = get_cci(cmd)
        for row in table:
            app.send_message(chat_dest, row)
    except:
        app.send_message(chat_dest, "ERROR")


@app.route('/token ?(.*)')
def token_command(message, cmd):
    """
    Возвращает теущую стоимость токена в USDT.
    :param message: Объект сообщения пользователя
    :param cmd: Переменная команды пользователя, в ней хранится код токена
    :return:
    """
    chat_dest = message['chat']['id']
    try:
        data = requests.get(key + cmd + "USDT").json()
    except:
        app.send_message(chat_dest, "Try other token")
    else:
        msg = f"{data['symbol']} price is {float(data['price'])}"
        app.send_message(chat_dest, msg)


@app.route('/help ?(.*)')
def help_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = """
    Bot commands:
/token [TOKEN NAME] - get a token crypto price from Binance. Token examples: ETH, BTC, DOGE
/ohlcv [TOKEN NAME] get 24 hour info(OHLCV) about token with timeframe = 1h
/cci [TOKEN NAME] get 24 hour cci(Commodity Channel Index) indicator with timeframe=1h and period=20
/binance_api_key [BINANCE PUBLIC KEY] adds users public binance api key to database
/binance_secret_api_key [BINANCE PRIVATE KEY] adds users private binance api key to database
/atr [TOKEN NAME] get 24 hour Average True Range with timeframe = 1h. ATR measures the volatility of token. 
    """
    app.send_message(chat_dest, msg)


@app.route('/binance_api_key ?(.*)')
def set_binance_key_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "KEY ACCEPTED"
    BINANCE_API_KEY = cmd
    app.send_message(chat_dest, msg)


@app.route('/binance_secret_api_key ?(.*)')
def set_secret_binance_key_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "SECRET KEY ACCEPTED"
    BINANCE_SECRET_KEY = cmd
    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)


@app.route('/atr ?(.*)')
def atr_command(message, cmd):
    chat_dest = message['chat']['id']
    try:
        atr = get_atr(cmd)
    except:
        app.send_message(chat_dest, "Try other token")
    else:
        app.send_message(chat_dest, f"Average True Range = {atr:,.2f}")


@app.route('/macd ?(.*)')
def macd_command(message, cmd):
    chat_dest = message['chat']['id']
    table = get_macd(cmd)
    app.send_message(chat_dest, "Time | MACD")
    for row in table:
        app.send_message(chat_dest, row)


@app.route('/start ?(.*)')
def start_command(message, cmd):
    chat_dest = message['chat']['id']
    app.send_message(chat_dest, f"Hello, {message['from']['first_name']}! Type in /help to see what I can do!")
