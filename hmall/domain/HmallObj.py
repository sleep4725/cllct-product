from dataclasses import dataclass

'''
@author JunHyeon.Kim
@date 20230325
'''
@dataclass
class HmallObj:
    
    flag: str
    keyword: str
    ranking: int
    current_time: str
    cllct_time: str 