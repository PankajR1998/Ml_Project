import sys
import logging
import src.logger
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_n = exc_tb.tb_lineno
    error = str(error)
    error_message = f"error occured in python script name [{file_name}] line number [{line_n}] error message [{error}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

