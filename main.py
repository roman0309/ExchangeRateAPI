from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.database import engine
from app.models import Base
from app.updater import scheduler
from app.parser import update_currency_rates

app = FastAPI()

# 🔥 CORS Middleware для разрешения запросов с фронтенда
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем запросы от всех доменов
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, DELETE и т. д.)
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Создаем таблицы в БД
Base.metadata.create_all(bind=engine)

# Подключаем маршруты API
app.include_router(router)

# Обновляем курсы при запуске сервера (чтобы не ждать первый запуск планировщика)
update_currency_rates()

# 🚀 Проверяем, не запущен ли планировщик, перед стартом
if not scheduler.running:
    scheduler.start()
