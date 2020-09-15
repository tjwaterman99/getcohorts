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

## Quickstart

GetCohorts provides a web service at `http://api.getcohorts.com` that you can use for testing. But that service runs on Heroku's free tier, and can occasionally have slow response times. We recommend that you deploy GetCohorts yourself.

The easiest way to deploy GetCohorts is with docker.

```sh
docker run --publish 8000:8000 tjwaterman99/getcohorts
```

For more details on using the service, you can read the documentation and API reference.

- [Documentation](http://docs.getcohorts.com)
- [API Reference](http://api.getcohorts.com)

## Development

Clone this repo.

```bash
git clone https://github.com/tjwaterman99/getcohorts.git
```

Install the package's dependencies, and install `getcohorts` in editable mode.

```
pip install -r requirements.txt
pip install --editable .
```

To run the webserver, install the Heroku cli.

```
sudo snap install --clasic heroku
heroku local
```

The webserver will run on port `8000`.

### Testing

Run the tests with pytest

```
pytest
```

You can run the github CI workflows locally if you have [act](https://github.com/nektos/act) installed. You'll also need to create a file `.secrets` that contains deployment secrets for the staging environments.

```
# .secrets
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
DOCS_S3_BUCKET=...

PYPI_USERNAME=...
PYPI_REPOSITORY_URL=...
PYPI_ACCESS_TOKEN=...
```

Then run the Github workflows.

```
sudo act --secret-file .secrets
```

### Documentation

Build the docs with sphinx-autobuild. The site is available at `0.0.0.0:8000`.

```
sphinx-autobuild docs docs/_build
```
