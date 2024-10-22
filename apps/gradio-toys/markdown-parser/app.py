import gradio as gr
from utils import get_how_to_material, get_text, render_preview


def build_markdown_parser_app():
    with gr.Blocks(
        title='Refinaid Markdown Parser',
    ) as demo:
        
        gr.HTML(
            "<h1 align=center>Refinaid Markdown Parser</h1>"
        )
        
        with gr.Row():
            input_markdown_content = gr.Textbox(
                interactive=True,
                label="📝 Input your content here (shift + enter to change line)",
                render=True,
                value=get_text(),
            )
            prev_markdown_content = gr.Markdown(
                value=get_text(),
            )

        with gr.Row():
            gr.Markdown(
                value=get_how_to_material(),
            )

        input_markdown_content.change(
            fn=render_preview,
            inputs=input_markdown_content,
            outputs=prev_markdown_content,
        )

    return demo

if __name__ == "__main__":
    build_markdown_parser_app().launch()
