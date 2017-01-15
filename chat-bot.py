import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiurl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : KEY,
        'info' : msg,
        'userid' : 'andy_bot',
    }
    try:
        r = requests.post(apiurl, data=data).json()

        return r.get('text')

    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_response(msg):

    defaultReply = 'I received: ' + msg['Text']

    reply = get_response(msg['Text'])

    return reply or defaultReply


itchat.auto_login(hotReload = True)
itchat.run()







