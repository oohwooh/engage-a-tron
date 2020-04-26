from flask_restful import Resource, reqparse
from os import getenv
from database.models import Voice, session_creator
from dateutil import parser as date_parser

secret = getenv("API_SECRET", None)

Voice_parser = reqparse.RequestParser()
Voice_parser.add_argument("secret", dest="secret", location="args")
Voice_parser.add_argument(
    "start_date",
    dest="start_date",
    location="args",
    type=lambda x: date_parser.parse(x).date(),
)
Voice_parser.add_argument(
    "end_date",
    dest="end_date",
    location="args",
    type=lambda x: date_parser.parse(x).date(),
)


class VoiceAPI(Resource):
    """ Returns date from the voice table

    If an env var named "API_SECRET" is present, then it is required that the request includes an arg called `secret`
    that matches, otherwise 401 unauthorized.

    """

    def prepare_json(self, start_date=None, end_date=None):
        """" TODO: Add support for custom time frames """
        if start_date is None and end_date is None:
            session = session_creator()
            results = session.query(Voice).all()
            return [i.as_dict() for i in results]
        if start_date is not None and end_date is None:
            """Return all data since datetime"""
            session = session_creator()
            results = session.query(Voice).filter(Voice.date >= start_date)
            return [i.as_dict() for i in results]
        if start_date is None and end_date is not None:
            """Return all data after datetime"""
            session = session_creator()
            results = session.query(Voice).filter(Voice.date <= end_date)
            return [i.as_dict() for i in results]
        if start_date is not None and end_date is not None:
            """Return all data between two datetimes"""
            session = session_creator()
            results = session.query(Voice).filter(
                Voice.date <= end_date, Voice.date >= start_date
            )
            return [i.as_dict() for i in results]

    def get(self):
        args = Voice_parser.parse_args()
        if args.secret != secret:
            return "Unauthorized", 401
        return self.prepare_json()
