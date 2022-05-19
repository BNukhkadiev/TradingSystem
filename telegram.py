from telebot import TeleBot

app = TeleBot(__name__)


@app.route('/command ?(.*)')
def example_command(message, cmd):
    """

    :param message:
    :param cmd:
    :return:
    """
    chat_dest = message['chat']['id']
    msg = "Command Recieved: {}".format(cmd)

    app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    """

    :param message:
    :return:
    """
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)


if __name__ == '__main__':
    with open('api_key.txt', 'r') as f:
        app.config['api_key'] = f.readline()
    app.poll(debug=True)
