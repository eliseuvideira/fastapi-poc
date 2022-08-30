FROM python:3.7

RUN apt-get update && apt-get install -y python3-opencv

RUN pip install opencv-python

RUN mkdir -p /root/.deepface/weights

RUN curl -L https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5 -o /root/.deepface/weights/vgg_face_weights.h5

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
