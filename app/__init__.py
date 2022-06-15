import flask,requests,json 
import jinja2
from authlib.flask.client import OAuth

app = flask.Flask(__name__)


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


