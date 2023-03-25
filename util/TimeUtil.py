import time

'''
@author JunHyeon.Kim
@date 20230325
'''
class TimeUtil:
    
    @classmethod
    def get_mmddHH(cls):
        '''
        :return (ex: 032511):
        '''
        return time.strftime("%m%d%H", time.localtime())
    
    @classmethod
    def get_cllct_time(cls):
        '''
        :return (ex: 2023-03-25 14:51:22)
        '''
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    @classmethod
    def get_index_name_time(cls):
        '''
        '''
        return time.strftime("%Y%m%d", time.localtime()) 