from random import Random
from typing import Any
import hashlib


DEFAULT_COHORTS = ['experimental', 'control']


def _get_bytes(value: Any) -> bytes:
    if type(value) == bytes:
        return value
    elif type(value) == str:
        return value.encode('utf8')
    elif type(value) == float:
        if value == int(value):
            return str(int(value)).encode('utf8')
        else:
            return str(value).encode('utf8')
    else:
        return str(value).encode('utf8')


def get_seed(identifier: Any, experiment: Any) -> int:
    identifier = _get_bytes(identifier)
    experiment = _get_bytes(experiment)
    hexdigest = hashlib.md5(identifier + experiment).hexdigest()
    seed = int(hexdigest, 16)
    return seed


def get_cohort(identifier: Any, experiment: Any, cohorts=DEFAULT_COHORTS):
    seed = get_seed(identifier, experiment)
    random = Random()
    random.seed(seed)
    index = int(random.random() * len(cohorts))
    return cohorts[index]
