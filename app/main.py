from dotenv import load_dotenv
from fastapi import Depends, FastAPI, File, HTTPException, status, UploadFile
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from deepface import DeepFace
from uuid import uuid4
from os import environ

load_dotenv()

app = FastAPI()

security = HTTPBasic()

PYTHON_ENV = environ.get("PYTHON_ENV", "production")
API_BASIC_AUTH_USERNAME = environ.get("API_BASIC_AUTH_USERNAME")
API_BASIC_AUTH_PASSWORD = environ.get("API_BASIC_AUTH_PASSWORD")

async def save(image: UploadFile):
    file_location = f"/tmp/{uuid4()}"
    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())
    return file_location


@app.post("/")
async def compare_images(current: UploadFile, original: UploadFile, credentials: HTTPBasicCredentials = Depends(security)):
    if (credentials.username != API_BASIC_AUTH_USERNAME or credentials.password != API_BASIC_AUTH_PASSWORD):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    current_filepath = await save(current)
    original_filepath = await save(original)

    result = DeepFace.verify(img1_path=current_filepath,
                             img2_path=original_filepath)

    return result
