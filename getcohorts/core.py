from random import Random
import hashlib


DEFAULT_COHORTS = ['experimental', 'control']


def get_cohort(identifier: bytes, experiment: bytes, cohorts=DEFAULT_COHORTS):
    hexdigest = hashlib.md5(identifier + experiment).hexdigest()
    _id = int(hexdigest, 16)
    random = Random()
    random.seed(_id)
    index = int(random.random() * len(cohorts))
    return cohorts[index]
