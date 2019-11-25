# Means unknown type
import json
from botSession import bot


def md_unknown(data):
    chat_id = bot.get(data).chat('id')
    rec_text = 'I don\'t know what I\'ve received!'
    bot.send(chat_id).message(rec_text)
    uk_tp_msg = 'Unknown message received.\n' + json.dumps(data)
    resp = bot.send(345060487).message(uk_tp_msg)
    return resp
