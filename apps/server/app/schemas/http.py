from pydantic import BaseModel


class BaseResponseSchema(BaseModel):
    """Base schema for response."""

    msg: str = "OK"


class Http400BadRequestSchema(BaseModel):
    """Base schema for 400 response."""

    detail: str = "Bad Request"


class Http401UnauthorizedSchema(BaseModel):
    """Base schema for 401 response."""

    detail: str = "Unauthorized"


class Http403ForbiddenSchema(BaseModel):
    """Base schema for 403 response."""

    detail: str = "Forbidden"


class Http404NotFoundSchema(BaseModel):
    """Base schema for 404 response."""

    detail: str = "Not Found"


class Http422UnprocessableEntitySchema(BaseModel):
    """Base schema for 422 response."""

    detail: str = "Unprocessable Entity"
