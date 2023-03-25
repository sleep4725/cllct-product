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
    def full_es_bulk_insert(self)-> None:
        '''
        전체 색인
        '''
    
    @abstractmethod
    def increase_es_bulk_insert(self)-> None:
        '''
        증분 색인
        '''