import requests
import time
import random
from text import text
import config

spam = None
randnum = -1
t = ""
while True:
    if spam is None:
        spam = time.time()
    elif time.time() - spam >= config.counter:
        spam = None
        if config.rand:
            randnum = random.randint(0, len(text) - 1)
            t = text[randnum]
        else:
            if randnum < len(text) - 1:
                randnum += 1
            else:
                randnum = 0
            t = text[randnum]
        payload = {
            'content': t
        }

        header = {
            'authorization': config.token
        }
        r = requests.post(config.channel_link, data=payload, headers=header)