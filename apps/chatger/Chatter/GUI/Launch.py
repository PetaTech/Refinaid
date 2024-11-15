# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
from typing import Any
from Chatter.GUI.Information import Header as heaader
from Chatter.GUI.Login import Auth as auth
from Chatter.GUI.Tab import History as history
from Chatter.GUI.Tab import Submit as submit

def build_chatter_judge(
        *args: Any, 
        **kwargs: Any,
    ) -> gr.Blocks:

    demo = gr.Blocks(
        title='Chatter Judge',
    )

    with demo:
        gr.Markdown(
            heaader.ee_judge_header
        )

        submit_tab = submit.init_submit_tab()
        history_tab = history.init_history_tab()

        with gr.Tab("Race Bar"):
            gr.Markdown(
                heaader.race_bar_page_header
            )

        with gr.Tab("Judge Mechanism"):
            gr.Markdown(
                heaader.judge_mechanism_page_header
            )

        with gr.Tab("Judge Developers"):
            gr.Markdown(
                heaader.judger_developer_page_header
            )

    # demo.auth=auth.auth_admin             # temporary disable auth
    # demo.auth_message = 'Welcome to Chatter Judge!!!'

    return demo
