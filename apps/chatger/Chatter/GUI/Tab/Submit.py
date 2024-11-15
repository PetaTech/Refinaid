# -*- coding: utf-8 -*-
'''
Create Date: 2024/01/14
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
from typing import Any
from Chatter.Judge.Judge import get_code
from Chatter.ChatBot.Chat import respond
from Chatter.Utils.Listener import submit_background_listener
from Chatter.GUI.Information import Header as heaader
from Chatter.GUI.Information import Question as question
from Chatter.GUI.Information import Header as heaader
from Chatter.Judge.Plot import make_plot
import pandas as pd

def init_submit_tab(*args, **kwargs):

    with gr.Tab("Submit Your Code") as submit_tab:
        gr.Markdown(
            heaader.submit_page_header
        )

        with gr.Row(
            # variant="compact",
        ):
            with gr.Column("Question part", variant="compact",):

                with gr.Row():
                    selected_homework_name = gr.Dropdown(
                        label="⛳️ Select Homework", 
                        value=question.homework_sessions[0],
                        choices=question.homework_sessions,
                        interactive=True,
                    )

                    selected_question_name = gr.Dropdown(
                        label="📸 Select Question", 
                        value=question.question_sessions[0],
                        choices=question.question_sessions,
                        interactive=True,
                    )

                gr.Markdown(
                    heaader.question_descriptions_header
                )

                question_description = gr.Markdown(
                    question.homework_one_content_sessions[0], 
                    visible=True,
                )

            with gr.Column(variant="default",):
                gr.ChatInterface(
                    fn=respond, 
                    # examples=["hello", "hola", "merhaba"],
                    additional_inputs=[
                        selected_homework_name,
                        selected_question_name,
                    ],
                    undo_btn=None,
                )

        with gr.Row(variant="compact",):

            with gr.Column():
                answer_code = gr.Code(
                    label="Write Your code here", 
                    language="python",
                    lines=10,
                    # info="Initial text",
                )

                with gr.Row():
                    clear_code_btn = gr.Button(
                        value="🗑️  Clear",
                        variant="secondary",
                    )
                    submit_code_btn = gr.Button(
                        value="Submit",
                        variant="primary",
                    )


            with gr.Column():
                judged_result = gr.Markdown(
                    f"### Results of your submission: "
                )

                # chatgpt_suggestion = gr.Markdown(
                #     f"### Review by ChatGPT: "
                # )
                with gr.Row() as visualized_result:
                    plot = gr.Plot(
                        value=make_plot("scatter_plot"),
                        label="Plotttttt",
                        scale=4,
                        interactive=True,
                        # show_actions_button=True,
                    )

                    plot_type_btn = gr.Radio(
                        scale=1,
                        label="Plot type",
                        choices=[
                            "AC",
                            "WA",
                            "TLE",
                            "MLE",
                            "RE",
                            "CE",
                            "ChatGPT",
                        ],
                        value="AC",
                        interactive=True,
                    )


    submit_code_btn.click(
        get_code, 
        inputs=[
            answer_code,
            selected_homework_name,
            selected_question_name,
        ], 
        outputs=[
            judged_result
        ],
    )

    submit_background_listener(
        selected_homework_name,
        selected_question_name,
        question_description
    )

    return submit_tab
