from src.ML_Project.logger import logging
from src.ML_Project.exception import CustomException
import sys


if __name__ == '__main__':
    logging.info("Execution Started")
    
    try:
        x = 1/0
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)