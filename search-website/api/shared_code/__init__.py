import os

def azure_config():
    
    configs={}
    configs["search_facets"]= "authors*,language_code"
    configs["search_index_name"]=os.environ.get("SearchIndexName", "hotels-sample-index")
    configs["search_service_name"]=os.environ.get("SearchServiceName", "mix")
    configs["search_api_key"]=os.environ.get("SearchApiKey", "ABF7920FCE83D3B4CA63947C7FDCE13F")
    
    return configs
