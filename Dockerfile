FROM python:3.7.9

ENV PORT=8000
EXPOSE 8000

WORKDIR /app

COPY ./getcohorts /app/getcohorts
COPY ./requirements.txt /app/requirements.txt
COPY ./setup.cfg /app/setup.cfg
COPY ./setup.py /app/setup.py
COPY ./README.md /app/README.md

RUN pip install .

CMD gunicorn --bind=0.0.0.0:$PORT --workers=2 --threads=4 --worker-class=uvicorn.workers.UvicornWorker --worker-tmp-dir=/dev/shm getcohorts.web:app
