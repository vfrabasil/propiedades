  
"""
Real State ML API
API prediction house price in B.A.
v22.04 April 2022

Author: @VictorFrabasil
Mail: vfrabasil@gmail.com
"""

from fastapi import FastAPI
from typing import Optional
import pickle
from pydantic import BaseModel 

class House(BaseModel):
    barrio: str
    m2: int
    rooms: int
    bathrooms: int
    years: int

app = FastAPI(title="Real State ML API", description="API prediction house price in B.A.", version="1.0")

# load model and saved sample
with open('models/model.pkl' , 'rb') as f:
    model = pickle.load(f)
with open('models/sample.pkl' , 'rb') as f:
    house = pickle.load(f)

#@app.on_event('startup')
#async def load_model():


@app.get('/')
async def root():
    return {'message':'Hello World'}


@app.get('/inicio')
async def ruta_de_prueba():
    return 'Prediction House Price in B.A. from FastApi'


@app.post('/predict') #, tags=["predictions"])
async def get_prediction(data : House):
    received = data.dict()

    # set all values to 0
    for col in house.columns:
        house[col].values[:] = 0

    # set 1 to barrio:
    for col in house.columns[4:]:
        if received['barrio'] in col:
            house[col] = 1

    house['m2'] = received['m2']
    house['rooms'] = received['rooms']
    house['bathrooms'] = received['bathrooms']
    house['years'] = received['years']

    print(house)
    prediction = model.predict(house).tolist()

    return {"prediction": prediction}


#if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)

