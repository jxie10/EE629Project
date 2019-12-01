from bottle import get,post,run,request,template
@get("/")
def index():
    return template("index")
@post("/cmd")
def cmd():
    print("pressed: "+request.body.read().decode())
#set host to your raspberrypi's IP
run(host="192.168.1.20",port="8080")
