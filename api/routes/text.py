from flask_restful import Resource, reqparse
from os import getenv
from database.models import Text, session_creator
from dateutil import parser as date_parser


secret = getenv("API_SECRET", None)

Text_parser = reqparse.RequestParser()
Text_parser.add_argument("secret", dest="secret", location="args")
Text_parser.add_argument(
    "start_date",
    dest="start_date",
    location="args",
    type=lambda x: date_parser.parse(x).date(),
)
Text_parser.add_argument(
    "end_date",
    dest="end_date",
    location="args",
    type=lambda x: date_parser.parse(x).date(),
)


class TextAPI(Resource):
    """ Returns date from the text table

    If an env var named "API_SECRET" is present, then it is required that the request includes an arg called `secret`
    that matches, otherwise 401 unauthorized.

    """

    def prepare_json(self, start_date=None, end_date=None):
        """" TODO: Add support for custom time frames """
        if start_date is None and end_date is None:
            session = session_creator()
            results = session.query(Text).all()
            return [i.as_dict() for i in results]
        if start_date is not None and end_date is None:
            """Return all data since datetime"""
            session = session_creator()
            results = session.query(Text).filter(Text.date >= start_date)
            return [i.as_dict() for i in results]
        if start_date is None and end_date is not None:
            """Return all data after datetime"""
            session = session_creator()
            results = session.query(Text).filter(Text.date <= end_date)
            return [i.as_dict() for i in results]
        if start_date is not None and end_date is not None:
            """Return all data between two datetimes"""
            session = session_creator()
            results = session.query(Text).filter(
                Text.date <= end_date, Text.date >= start_date
            )
            return [i.as_dict() for i in results]

    def get(self):
        args = Text_parser.parse_args()
        if args.secret != secret:
            return "Unauthorized", 401
        return self.prepare_json()
