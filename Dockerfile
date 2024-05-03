FROM python:3.12.0

#RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir /seashells-backend

WORKDIR seashells-backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000