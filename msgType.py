from botSession import bot
from mdGroup import Group
from mdPriv import Private
from mdUnknown import md_unknown


def msg_type(data):
    chat_id = bot.get(data).chat('id')
    message_type = bot.get(data).message('type')

    if chat_id < 0:
        if 'message' in data:
            grp = Group(data)
            if 'new' in message_type:
                resp = grp.new_member()
            elif 'text' in message_type:
                resp = grp.text()
            else:
                resp = message_type
        else:
            resp = message_type

    elif chat_id == 0:
        resp = 'Can\'t get chat id.'

    else:
        priv = Private(data)
        if 'text' in message_type:
            resp = priv.text()
        elif 'sticker' in message_type:
            resp = priv.sticker()
        elif 'photo' in message_type:
            resp = priv.photo()
        elif 'video' in message_type:
            resp = priv.video()
        elif 'animation' in message_type:
            resp = priv.gif()
        elif 'document' in message_type:
            resp = priv.file()
        elif 'edited message' in data:
            resp = message_type
        else:
            resp = message_type

    if chat_id > 0 and 'undefined' in message_type:
        resp = md_unknown(data)

    return resp
