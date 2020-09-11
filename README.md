# GetCohorts

Allocate users in your experiments to a cohort using our idempotent function.

```python
>>> from getcohorts import get_cohort
>>> get_cohort(b'user123', b'experiment', cohorts=['experimental', 'control'])
'experimental'

```

Using `get_cohort` will randomly assign a user to a cohort, but always assigns that user to the same cohort for the same `experiment`.

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

### Testing

Run the tests with pytest

```
pytest
```

### Documentation

Build the docs with sphinx-autobuild. The site is available at `0.0.0.0:8000`.

```
sphinx-autobuild docs docs/_build
```
