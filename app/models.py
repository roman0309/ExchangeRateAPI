from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class CurrencyRate(Base):
    __tablename__ = "rates"

    currency = Column(String, primary_key=True, index=True)
    rate = Column(Float, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
