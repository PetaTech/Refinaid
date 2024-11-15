# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

from Chatter.Utils.Update import get_question_description

def submit_background_listener(
        selected_homework_name,
        selected_question_name,
        test_word,
    ):
    selected_question_name.change(
        fn=get_question_description,
        inputs=[
            selected_homework_name,
            selected_question_name,
        ],
        outputs=test_word,
    )
