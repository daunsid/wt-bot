from fastapi import FastAPI, Request, Response, staticfiles
from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session


from wt_bot.api.v1.api import api_router
from wt_bot.core.config import settings
from wt_bot.models import User


app = FastAPI(title="APGAR HEALTH PAL", openapi_url=f"")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 
html_file = open('frontend/template/index.html', 'r').read()


app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

# @app.get("/")
# async def get():
#     return HTMLResponse(html_file)



# @app.on_event("startup")
# async def startup_event():
#     app.html_file = open('frontend/template/index.html', 'r').read()

@app.get("/")
async def get():
    return HTMLResponse(html_file)



app.include_router(api_router)



