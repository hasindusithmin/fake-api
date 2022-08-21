from fastapi import FastAPI,HTTPException
from fastapi.responses import RedirectResponse
from faker import Faker
import inspect
import uvicorn


description = """
FakerAPP API helps you do awesome stuff. 🚀

_fake data for testing applications_

[see available path string and descriptions](https://fakerapi.deta.dev/)

![david-travis-WC6-MJ0k-Rz-Gw-unsplash](https://i.ibb.co/H2mqFw3/david-travis-WC6-MJ0k-Rz-Gw-unsplash.jpg)

"""


# Create `app` instance
app = FastAPI(
    title="FakerAPP",
    description=description,
    version="0.0.1",
    contact={
        "name": "Hasindu Sithmin",
        "url": "https://hasindusithmin.github.io/",
        "email": "hasindusithmin64@gmail.com",
    }
)


# Create fake instance 
fake = Faker()


@app.get('/',response_class=RedirectResponse)
def root():
    return '/docs'

@app.get('/endpoints',tags=['It provide all available types'])
def get_endpoint_details():
    funcs = [func for func in dir(fake) if not (func.startswith('_') or func.startswith('__') or func.startswith('seed'))]
    docs = [inspect.getdoc(eval(f'fake.{func}')) for func in funcs]
    desc = []
    for i in range(len(funcs)):
        doc = docs[i]
        desc.append({
            'path':f'/{funcs[i]}',
            'return':str(doc).replace('\n', '')
        })
    return desc

@app.get('/{type}',tags=['Use /endpoints to get available types'])
def get_fake_data(type:str):
    try:
        data =  eval(f'fake.{type}()')
        return {'data':data}
    except:
        raise HTTPException(status_code=404,detail=f"Generator' object has no attribute '{type}.use /endpoints to get available types")
   

if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port=8001)



