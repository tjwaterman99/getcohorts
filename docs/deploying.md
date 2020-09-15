# Deploying GetCohorts

You can deploy GetCohorts with Docker or by downloading the package from PyPI.

## Docker

```
docker run --publish 8000:8000 tjwaterman99/getcohorts
```

## PyPI

Ensure you have Python version 3.6+.

```
python --version
```

Install GetCohorts from PyPI.

```
python -m pip install getcohorts
```

You can now run the webserver with `gunicorn`.

```
gunicorn --bind 0.0.0.0:8000 \
    --workers 2 \
    --worker-class uvicorn.workers.UvicornWorker \
    getcohorts.web:app
```
