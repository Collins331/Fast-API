# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {'name': "Collins", 'email': "coduor24@gmail.com"}}

