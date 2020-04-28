from flask import Flask, send_from_directory
from flask_restful import Resource, Api
import os, sys, inspect

# Long story short, imports bad.
# This is needed to allow the cogs to import database, as python doesn't check in the parent directory otherwise.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

app = Flask(__name__)
api = Api(app)

from api.routes import OnlineAPI, VoiceAPI, TextAPI

api.add_resource(OnlineAPI, "/online")
api.add_resource(VoiceAPI, "/voice")
api.add_resource(TextAPI, "/text")


@app.route("/apidocs", methods=["GET"])
def apidocs():
    return send_from_directory("./static/", "redoc-static.html")


if __name__ == "__main__":
    app.run(debug=True)
