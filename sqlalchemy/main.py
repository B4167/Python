from infrastructure.database.db_gateway import init_db, Base, engine
import asyncio

from domain.users.models.user import User

from domain.roles.models.role import Role

from domain.user_role_relations.models.user_role_relation import UserRoleRelation


# Основная функция в которой выполняем инициализацию бд
async def main():
    await init_db()


# Асинхронный запуск функции, так как мы используем асинхронное подключение к бд
asyncio.run(main())