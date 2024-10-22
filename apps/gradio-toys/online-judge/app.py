import gradio as gr

def build_online_judge_app():
    with gr.Blocks(title="Refinaid - Online Judge") as app:

        gr.HTML(
            "<h1 align=center>Refinaid - Online Judge</h1>"
        )

    return app

def main():
    build_online_judge_app().launch()

if __name__ == "__main__":
    main()
