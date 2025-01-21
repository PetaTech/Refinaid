import gradio as gr
from app.config.settings.base import ROOT_DIR


def chatger() -> gr.Blocks:

    with gr.Blocks(title="Chatger") as demo:

        gr.HTML("<h1 align=center>✏️ Chatger</h1>")

    demo.favicon_path = ROOT_DIR / "static" / "favicon.ico"
    return demo
