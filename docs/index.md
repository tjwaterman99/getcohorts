# Introduction

GetCohorts enables random, idempotent allocations of a user to an experiment's cohort.

```python
>>> from getcohorts import get_cohort
>>> get_cohort('userid-1', 'homepage-test', cohorts=['experimental', 'control'])
'experimental'

```
