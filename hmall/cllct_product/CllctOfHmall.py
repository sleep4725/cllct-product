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
'''
Hmall
@author JunHyeon.Kim
@date 20230324
'''
class CllctOfHmall(Template, EsService):
    
    FLAG = "hmall"
    def __init__(self, deploy: str) -> None:
        self._es_client :Elasticsearch= EsClient.get_es_client(deploy= deploy)
        EsService.__init__(self)
        self._action_list :list[dict]= []
        self._config :dict= CllctOfHmall.get_config()
        self._cllct_current_time :str= TimeUtil.get_cllct_time()
        self._cllct_time :str= TimeUtil.get_mmddHH()
        self._es_index :str= EsService.get_index_name()
    
    def increase_es_bulk_insert(self) -> None:
        ''''''
    
    def full_es_bulk_insert(self) -> None:
        '''
        :param:
        :return:
        '''
        if self._action_list:
            is_check :bool= self.do_bulk_insert(es_client=self._es_client, action= self._action_list)
            if is_check:
                EsService.exchange_index_of_alias(
                    es_client= self._es_client,
                    alias=EsService.es_config["es"]["alias"],
                    index=self._es_index
                )
            else:
                print("alias index exchange fail~!!")
        else:
            print("적재할 데이터가 없습니다.")
        
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
        req_url :str= self._config["requrl"] + self._cllct_time
        response = requests.get(req_url)
        if self.check_status_code(status_code=response.status_code):
            response_data = str(response.text)\
                .lstrip("var popKeyWordListJson = $.parseJSON('")\
                .rstrip("');\r\n")
            response_dict = json.loads(response_data)
            
            for element in response_dict:
                document :dict= asdict(HmallObj(
                        flag= CllctOfHmall.FLAG, 
                        keyword= element["keyword"], 
                        ranking=element["ranking"], 
                        current_time= self._cllct_current_time,
                        cllct_time= self._cllct_time
                )) 
                self._action_list.append({
                    "_index": self._es_index,
                    "_id": f'{document["flag"]}_{document["ranking"]}_{document["keyword"]}_{document["cllct_time"]}',
                    "_source": document
                })
                
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