import os
import sys
PROJ_ROOT_DIR :str= os.path.abspath(os.path.dirname(__file__))
for _ in range(1):
    PROJ_ROOT_DIR = os.path.dirname(PROJ_ROOT_DIR)

print(PROJ_ROOT_DIR)
sys.path.append(PROJ_ROOT_DIR)

from hmall.cllct_product.CllctOfHmall import CllctOfHmall

'''
@author JunHyeon.Kim
'''
def main():
    '''
    '''
    cllct_of_hmall = CllctOfHmall()
    cllct_of_hmall.get_product_rank()
        
if __name__ == "__main__":
    main()