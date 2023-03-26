import os
import sys
PROJ_ROOT_DIR :str= os.path.abspath(os.path.dirname(__file__))
for _ in range(1):
    PROJ_ROOT_DIR = os.path.dirname(PROJ_ROOT_DIR)

print(PROJ_ROOT_DIR)
sys.path.append(PROJ_ROOT_DIR)

from ssg.cllct_product.CllctOfSSG import CllctOfSSG

'''
@author JunHyeon.Kim
'''
def main():
    '''
    '''
    cllct_of_ssg = CllctOfSSG(deploy="local")
    cllct_of_ssg.get_product_rank()
    cllct_of_ssg.full_es_bulk_insert() 
if __name__ == "__main__":
    main()