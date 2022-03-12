import importlib

def get_module(module_name: str):
    return importlib.import_module(module_name)

AbstractHttp = get_module('core.http.fragrant_http_abstract').FragrantHttpAbstract
