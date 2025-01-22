import time
import random
import gradio as gr
from app.config.settings.base import ROOT_DIR

homework_sessions = [
    "HW01",
    "HW02",
]

question_sessions = [
    "Q1",
    "Q2",
]

question_one_description = """\
### Q1
> 將價錢 ( 105、130 ) 用字串 slice 方式取出，並相加後，並賦值給變數 cost

```python
def hw1_0():
    string1 = "小明花105元買了蘋果"
    string2 = "小華花130元買了香蕉"
    #-------------------------------
    # 注意cost為字串(string)的型別
    # cost = # ...
    #-------------------------------
    return "小明和小華共花了" + cost + "元買水果"
```
"""

question_two_description = """\
### Q2
> 透過字串可使用的函式或方法，使用變數 str1 組合出 "ABCCCCdIIkGHH"，並賦值給 output

```python
def hw1_1():
    str1 = "abcdefghijk"
    output = ""
    #-------------------------------
    # output = # ...
    #-------------------------------
    return output
```
"""

homework_one_content_sessions = [
    question_one_description,
    question_two_description,
]


def chatger() -> gr.Blocks:
    with gr.Blocks(title="Chatger", theme=gr.themes.Default()) as demo:
        gr.HTML("<h1 align=center>✏️ Chatger</h1>")

        with gr.Tab("Submit Your Code"):
            gr.HTML("<h1 align=center>🔥 Show Your Endeavor 🔥</h1>")

            with gr.Row():
                with gr.Column("Question"):
                    with gr.Row():
                        gr.Dropdown(
                            label="⛳️ Select Homework",
                            value=homework_sessions[0],
                            choices=homework_sessions,
                            interactive=True,
                        )
                        gr.Dropdown(
                            label="📸 Select Question",
                            value=question_sessions[0],
                            choices=question_sessions,
                            interactive=True,
                        )
                with gr.Column("Chat Bot"):
                    chatbot = gr.Chatbot(type="messages")
                    msg = gr.Textbox()
                    clear = gr.Button("Clear")

        with gr.Tab("Race Bar"):
            gr.Markdown("Race Bar")

        with gr.Tab("Judge Mechanism"):
            gr.Markdown("Judge Mechanism")

        with gr.Tab("Judge Developers"):
            gr.Markdown("Judge Developers")

        def user(user_message, history: list):
            return "", history + [{"role": "user", "content": user_message}]

        def bot(history: list):
            bot_message = random.choice(
                ["How are you?", "I love you", "I'm very hungry"]
            )
            history.append({"role": "assistant", "content": ""})
            for character in bot_message:
                history[-1]["content"] += character
                time.sleep(0.05)
                yield history

        msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
            bot, chatbot, chatbot
        )
        clear.click(lambda: None, None, chatbot, queue=False)

    demo.favicon_path = ROOT_DIR / "static" / "favicon.ico"
    return demo
