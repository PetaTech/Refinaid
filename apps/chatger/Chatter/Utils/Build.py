# -*- coding: utf-8 -*-
'''
Create Date: 2023/10/18
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.0.1
'''

import os
import gradio as gr
from fastapi import FastAPI
from Chatter.GUI.Launch import build_chatter_judge

def build_and_mount_playground(
        app: FastAPI, 
        playground_name: gr.Blocks, 
        favicon_file: str, 
        path: str,
    ) -> FastAPI:

    if playground_name == "judge":
        playground = build_chatter_judge()
    else:
        raise ValueError("Invalid playground name")
    
    favicon_path = "." + os.sep + "static" + os.sep + favicon_file
    playground.favicon_path = favicon_path


    app = gr.mount_gradio_app(
        app, 
        playground, 
        path=path
    )

    return app
