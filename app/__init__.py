import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth

app = flask.Flask(__name__)

host="ec2-107-22-238-112.compute-1.amazonaws.com"
database="dimfu044kiidh"
user="wttxpbzwwyiezo"
port="5432"
password="da62a0b0a27d53b8c813a6eb60df65b636c162a4df0336c00409558a5c3f2c14"
uri="postgres://wttxpbzwwyiezo:da62a0b0a27d53b8c813a6eb60df65b636c162a4df0336c00409558a5c3f2c14@ec2-107-22-238-112.compute-1.amazonaws.com:5432/dimfu044kiidh"
heroku_cli="heroku pg:psql postgresql-metric-77907 --app rpi-iot-logger"



@app.route("/update",methods=["POST"])
def updateinfo():
    if(flask.request.method=="POST"):
        info=flask.request.json
        print(info["temp"])
        print(info["distance"])
        print(info)
        return flask.jsonify(
                message="good test",
                category="success",
                status=200
            )

@app.route("/")
def home_view():
    return "<p>hello</p>"


