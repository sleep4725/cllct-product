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
    def is_index_exists(cls, es_client: Elasticsearch, index: str)-> bool:
        '''
        :param es_client:
        :param index:
        '''
        is_index_exists :bool= es_client.indices.exists(index=index)
        print(f"{is_index_exists}")
        if is_index_exists: return True
        else: return False
        
    @classmethod 
    def add_index_from_alias(cls, es_client: Elasticsearch, alias: str, index: str):
        '''
        :param:
        :param:
        :param:
        :return:
        '''
        body = {
            "actions": [
                {
                    "add": {
                        "index": index,
                        "alias": alias
                    }
                }
            ]
        }
        try:
                
            es_client.indices.update_aliases(body=body)
        except:
            print(f"alias index[{index}] add fail~!!")
        else:
            print(f"alias index[{index}] add success~!!")
                 
    @classmethod
    def delete_index_from_alias(cls, es_client: Elasticsearch, alias: str, index_list: list[str]):
        '''
        :param:
        :param:
        :param:
        :return:
        '''
        for idx in index_list:
            body = {
                "actions": [
                    {
                        "remove": {
                            "index": idx,
                            "alias": alias
                        }
                    }
                ]
            }
            try:
                
                es_client.indices.update_aliases(body=body)
            except:
                print("")
            else:
                print(f"alias index[{idx}] remove success")
                
    @classmethod 
    def exchange_index_of_alias(cls, es_client: Elasticsearch, alias: str, index: str):
        '''
        :param es_client:
        :param alias:
        :param index:
        '''
        # alias 가 ES 에 있는지 확인
        ## 만약 없다면 index 를 그대로 add
        ## 만약 있다면
        ### 기존 index 를 제거 후 새로운 index 를 추가
        if EsService.is_index_exists(es_client=es_client, index=alias):
            indices = [idx for idx in es_client.indices.get_alias(alias).keys()][0]
            if indices != index:
                EsService.delete_index_from_alias(es_client=es_client, alias=alias, index_list=indices)
        else:
            EsService.add_index_from_alias(es_client=es_client, alias=alias, index=index)
    
    @classmethod
    def get_index_name(cls)-> str:
        '''
        :param:
        :return: Elasticsearch-index
        '''  
        return EsService.es_config["es"]["index"] + "_" + TimeUtil.get_index_name_time()

    @classmethod
    def do_bulk_insert(cls, es_client: Elasticsearch, action: list[dict])->bool:
        '''
        :param es_client:
        :param action:
        :return:
        '''
        try:
                
            bulk(client= es_client, actions= action)
        except:
            print("bulk insert fail~!!")
            return False
        else:
            print("bulk insert success~!!")
            return True
        finally:
            action.clear() 
