import os
import sys
PROJ_ROOT_DIR :str= os.path.abspath(os.path.dirname(__file__))
for _ in range(2):
    PROJ_ROOT_DIR = os.path.dirname(PROJ_ROOT_DIR)
    
sys.path.append(PROJ_ROOT_DIR)

import yaml
import json
import requests
from skeleton.Template import Template
from util.TimeUtil import TimeUtil
from es.EsService import EsService
'''
Hmall
@author JunHyeon.Kim
@date 20230324
'''
class CllctOfHmall(Template, EsService):
    
    FLAG = "hmall"
    def __init__(self) -> None:
        EsService.__init__(self)
        self._config = CllctOfHmall.get_config()
        self._cllct_current_time = TimeUtil.get_cllct_time()
         
    def check_status_code(self, status_code: int) -> bool:
        '''
        :param status_code:
        '''
        if status_code == 200: return True
        else: return False
        
    def get_product_rank(self):
        '''
        :param:
        :return:
        '''
        req_url :str= self._config["requrl"] + TimeUtil.get_mmddHH()
        response = requests.get(req_url)
        if self.check_status_code(status_code=response.status_code):
            response_data = str(response.text)\
                .lstrip("var popKeyWordListJson = $.parseJSON('")\
                .rstrip("');\r\n")
            response_dict = json.loads(response_data)
            
            for element in response_dict:
                keyword :str= element["keyword"]
                ranking :int= element["ranking"]
                print(f"keyword : {keyword} | ranking : {ranking}")
        
        response.close()
        
    @classmethod
    def get_config(cls)-> dict:
        '''
        :param:
        :return:
        '''
        global PROJ_ROOT_DIR
        config_file_path :str= os.path.join(PROJ_ROOT_DIR, f"config/{CllctOfHmall.FLAG}-config.yaml")
        is_file_exists :bool= os.path.exists(config_file_path)
        
        if is_file_exists:
            with open(config_file_path, "r", encoding="utf-8") as config_file_read:
                config_file :dict= yaml.safe_load(config_file_read)
                config_file_read.close()
                return config_file
        else:
            raise FileNotFoundError