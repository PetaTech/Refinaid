import gradio as gr


def chatter_judge() -> gr.Blocks:

    with gr.Blocks(title="Chatter Judge") as demo:

        gr.HTML("<h1 align=center>🗂️ Chatter Judge</h1>")

    return demo
