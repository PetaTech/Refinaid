import gradio as gr


def simple_ai() -> gr.Blocks:

    with gr.Blocks(title="Simple AI") as demo:

        gr.HTML("<h1 align=center>🐻 Simple AI</h1>")

    return demo
