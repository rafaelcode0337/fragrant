
from abc import ABC
import string
from typing import List
import sqlalchemy

from core.models.fragrant_model_rules import RulesEnum


class FragrantModelAbstract(ABC):
    pass

def fillable( list = []  ):
   """Lista dos Fields da tabela que serão tratados pela aplicação
   para serialização e desserialização, tratamentos de regras e 
   usados para a montagem do SQl term.
   Representam as propriedades das entidades do banco de dados
    """
   return list;


def fieldalias(list = {string,string}):
     """Adicione apelidos para os Fields do modelo de dados
     segundo o Fillable, um dicionário de dados do tipo key: string, value: string
     ex: 'name':'Nome do Cliente'
     pode ser usado para enviar no pacote de Resposta.
    """
     return list;

def fieldmask(list = {string,string}):
    """Adicione Mascaras para exibição seguindo os Fillables , as mascaras 
      ajudam no tratamento de dados como formatação do CNPJ, CEP, etc..
    """
    return list;

def rules(Dict = {string,RulesEnum}):
    """Adicione Regras para os campos do modelo segundo o Fillable, as Regras serão validadas 
    por uma camada Validate para previnir desastres ao executar transações
    e você pode definir regras para serem enviadas para o Client-Side
    """
    return 

