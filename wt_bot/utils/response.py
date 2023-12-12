from abc import ABC
from typing import Generic, TypeVar


from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import Field
from pydantic.generics import GenericModel
from starlette.responses import Response




from wt_bot import utils



T = TypeVar("T")


