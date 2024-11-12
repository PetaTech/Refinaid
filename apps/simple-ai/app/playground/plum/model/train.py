# -*- coding: utf-8 -*-
'''
Create Date: 2023/08/26
Author: @1chooo(Hugo ChunHo Lin)
Version: v0.0.6
'''

from pathlib import Path
from os.path import join
from os.path import dirname
from os.path import abspath
from app.playground.plum.data.data import data_preprocessing
from app.playground.plum.model.model import train_logistic_regression
from app.playground.plum.model.model import evaluate_model
from app.playground.plum.utils.tools import load_data
from app.playground.plum.utils.tools import save_model
from app.playground.plum.utils.tools import get_trained_result

def train():
    df = data_preprocessing(load_data())

    lr, X_test, y_test, predictions = train_logistic_regression(df)
    accuracy, recall, precision, confusion = evaluate_model(y_test, predictions)

    get_trained_result(accuracy, recall, precision, confusion)

    proba = lr.predict_proba(X_test)[:, 1]

    output_model_path = join(
        dirname(abspath(__file__)),
        '..',
        '..',
        '..',
        'model', 
        'plum_prediction.pkl'
    )

    save_model(lr, output_model_path, 3)

    return confusion, accuracy, recall, precision, proba
