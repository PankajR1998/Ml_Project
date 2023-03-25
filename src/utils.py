import numpy as np
import pandas as pd
import dill
import os
import sys

from src.exception import CustomException

def saved_object(file_path,object):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(object,file_obj)
    
    except Exception as e:
        CustomException(e,sys)