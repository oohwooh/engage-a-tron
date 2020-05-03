from flask_restful import Resource, reqparse
from os import getenv
from database.models import Online, session_creator
from dateutil import parser as date_parser

secret = getenv("API_SECRET", None)

online_parser = reqparse.RequestParser()
online_parser.add_argument("secret", dest="secret", location="args")
online_parser.add_argument(
    "start_date",
    dest="start_date",
    location="args",
    type=lambda x: date_parser.parse(x).date(),
)
online_parser.add_argument(
    "end_date",
    dest="end_date",
    location="args",
    type=lambda x: date_parser.parse(x).date(),
)


class OnlineAPI(Resource):
    """ Returns date from the online table

    If an env var named "API_SECRET" is present, then it is required that the request includes an arg called `secret`
    that matches, otherwise 401 unauthorized.

    Plan to implement a time range filter

    """

    def prepare_json(self, start_date=None, end_date=None):
        """" TODO: Add support for custom time frames """
        if start_date is None and end_date is None:
            """Return all data"""
            session = session_creator()
            results = session.query(Online).all()
            session.close()
            return [i.as_dict() for i in results]
        if start_date is not None and end_date is None:
            """Return all data since datetime"""
            session = session_creator()
            results = session.query(Online).filter(Online.date >= start_date)
            session.close()
            return [i.as_dict() for i in results]
        if start_date is None and end_date is not None:
            """Return all data after datetime"""
            session = session_creator()
            results = session.query(Online).filter(Online.date <= end_date)
            session.close()
            return [i.as_dict() for i in results]
        if start_date is not None and end_date is not None:
            """Return all data between two datetimes"""
            session = session_creator()
            results = session.query(Online).filter(
                Online.date <= end_date, Online.date >= start_date
            )
            session.close()
            return [i.as_dict() for i in results]

    def get(self):
        args = online_parser.parse_args()
        if args.secret != secret:
            return "Unauthorized", 401
        return self.prepare_json(args.start_date, args.end_date)
