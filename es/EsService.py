import os
import sys
import yaml
PROJ_ROOT_DIR :str= os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(PROJ_ROOT_DIR)

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from es.EsArgument import EsArgument
from util.TimeUtil import TimeUtil
'''
@author JunHyeon.Kim
@date 20230325
'''
class EsService:
    
    es_config = EsArgument.get_config()
    
    @classmethod
    def get_index_name(cls)-> str:
        '''
        :param:
        :return: Elasticsearch-index
        '''  
        return EsService.es_config["es"]["index"] + "_" + TimeUtil.get_index_name_time()

    @classmethod
    def do_bulk_insert(cls, es_client: Elasticsearch, action: list[dict]):
        '''
        :param es_client:
        :param action:
        :return:
        '''
        try:
                
            bulk(client= es_client, actions= action)
        except:
            print("bulk insert fail~!!")
        else:
            print("bulk insert success~!!")
        finally:
            action.clear() 
