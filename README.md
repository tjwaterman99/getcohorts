# GetCohorts

[![CI Actions Status](https://github.com/tjwaterman99/getcohorts/workflows/CI/badge.svg)](https://github.com/tjwaterman99/getcohorts/actions)
[![PyPI version](https://badge.fury.io/py/getcohorts.svg)](https://badge.fury.io/py/getcohorts)
[![codecov](https://codecov.io/gh/tjwaterman99/getcohorts/branch/master/graph/badge.svg)](https://codecov.io/gh/tjwaterman99/getcohorts)

GetCohorts provides an endpoint that will randomly determine a cohort for a user in an A/B test, and is gauranteed to always assign the same user to the same cohort for the same experiment.

```python
>>> import requests
>>> resp = requests.get('http://api.getcohorts.com/v1/cohorts', json={
...    'identifier': 'user1',
...    'experiment': 'homepage-test'
... })
>>> print(resp.json()['cohort'])
experimental

```

More details on using the service are available on the documentation site.

- [Documentation](http://docs.getcohorts.com)
- [API Reference](http://api.getcohorts.com)

## Quickstart

GetCohorts provides a web service at `http://api.getcohorts.com` that you can use for testing. But that service runs on Heroku's free tier, and can occasionally have slow response times. 

We recommend that you deploy GetCohorts yourself.

The easiest way to deploy GetCohorts is with docker.

```sh
docker run --publish 8000:8000 tjwaterman99/getcohorts
```

## Development

Clone this repo.

```bash
git clone https://github.com/tjwaterman99/getcohorts.git
```

Install the package's dependencies. This will also install `getcohorts` in editable mode.

```
pip install -r requirements.txt
```

Run the uvicorn server locally in development mode.

```
uvicorn getcohorts.web:app --host 0.0.0.0 --port 8000 --reload
```

### Testing

Run the tests with pytest. Note that the tests assume the webserver is running locally on port 8000, and they will fail if you have not started the webserver.

```
pytest
```

You can run the github CI workflows locally if you have [act](https://github.com/nektos/act) installed. 

```
act
```

### Documentation

Build the docs with mkdocs. The site is available at `0.0.0.0:8000`.

```
mkdocs serve
```
