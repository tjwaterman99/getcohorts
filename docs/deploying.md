# Deploying GetCohorts

You can deploy GetCohorts with Docker, Heroku, or by downloading the package from PyPI.

## Docker

```
docker run --publish 8000:8000 tjwaterman99/getcohorts
```

## Heroku

You'll need to create an account on heroku.com, and then you can deploy the app by clicking the button below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/tjwaterman99/getcohorts/tree/master)

## PyPI

Ensure you have Python version 3.6+ installed.

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

## Next Steps

For an overview of the API, you can view the API reference docs at [http://api.getcohorts.com](http://api.getcohorts.com).
