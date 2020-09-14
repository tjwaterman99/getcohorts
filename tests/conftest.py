import sys
from pytest import fixture
from fastapi.testclient import TestClient

# pytest can't import the `getcohorts` package without having `.` in PYTHONPATH
sys.path.append('.')

from getcohorts.web import v1, app  # noqa


@fixture()
def test_client():
    return TestClient(v1)
