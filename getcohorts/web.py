from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

from getcohorts.core import get_seed, get_cohort

app = FastAPI()
v1 = FastAPI()


class CohortParams(BaseModel):
    identifier: Any
    experiment: Any


@app.get("/health")
def read_health():
    return {"healthy": True}


@v1.get('/seeds')
def read_seed(data: CohortParams):
    seed = get_seed(**data.dict())
    return {'seed': seed, 'params': data}


@v1.get('/cohorts')
def read_cohort(data: CohortParams):
    cohort = get_cohort(**data.dict())
    return {'cohort': cohort, 'params': data}


app.mount('/v1', v1)
