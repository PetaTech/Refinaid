# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/27
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.1.4
'''

import os

import gradio as gr

from app.playground.classifier.launch import build_classifier_playground
from app.playground.plum.gui.launch import build_plum_playground


def build_and_mount_playground(
        app, playground_name, favicon_file, path):

    if playground_name == "classifier":
        playground = build_classifier_playground()
    elif playground_name == "plum":
        from app.playground.plum.model.train import train
        confusion, accuracy, recall, precision, proba = train()
        playground = build_plum_playground(confusion, accuracy, recall, precision, proba)
    else:
        raise ValueError("Invalid playground name")
    
    favicon_path = "." + os.sep + "static" + os.sep + favicon_file
    playground.favicon_path = favicon_path
    app = gr.mount_gradio_app(app, playground, path=path)

    return app
