from random import random
import requests
from threading import Thread
from flask import request, render_template, redirect, url_for, session, Flask
import json
from concurrent.futures import ThreadPoolExecutor
from waitress import serve

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


# route for main page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
    # with ThreadPoolExecutor() as executor:
    #     future = [executor.submit(randIMG) for x in range(10)]
    #     returnVal = [f.result() for f in future]
    #     return str(json.dumps(returnVal))
    # que = Queue()
    # requestFast(10)
    # #randIMG()
    # result = que.get()
    return str(json.dumps(requestFast(49)))


def randIMG(ret):
    imgList = str()
    imgStr = list()
    if random() > 0.2:
        length = 5
    else:
        length = 7
    id = str(random())[2:(length+2)]
    image = "https://i.imgur.com/" + id + "s.jpg" 
    img = requests.get(image).url
    if img != "https://i.imgur.com/removed.png":
        imgList = img.strip()
        print(imgList)
        ret.append(imgList)
    else:
        randIMG(ret)
    
        
def requestFast(itr):
    threads = list()
    rets = list()
    for i in range(itr):
        x = Thread(target=randIMG, args=(rets,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()

    return rets

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080, threads=2)

#requestFast(100)
#input()
