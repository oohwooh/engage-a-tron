from flask_restful import Resource, reqparse
from os import getenv
from database.models import Voice, session_creator

secret = getenv("API_SECRET", None)

online_parser = reqparse.RequestParser()
online_parser.add_argument(
    "secret", dest="secret",
    location="args"
)


class VoiceAPI(Resource):
    """ Returns date from the online table

    If an env var named "API_SECRET" is present, then it is required that the request includes an arg called `secret`
    that matches, otherwise 401 unauthorized.

    Plan to implement a time range filter

    """

    def prepare_json(self, start_time=None, end_time=None):
        """" TODO: Add support for custom time frames """
        if start_time is None and end_time is None:
            session = session_creator()
            results = session.query(Voice).all()
            return [i.as_dict() for i in results]

    def get(self):
        args = online_parser.parse_args()
        if args.secret != secret:
            return "Unauthorized", 401
        return self.prepare_json()
