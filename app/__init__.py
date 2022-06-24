import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth
import psycopg2
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

        distance=info["distance"]
        temp=info["temp"]
        
        command="SELECT Led1, Led2 FROM abhi_table"
        conn=psycopg2.connect(uri, sslmode='require')
        cur=conn.cursor()
        cur.execute(command)

        led1,led2=cur.fetchone()

        if(led1==True):
            led1="TRUE"
        else:
            led1="FALSE"

        if(led2==True):
            led2="TRUE"
        else:
            led2="FALSE"

        
        command="INSERT INTO abhi_table (Temperature, Distance, Led1, Led2) VALUES("+str(temp)+", "+str(distance)+", "+led1+", "+led2+")"

        cur.execute(command)
        conn.commit()
        
        conn.close()

        
        return flask.jsonify(
                message="good test",
                category="success",
                status=200
            )

@app.route("/")
def home_view():
    return "<p>hello</p>"


