# Introduction

GetCohorts provides a web service for assigning users to a cohort of an A/B test.

```python
>>> import requests
>>> resp = requests.get('http://api.getcohorts.com/v1/cohorts', json={
...    'identifier': 'user1',
...    'experiment': 'homepage-test'
... })
>>> print(resp.json()['cohort'])
experimental

```

You can supply a custom list of cohorts of any length.

```python
>>> resp = requests.get('http://api.getcohorts.com/v1/cohorts', json={
...    'identifier': 'user1',
...    'experiment': 'homepage-test',
...    'cohorts': ['control', 'version1', 'version2']
... })
>>> print(resp.json()['cohort'])
version1

```

For reference details of the service, see the documentation site at [http://api.getcohorts.com](http://api.getcohorts.com).

## Getting started

The public endpoint at `http://api.getcohorts.com` is free to use, but is only suitable for testing and proof of concept applications. For production, we recommend deploying GetCohorts yourself.

For instructions on how to deploy the service, see the section on [deploying](http://docs.getcohorts.com/deploying).
