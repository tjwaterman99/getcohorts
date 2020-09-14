
def test_version_is_set():
    from getcohorts import __version__
    assert type(__version__) == str


def test_imports():
    from getcohorts import get_cohort
    from getcohorts import get_seed
    from getcohorts import DEFAULT_COHORTS

    assert callable(get_cohort)
    assert callable(get_seed)
    assert type(DEFAULT_COHORTS) == list
