import string
from random import randrange
import time
import requests
from threading import Thread

terms = string.ascii_letters + string.digits

def randIMGBeta6(rets):
    terms = string.ascii_letters + string.digits
    for a in range(20):
        randList = str()
        for a in range(6):
            randList += terms[randrange(0,62)]
        
        link = "https://i.imgur.com/" + randList + ".jpeg"
        ress = requests.head(link).status_code

        if ress == 200:
            rets.append(link)

def randIMGBeta7(rets):
    terms = string.ascii_letters + string.digits
    for a in range(20):
        randList = str()
        for a in range(7):
            randList += terms[randrange(0,62)]
        
        link = "https://i.imgur.com/" + randList + ".jpeg"
        ress = requests.head(link).status_code

        if ress == 200:
            rets.append(link)

def requestFastBeta6(itr):
    threads = list()
    rets = list()
    for i in range(itr):
        x = Thread(target=randIMGBeta6, args=(rets,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()

    return rets

def requestFastBeta7(itr):
    threads = list()
    rets = list()
    for i in range(itr):
        x = Thread(target=randIMGBeta7, args=(rets,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()

    return rets

if __name__ == "__main__":
    t = time.time()
    for i in range(10):
        requestFastBeta6(20)
    print("6 chars: " + str(time.time() - t))

    t = time.time()
    for i in range(10):
        requestFastBeta7(20)
    print("7 chars: " + str(time.time() - t))