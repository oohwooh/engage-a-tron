from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

from api.routes import OnlineAPI, VoiceAPI, TextAPI

api.add_resource(OnlineAPI, "/online")
api.add_resource(VoiceAPI, "/voice")
api.add_resource(TextAPI, "/text")

if __name__ == "__main__":
    app.run(debug=True)
