import json
from botSession import bot
from starting import getadminid


def md_debug(data):
    admin_id = getadminid()
    debug_msg = json.dumps(data)
    resp = bot.send(admin_id[0]).message(debug_msg)
    """
    if log:
        sendfile(admin_id[0], 'log/log.csv', False, 'upload')
    if os.name == 'nt':
        scrst = scrshot.grab()
        scrst.save('log/screenshot.png')
        sendphoto(admin_id, 'log/screenshot.png', False, 'upload')
    """
    return resp
