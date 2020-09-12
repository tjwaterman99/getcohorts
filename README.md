# GetCohorts

Allocate users in your experiments to a cohort using our random, idempotent resource.

```bash
curl http://api.getcohorts.com/v1/cohorts \
    -X GET \
    -d '{"identifier": "user1", "experiment": "homepage-test"}'
```

The endpoint will randomly assign the user `user1` to a cohort for the experiment `homepage-test`, but is gauranteed to always assign the same user to the same cohort for the same `experiment`.

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
