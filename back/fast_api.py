from fastapi import FastAPI, File, UploadFile
from tools import predict
import os
import numpy as np

app = FastAPI()

@app.get("/api")
def read_root():
    return {"message": "Welcome to the API!"}


@app.post("/api/upload")
async def create_upload_file(file: UploadFile = File(...)):
    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as file_object:
        file_object.write(file.file.read())

    json_return = predict(file_location)

    print(json_return)


    return json_return
