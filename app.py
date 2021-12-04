from random import random, randrange
from flask.wrappers import Request
import requests
from threading import Thread
from flask import request, render_template, Flask
import json
from waitress import serve
import time
import string

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# route for main page
@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/image/")
# def image():
#     Request.form

@app.route("/alpha")
def alpha():
    return render_template("index_alpha.html")

@app.route("/beta")
def beta():
    return render_template("index_beta.html")

@app.route("/api/beta")
def apiBeta():
    try:
        return str(json.dumps(requestFastBeta(50)))
    except Exception as e:
        return str(json.dumps(requestFastBeta(25)))

@app.route("/api")
def api():
    return str(json.dumps(requestFast(50)))


def randIMGBeta(rets):
    terms = string.ascii_letters + string.digits
    for a in range(20):
        randList = str()
        for a in range(6):
            randList += terms[randrange(0,62)]
        
        link = "https://i.imgur.com/" + randList + ".jpeg"
        ress = requests.head(link).status_code

        if ress == 200:
            rets.append(link)

        # if ress != "https://i.imgur.com/removed.png":
        #     if ress != "https://imgur.com/" + randList:
        #         rets.append(ress)
        #         # print(ress)

def requestFastBeta(itr):
    threads = list()
    rets = list()
    for i in range(itr):
        x = Thread(target=randIMGBeta, args=(rets,))
        threads.append(x)
        x.start()
    for index, thread in enumerate(threads):
        thread.join()

    return rets


def randIMG(ret):
    imgList = str()
    imgStr = list()
    if random() > 0.2:
        length = 5
    else:
        length = 7
    id = str(random())[2:(length+2)]
    image = "https://i.imgur.com/" + id + "s.jpg" 
    img = requests.head(image).status_code
    #if img != "https://i.imgur.com/removed.png":
    if img == 200:
        imgList = image.strip()
        #print(imgList)
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

