import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, sessionmaker, declared_attr

DB_HOST = "147.45.184.12"
DB_USER = "1_Ogurcov"
DB_PASSWORD = "HH6kjRG5bSPxfFXD"
DB_NAME = "1_Ogurcov"


DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"

# Асинхронный движок
engine = create_async_engine(DATABASE_URL, echo=False)

class Base(DeclarativeBase):
    pass

# Асинхронная сессия
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Функция для инициализации БД
# Создание таблиц в бд по моделям
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Функция получения сессий для работы с бд
async def get_session():
    async with SessionLocal() as session:
        yield session