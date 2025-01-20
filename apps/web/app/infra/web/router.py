import gradio as gr
from fastapi import FastAPI

from app.adapters.controllers.mock import mock_routes
from app.views.simple_ai import simple_ai
from app.views.chatter_judge import chatter_judge


def setup_routers(app: FastAPI) -> None:
    """
    Setup routers for the application

    Args:
        - app (FastAPI): FastAPI instance

    Returns:
        - None
    """
    gr.mount_gradio_app(app, simple_ai(), path="/simple-ai")
    gr.mount_gradio_app(app, chatter_judge(), path="/chatter-judge")
    app.include_router(mock_routes)
