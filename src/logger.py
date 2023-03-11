import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
file_path = os.path.join(os.getcwd(),'logs',log_file)
os.makedirs(file_path,exist_ok=True)
logs_path = os.path.join(file_path,log_file)
logging.basicConfig(
    filename=logs_path,
    format='[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
