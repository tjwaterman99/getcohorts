# GetCohorts

Allocate users in your experiments to a cohort using our idempotent, random function.

```python
>>> from getcohorts import get_cohort
>>> get_cohort(b'user123', b'experiment')
'experimental'

```
