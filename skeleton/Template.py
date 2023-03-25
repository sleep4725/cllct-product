from abc import *

'''
'''
class Template(metaclass=ABCMeta):
    
    @abstractmethod
    def check_status_code(self)-> bool:
        '''
        :return bool:
        '''
        
    @abstractmethod
    def get_product_rank(self)-> None:
        '''
        '''
    
    @abstractmethod
    def es_bulk_insert(self)-> None:
        '''
        '''