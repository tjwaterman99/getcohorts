from random import Random
from typing import Any, List
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


def _format_cohorts(cohorts: List[str]):
    return list(sorted(set(cohorts)))


def get_seed(identifier: Any, experiment: Any) -> int:
    """
    Convert any combination of identifier and experiment to a random integer.

    Calling this function with the same identifier and experiment value
    will return the same integer every time.
    """

    identifier = _get_bytes(identifier)
    experiment = _get_bytes(experiment)
    hexdigest = hashlib.md5(identifier + experiment).hexdigest()
    seed = int(hexdigest, 16)
    return seed


def get_cohort(identifier: Any, experiment: Any, cohorts:
               List[str] = DEFAULT_COHORTS):
    """
    Randomly assign a value from the `cohort` list to the given experiment and
    identifier.

    Calling this function with the same identifier, experiment, and list of
    cohorts will return the same selection from the cohort list every time.
    """

    seed = get_seed(identifier, experiment)
    formatted_cohorts = _format_cohorts(cohorts)
    random = Random()
    random.seed(seed)
    index = int(random.random() * len(formatted_cohorts))
    return formatted_cohorts[index]
