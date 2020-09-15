from typing import Union, Optional, List

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from getcohorts.core import (
    get_seed as _get_seed,
    get_cohort as _get_cohort,
    DEFAULT_COHORTS
)
from getcohorts import __version__

docs_data = {
    'version': __version__,
    'title': "GetCohorts",
    'description': "Utilities for allocating users to cohorts of an A/B test."
}

app = FastAPI(redoc_url=None, docs_url=None)
v1 = FastAPI(redoc_url='/', **docs_data)


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


@app.middleware('http')
async def add_version(request: Request, call_next):
    resp = await call_next(request)
    resp.headers['X-API-Version'] = __version__
    return resp


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
