from flask import Flask,request,redirect,url_for,render_template
from flask_socketio import SocketIO, emit
from kazoo.client import *
import configs
from Fans import Fans
    
fan=Fans()

app = Flask(__name__, static_folder="static", static_url_path="/")
app.config.from_object(configs)
socketio = SocketIO(app,logger=True)
flag=False
path="/"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    place=request.form['Stadium']
    time=request.form['Time']
    print(time)
    try:
        result=fan.search("/"+place+"/"+time)
        return render_template("index.html", result="Result: ", score=result)
    except:
        return render_template("index.html", result="Result: ", score="No competition")
    
@app.route("/subscribe", methods=['POST'])
def subscribe():
    global path
    path="/"+request.form['Stadium']
    print(path)
    return render_template("index.html",result_sub="Result: ")

@socketio.on('subscribe')
def push():
    global flag
    global path
    flag=False
    while (True):
        socketio.sleep(1)
        fan.subscribe(path)
        if fan.Mark():
            result=fan.subscribe_result(path)
            fan.Lock()
            socketio.send(result)
        if(flag):
            break
            
@socketio.on('stop')
def stop():
    global flag
    flag=True
    socketio.send("stop")
    


    
if __name__ == "__main__":
    socketio.run(app)
