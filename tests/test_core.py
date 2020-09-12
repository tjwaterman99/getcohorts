from getcohorts.core import (
    get_cohort, _get_bytes, get_seed, DEFAULT_COHORTS, _format_cohorts
)


def test_get_bytes_converts_bytes():
    assert type(_get_bytes(b'id')) == bytes


def test_get_bytes_converts_strings():
    assert type(_get_bytes('id')) == bytes


def test_get_bytes_converts_integers():
    assert type(_get_bytes(1)) == bytes


def test_get_bytes_converts_floats():
    assert type(_get_bytes(1.5)) == bytes


def test_get_seed_creates_a_seed():
    assert type(get_seed('a', 'b')) == int


def test_format_cohorts_dedupes():
    assert _format_cohorts(['a', 'a']) == ['a']


def test_format_cohorts_sorts():
    assert _format_cohorts(['b', 'a']) == ['a', 'b']


def test_get_seed_returns_same_value_for_different_types():
    assert get_seed(b'1', b'2') == get_seed('1', '2')
    assert get_seed(b'1', b'2') == get_seed(1, 2)
    assert get_seed(b'1', b'2') == get_seed(1.0, 2.0)


def test_get_seed_returns_different_seeds():
    assert get_seed(1, 2) != get_seed(2, 1)
    assert get_seed(1, 3) != get_seed(1, 2)
    assert get_seed(1, 2) != get_seed(2, 2)


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


def test_default_cohorts_are_experimental_and_control():
    assert DEFAULT_COHORTS == ['experimental', 'control']


def test_get_cohorts_ignores_order_of_cohorts():
    first = get_cohort(1, 2, cohorts=['a', 'b'])
    second = get_cohort(1, 2, cohorts=['b', 'a'])
    assert first == second
