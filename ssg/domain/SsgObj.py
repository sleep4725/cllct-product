from dataclasses import dataclass

'''
@author JunHyeon.Kim
@date 20230326
'''
@dataclass
class SsgObj:
    
    flag: str
    keyword: str
    ranking: int
    current_time: str
    cllct_time: str 