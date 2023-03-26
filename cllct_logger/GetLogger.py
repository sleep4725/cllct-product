import logging

'''
@author JunHyeon.Kim
'''
class GetLogger:
    
    @classmethod 
    def product_logger(cls, logging_file_path: str, flag: str):
        '''
        '''
        # Logger instance 생성
        logger = logging.getLogger(__name__)

        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(f"{logging_file_path}/{flag}.log")
        
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)
        logger.setLevel(level=logging.DEBUG)
        
        return logger