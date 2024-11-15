# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import subprocess

def get_code(txt, selected_homework_name,
        selected_question_name, *args, **kwargs):
    with open("tmp.py", "w") as file:
        file.write(txt)

    try:
        output = subprocess.check_output(
            ["python", "tmp.py"], 
            stderr=subprocess.STDOUT, 
            universal_newlines=True,
        )
        print("Script output:")
        print(output)

        result = judge_question_1(output)
        return result
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)
        return e.output
    finally:
        os.remove("tmp.py")

def judge_question_1(output):
    if output == "Hello World\n":
        return "### Your code results: AC"
    elif output == "Hello World":
        return "### Your code results: AC"
    else:
        return "### Your code results: WA"
