import os
import sys
import yaml
PROJ_ROOT_DIR :str= os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(PROJ_ROOT_DIR)

class EsArgument:
            
    @classmethod 
    def get_config(cls)-> dict:
        '''
        '''
        global PROJ_ROOT_DIR
        es_service_config_file :str= os.path.join(PROJ_ROOT_DIR, "config/es-service-config.yaml")
        is_file_exists :bool= os.path.exists(es_service_config_file)
        if is_file_exists:
            with open(es_service_config_file, "r", encoding="utf-8") as es_service_config_read:
                es_service_data = yaml.safe_load(es_service_config_read)
                es_service_config_read.close()
                return es_service_data
        else:
            raise FileNotFoundError
