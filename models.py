from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ChatMessage(Base):
    __tablename__ = "messages"

    id = Column("id", Integer, primary_key=True)
    text = Column("text", String)
    message_id = Column("message_id", String, unique=True)
    author = Column("author", String)
    date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
