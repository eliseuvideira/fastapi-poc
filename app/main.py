from fastapi import FastAPI, File, UploadFile

from deepface import DeepFace

from uuid import uuid4


app = FastAPI()


async def save(image: UploadFile):
    file_location = f"/tmp/{uuid4()}"
    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())
    return file_location


@app.post("/")
async def compare_images(current: UploadFile, original: UploadFile):
    current_filepath = await save(current)
    original_filepath = await save(original)

    result = DeepFace.verify(img1_path=current_filepath,
                             img2_path=original_filepath)

    return result
