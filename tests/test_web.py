
def test_get_index(test_client):
    resp = test_client.get('/')
    assert resp.status_code == 200


def test_read_health(test_client):
    resp = test_client.get('/health')
    assert resp.status_code == 200
    assert resp.json()['healthy'] is True


def test_read_seed(test_client):
    json = {
        'identifier': 1,
        'experiment': 'test'
    }
    resp = test_client.get('/seeds', json=json)
    assert resp.status_code == 200
    assert type(resp.json()['seed']) == int
    assert resp.json()['params'] == json


def test_read_cohort(test_client):
    json = {
        'identifier': 1,
        'experiment': 'test'
    }
    resp = test_client.get('/cohorts', json=json)
    assert resp.status_code == 200
    assert type(resp.json()['cohort']) == str
    assert resp.json()['params'] == json
