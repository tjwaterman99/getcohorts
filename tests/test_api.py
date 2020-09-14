import os

import pytest
import requests


@pytest.fixture()
def host():
    host = f"{os.environ.get('GETCOHORTS_API_URL') or 'http://0.0.0.0:8000'}"
    return host + "{route}"


@pytest.fixture()
def params():
    return {'identifier': 1, 'experiment': 2}


def test_index(host):
    resp = requests.get(host.format(route='/'))
    assert resp.status_code == 200


def test_v1_index(host):
    resp = requests.get(host.format(route='/v1'))
    assert resp.status_code == 200


def test_v1_seeds(host, params):
    resp = requests.get(host.format(route='/v1/seeds'), json=params)
    assert resp.status_code == 200


def test_v1_cohorts(host, params):
    resp = requests.get(host.format(route='/v1/cohorts'), json=params)
    assert resp.status_code == 200
