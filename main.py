from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {'message':'Hello World'}

@app.get('/inicio')
async def ruta_de_prueba():
    return 'Hello World from FastApi'