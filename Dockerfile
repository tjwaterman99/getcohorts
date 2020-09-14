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

# This isn't listening to interrupt signals and stopping the container.
# https://hynek.me/articles/docker-signals/ might have some insight as
# to how to fix
CMD gunicorn --bind=0.0.0.0:$PORT --workers=2 --threads=4 --worker-class=uvicorn.workers.UvicornWorker --worker-tmp-dir=/dev/shm getcohorts.web:app
