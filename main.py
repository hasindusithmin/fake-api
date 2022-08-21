from fastapi import FastAPI
from fastapi.responses import RedirectResponse


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


@app.get('/',response_class=RedirectResponse)
def root():
    return '/docs'


