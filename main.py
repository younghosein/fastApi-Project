import os
import sys
import pkg_resources
from fastapi import FastAPI , status, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# from pathlib import Path
public_path = pkg_resources.resource_filename(__name__, 'public')

os.chdir("..")
sys.path.append(os.getcwd())

project_folder = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = project_folder
load_dotenv(os.path.join(project_folder, '.env'))


from api.v1.api import api_router
from core.config import settings


app = FastAPI(
    title="pishkhan",
    debug=True
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()[0]["msg"]}),
    )

app.mount("/public", StaticFiles(directory=public_path), name="public")


# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
       CORSMiddleware,
       allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
    )

app.include_router(api_router, prefix=settings.API_V1_STR)