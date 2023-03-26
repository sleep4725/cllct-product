import os
import yaml
PROJ_ROOT_DIR :str= os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
from elasticsearch import Elasticsearch, exceptions

##
# @author JunHyeon.Kim
# @date 20230325
## --------------------
class EsClient:
    
    @classmethod
    def get_es_client(cls, deploy: str)-> Elasticsearch:
        '''
        :param deploy:
        :return Elasticsearch
        '''
        global PROJ_ROOT_DIR
        es_conn_config_dir :str= os.path.join(PROJ_ROOT_DIR, "config/es-conn-config.yaml")
        
        is_file_exists :bool= os.path.exists(es_conn_config_dir)
        if is_file_exists:
            with open(es_conn_config_dir, "r", encoding="utf-8") as es_conn_file:
                es_conn :dict= yaml.safe_load(es_conn_file)
                es_conn_file.close()
                es_deploy :dict= es_conn[deploy]
                
                _port :int= es_deploy["port"]
                _schema :str= es_deploy["schema"]
                
                es_client = Elasticsearch(
                    [f"{_schema}://{host}:{_port}" for host in es_deploy["hosts"]]
                )
                
                try:
                    
                    response :dict= es_client.cluster.health()
                except exceptions.ConnectionError as err:
                    print(err)
                    exit(1)
                else:
                    if response['status'] in ["yellow", "green"]: 
                        return es_client
        else:
            raise FileNotFoundError