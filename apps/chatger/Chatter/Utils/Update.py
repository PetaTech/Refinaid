# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import gradio as gr
import Chatter.GUI.Information.Question as question

def get_question_description(selected_homework_name, selected_question_name):

    output_components = []

    if selected_homework_name == "HW01" and selected_question_name == "Q1":

        test_word = gr.Markdown(
            question.homework_one_content_sessions[0],  
            visible=True,
        )
    elif selected_homework_name == "HW01" and selected_question_name == "Q2":
        test_word = gr.Markdown(
            question.homework_one_content_sessions[1], 
            visible=True,
        )

    output_components.append(test_word)
    
    return test_word
