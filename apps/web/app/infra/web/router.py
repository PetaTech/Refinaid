import gradio as gr
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.config.settings.base import ROOT_DIR


from app.adapters.controllers.mock import mock_routes
from app.views.simple_ai import simple_ai
from app.views.chatger import chatger


def setup_routers(app: FastAPI) -> None:
    """
    Setup routers for the application

    Args:
        - app (FastAPI): FastAPI instance

    Returns:
        - None
    """
    gr.mount_gradio_app(app, simple_ai(), path="/simple-ai")
    gr.mount_gradio_app(app, chatger(), path="/chatger")
    app.include_router(mock_routes)

    # Mount the static files directory
    static_dir = ROOT_DIR / "static"
    app.mount(
        "/static",
        StaticFiles(directory=static_dir),
        name="static",
    )

    # Add a route for the favicon
    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon() -> FileResponse:
        favicon_path = static_dir / "favicon.ico"
        return FileResponse(favicon_path)
