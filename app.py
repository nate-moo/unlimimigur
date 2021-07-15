from random import random
import requests
from threading import Thread
from flask import request, render_template, Flask
import json
from waitress import serve

app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

# route for main page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api")
def api():
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

#requestFast(100)
#input()
