from getcohorts.core import get_cohort, DEFAULT_COHORTS


def test_get_cohorts_returns_a_default_cohort():
    assert get_cohort(b'1', b'experiment') in DEFAULT_COHORTS


def test_get_cohorts_returns_multiple_cohorts():
    results = []
    for i in range(1000):
        identifier = str(i).encode('utf8')
        results.append(get_cohort(identifier, b'experiment'))
    assert len(set(results)) == 2
    assert len([r for r in results if r == DEFAULT_COHORTS[0]]) > 400


def test_get_cohorts_returns_same_cohort_for_same_identifier():
    results = []
    identifier = b'1'
    experiment = b'experiment'
    for i in range(1000):
        results.append(get_cohort(identifier, experiment))
    assert len(set(results)) == 1


def test_default_cohorts_remain_static():
    assert DEFAULT_COHORTS == ['experimental', 'control']
