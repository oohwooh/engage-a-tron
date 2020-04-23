from sqlalchemy import *
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.schema import UniqueConstraint

from os import getenv
from datetime import datetime

postgres_db = {
    "drivername": "postgres",
    "username": getenv("DB_USERNAME", "postgres"),
    "password": getenv("DB_PASSWORD", "rceF^rx71WHq"),
    "database": getenv("DB_DB", "engagement"),
    "host": getenv("DB_HOST", "localhost"),
    "port": 5432,
}
postgres_url = URL(**postgres_db)
engine = create_engine(postgres_url)
metadata = MetaData()

Base = declarative_base(bind=engine, metadata=metadata)


class Online(Base):
    __tablename__ = "online"

    id = Column(Integer, primary_key=True)
    discord_user_id = Column(BIGINT, nullable=False)
    date = Column(Date, nullable=False, default=datetime.now().date())
    online = Column(Boolean, nullable=False, default=True)

    UniqueConstraint(discord_user_id, date, name="unique_user_per_day_constraint")

    def __repr__(self):
        return f"{self.discord_user_id}"


class Voice(Base):
    __tablename__ = "voice"

    id = Column(Integer, primary_key=True)
    discord_user_id = Column(BIGINT, nullable=False)
    date = Column(Date, nullable=False, default=datetime.now().date())
    vc_id = Column(BIGINT, nullable=False)
    is_team_channel = Column(Boolean, nullable=False)

    def __repr__(self):
        if self.is_team_channel:
            return f"{self.discord_user_id} joined team vc {self.vc_id} on {self.date}"
        else:
            return (
                f"{self.discord_user_id} joined non-team vd {self.vc_id} on {self.date}"
            )


class Text(Base):
    __tablename__ = "text"

    id = Column(Integer, primary_key=True)
    discord_user_id = Column(BIGINT, nullable=False)
    date = Column(Date, nullable=False, default=datetime.now().date())
    is_team_channel = Column(Boolean, nullable=False)

    def __repr__(self):
        if self.is_team_channel:
            return f"{self.discord_user_id} messaged in a team channel on  {self.date}"
        else:
            return (
                f"{self.discord_user_id} messaged in a non-team channel on  {self.date}"
            )


def session_creator() -> Session:
    session = sessionmaker(bind=engine)
    return session()
