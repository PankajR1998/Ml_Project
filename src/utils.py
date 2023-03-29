import numpy as np
import pandas as pd
import dill
import os
import sys

from src.exception import CustomException
from sklearn.metrics import r2_score

def saved_object(file_path,object):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(object,file_obj)
    
    except Exception as e:
        CustomException(e,sys)
def evaluate_models(X_train,y_train,X_test,y_test, models):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(X_train,y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_r2_score = r2_score(y_train,y_train_pred)
            test_r2_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_r2_score

        return report
    except Exception as e:
        raise CustomException(e,sys)