import os 
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import saved_object,evaluate_models

@dataclass
class ModelTrainerConfig:
    train_modal_file_path = os.path.join('artifect','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            
            X_train,X_test,y_train,y_test = (
                train_arr[:,:-1],
                test_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,-1]
            )
            logging.info('Split train and test data.')

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Linear Regressor": LinearRegression(),
                "K-Neigbors Regressor": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "catboost Regressor": CatBoostRegressor(),
                "AdaBoost Regressor": AdaBoostRegressor()
            }
            model_report= evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                        models=models)
            

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]
            if best_model_score < 0.6:
                CustomException("No best model found.")
            logging.info("best model found.")
            saved_object(
                file_path=self.model_trainer_config.train_modal_file_path,
                object=best_model
            )
            predicted = best_model.predict(X_test)
            r2 = r2_score(y_test,predicted)

            return r2


        except Exception as e:
            CustomException(e,sys)
