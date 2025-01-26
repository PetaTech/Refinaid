from fastapi import APIRouter, status, Path, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import Annotated

from app.config.settings.base import ROOT_DIR
from app.schemas import http as http_schemas

dataset_routes = APIRouter(tags=["dataset"], prefix="/dataset")

static_dir = ROOT_DIR / "static"
dataset_routes.mount(
    "/static",
    StaticFiles(directory=static_dir),
    name="static",
)


@dataset_routes.get(
    "/health",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"model": http_schemas.BaseResponseSchema},
        400: {"model": http_schemas.Http400BadRequestSchema},
        401: {"model": http_schemas.Http401UnauthorizedSchema},
        403: {"model": http_schemas.Http403ForbiddenSchema},
        404: {"model": http_schemas.Http404NotFoundSchema},
    },
    response_model=http_schemas.BaseResponseSchema,
    description="Health check endpoint.",
)
async def health_check():
    return {"status": "ok"}


@dataset_routes.get(
    "/{dataset_name}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"model": http_schemas.BaseResponseSchema},
        400: {"model": http_schemas.Http400BadRequestSchema},
        401: {"model": http_schemas.Http401UnauthorizedSchema},
        403: {"model": http_schemas.Http403ForbiddenSchema},
        404: {"model": http_schemas.Http404NotFoundSchema},
    },
    response_model=http_schemas.BaseResponseSchema,
)
async def get_dataset(
    dataset_name: Annotated[
        str,
        Path(description="The name of the dataset file to fetch"),
    ],
):
    # TODO: Add logic to detect different dataset schema and return the appropriate response
    file_path = static_dir / "data" / f"{dataset_name}" / f"{dataset_name}.csv"

    if not file_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dataset file '{dataset_name}.csv' not found.",
        )
    return {"status": "Success"}
