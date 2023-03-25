from elasticsearch import Elasticsearch

'''
'''
class EsService:

    def __init__(self) -> None:
        self._es_index :str= ""