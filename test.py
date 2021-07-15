import string
import random
import requests
from threading import Thread

terms = string.ascii_letters + string.digits

def randIMGBeta(rets):
    for a in range(20):
        randList = str()
        for a in range(6):
            randList += terms[random.randrange(0,62)]
        
        link = "https://i.imgur.com/" + randList + ".jpeg"
        ress = requests.get(link).url

        if ress != "https://i.imgur.com/removed.png":
            if ress != "https://imgur.com/" + randList:
                rets.append(ress)

def requestFastBeta(itr):
    threads = list()
    rets = list()
    for i in range(itr):
        x = Thread(target=randIMG, args=(rets,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()

    return rets

print(requestFast(10))

    #res = link if ress != "https://i.imgur.com/removed.png" or ress != "https://imgur.com/" + randList else "None"
    #print(res)