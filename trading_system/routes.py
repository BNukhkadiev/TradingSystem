from trading_system import app
from trading_system.config import BINANCE_API_KEY
from trading_system.config import BINANCE_SECRET_KEY
import requests
from trading_system.models import get_ohcv, get_cci

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
    chat_dest = message['chat']['id']
    data = requests.get(key + cmd + "USDT").json()
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
