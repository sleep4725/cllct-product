import time

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
        '''
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())