import os
import sys
PROJ_ROOT_DIR :str= os.path.abspath(os.path.dirname(__file__))
for _ in range(2):
    PROJ_ROOT_DIR = os.path.dirname(PROJ_ROOT_DIR)
    
sys.path.append(PROJ_ROOT_DIR)

import yaml
import json
import requests
from dataclasses import asdict
from elasticsearch import Elasticsearch

from skeleton.Template import Template
from util.TimeUtil import TimeUtil
from es.EsService import EsService
from es.EsClient import EsClient
from hmall.domain.HmallObj import HmallObj

class CllctOfSSG(Template, EsService):
    
    FLAG = "ssg"
    def __init__(self, deploy: str) -> None:
        self._es_client :Elasticsearch= EsClient.get_es_client(deploy= deploy)
        EsService.__init__(self)
        self._action_list :list[dict]= []
        self._config :dict= CllctOfSSG.get_config()
        self._cllct_current_time :str= TimeUtil.get_cllct_time()
        self._cllct_time :str= TimeUtil.get_mmddHH()
        self._es_index :str= EsService.get_index_name()
    
    def increase_es_bulk_insert(self) -> None:
        '''
        '''
    
    def full_es_bulk_insert(self) -> None:
        '''
        '''
    
    def check_status_code(self, status_code: int) -> bool:
        '''
        '''
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
        req_url :str= self._config["requrl"]
        response = requests.get(req_url)
        if self.check_status_code(status_code=response.status_code):
            print("good")
            
    @classmethod
    def get_config(cls)-> dict:
        '''
        :param:
        :return:
        '''
        global PROJ_ROOT_DIR
        config_file_path :str= os.path.join(PROJ_ROOT_DIR, f"config/{CllctOfSSG.FLAG}-config.yaml")
        is_file_exists :bool= os.path.exists(config_file_path)
        
        if is_file_exists:
            with open(config_file_path, "r", encoding="utf-8") as config_file_read:
                config_file :dict= yaml.safe_load(config_file_read)
                config_file_read.close()
                return config_file
        else:
            raise FileNotFoundError 