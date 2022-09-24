# Import utils
from app.schemas.schemas import Request
from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.post("/get_data")
def get_data(request: Request) -> JSONResponse:
    """get_data endpoint

    Args:
        request (Request): request with dummy utterances

    Returns:
        dict: a dummy response
    """
    # Add your code here
    # Create some helper function in utils/
    # Use your helper functions by utils.functionname()

    return dict(request)
