from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import CurrencyRate

router = APIRouter()


@router.get("/rate/{currency}")
def get_exchange_rate(currency: str, db: Session = Depends(get_db)):
    rate = db.query(CurrencyRate).filter(CurrencyRate.currency == currency.upper()).first()
    if not rate:
        raise HTTPException(status_code=404, detail="Валюта не найдена")

    return {"currency": currency.upper(), "rate": rate.rate}


@router.get("/rates")
def get_all_rates(db: Session = Depends(get_db)):
    rates = db.query(CurrencyRate).all()
    return {rate.currency: rate.rate for rate in rates}
