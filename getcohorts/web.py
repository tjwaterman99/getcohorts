from typing import Union, Optional, List

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from getcohorts.core import (
    get_seed as _get_seed,
    get_cohort as _get_cohort,
    DEFAULT_COHORTS
)


app = FastAPI(redoc_url=None, docs_url=None)
v1 = FastAPI(redoc_url='/')


class SeedParams(BaseModel):
    identifier: Union[int, str, float]
    experiment: Union[int, str, float]


class Seed(BaseModel):
    params: SeedParams
    seed: int


class CohortParams(BaseModel):
    identifier: Union[int, str, float]
    experiment: Union[int, str, float]
    cohorts: Optional[List[str]] = DEFAULT_COHORTS


class Cohort(BaseModel):
    params: CohortParams
    cohort: str


@v1.get("/health")
def get_health():
    return {"healthy": True}


@v1.get('/seeds', response_model=Seed)
def get_seed(data: SeedParams):
    seed = _get_seed(**data.dict())
    return Seed(seed=seed, params=data)


@v1.get('/cohorts', response_model=Cohort)
def get_cohort(data: CohortParams):
    cohort = _get_cohort(**data.dict())
    return Cohort(cohort=cohort, params=data)


@app.get('/')
def get_index():
    return RedirectResponse('/v1/')


app.mount('/v1', v1)
