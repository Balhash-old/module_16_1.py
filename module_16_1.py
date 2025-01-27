from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main_page():
    return "Главная страница"


@app.get("/user/admin")
async def admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def user_number(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def user_age(username: str, age: int):
    return f"Информация о пользователе. Имя:{username}, возраст:{age},"


