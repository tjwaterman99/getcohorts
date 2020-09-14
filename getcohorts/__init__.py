import pkg_resources

from getcohorts.core import get_cohort, get_seed, DEFAULT_COHORTS  # noqa

__version__ = pkg_resources.get_distribution('getcohorts').version
