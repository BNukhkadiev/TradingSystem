from telebot import TeleBot
import json
import requests

app = TeleBot(__name__)

# defining key/request url
key = "https://api.binance.com/api/v3/ticker/price?symbol="


@app.route('/token ?(.*)')
def currency_command(message, cmd):
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
    """
    app.send_message(chat_dest, msg)


@app.route('/binance_key ?(.*)')
def help_command(message, cmd):
    chat_dest = message['chat']['id']
    msg = "KEY ACCEPTED"
    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)


