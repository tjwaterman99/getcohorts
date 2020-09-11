# GetCohorts

Allocate users in your experiments to a cohort using our idempotent, random function.

```python
>>> from getcohorts import get_cohort
>>> get_cohort(b'user123', b'experiment')
'experimental'

```

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

## Testing

Run the tests with pytest

```
pytest
```
