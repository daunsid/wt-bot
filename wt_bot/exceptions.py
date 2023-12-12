import logging
import traceback
from typing import Any

from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError


from wt_bot import utils
from wt_bot.core.config import settings


logger = logging.getLogger(__name__)


class InternalServiceError(HTTPException):

    """Error class for failed internal services"""

    
