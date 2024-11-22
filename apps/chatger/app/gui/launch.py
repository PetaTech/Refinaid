# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
from app.gui.information import header
from app.gui.login import auth
from app.gui.tab import history
from app.gui.tab import submit

def build_chatter_judge() -> gr.Blocks:

    demo = gr.Blocks(
        title='Chatter Judge',
    )

    with demo:
        gr.Markdown(
            header.ee_judge_header
        )

        submit.init_submit_tab()
        history.init_history_tab()

        with gr.Tab("Race Bar"):
            gr.Markdown(
                header.race_bar_page_header
            )

        with gr.Tab("Judge Mechanism"):
            gr.Markdown(
                header.judge_mechanism_page_header
            )

        with gr.Tab("Judge Developers"):
            gr.Markdown(
                header.judger_developer_page_header
            )

    # demo.auth=auth.auth_admin             # temporary disable auth
    # demo.auth_message = 'Welcome to Chatter Judge!!!'

    return demo
