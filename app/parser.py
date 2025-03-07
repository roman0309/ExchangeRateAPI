import requests
import xml.etree.ElementTree as ET
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import CurrencyRate

CBR_URL = "https://www.cbr.ru/scripts/XML_daily.asp"

def update_currency_rates():
    response = requests.get(CBR_URL)
    if response.status_code != 200:
        print("Ошибка загрузки данных")
        return

    root = ET.fromstring(response.content)
    db: Session = SessionLocal()

    for valute in root.findall("Valute"):
        code = valute.find("CharCode").text
        value = float(valute.find("Value").text.replace(",", "."))

        rate = db.query(CurrencyRate).filter(CurrencyRate.currency == code).first()
        if rate:
            rate.rate = value
        else:
            rate = CurrencyRate(currency=code, rate=value)
            db.add(rate)

    db.commit()
    db.close()
    print("Курсы валют обновлены!")
