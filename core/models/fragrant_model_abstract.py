
from abc import ABC
import string
from typing import List
import sqlalchemy
import threading
import time

from core.models.fragrant_model_rules import RulesEnum


class FragrantModelAbstract(ABC):
    pass

def __InternalEvents__(target=None):
 event_obj = threading.Event()
 th = threading.Thread(target, args=(event_obj))
 th.start()
 time.sleep(0.1)
 event_obj.set()

def Beforepost(target=None):
 """Evento que será disparado apos ocorrer uma Transação Post no banco de dados
    passe no argumento target um método que será executado
"""
 __InternalEvents__()
 
def Afterpost(target=None):
 """Evento que será disparado Antes ocorrer uma Transação Post no banco de dados
    passe no argumento target um método que será executado
"""
__InternalEvents__()

 
def BeforeEdit(target=None):
 """Evento que será disparado Depois que  ocorrer uma Transação Edit/Update no banco de dados
    passe no argumento target um método que será executado
"""
 __InternalEvents__()

def fillable( list = []  ):
   """Lista dos Fields da tabela que serão tratados pela aplicação
   para serialização e desserialização, tratamentos de regras e 
   usados para a montagem do SQl term.
   Representam as propriedades das entidades do banco de dados
    """
   return list


def fieldalias(list = {string,string}):
     """Adicione apelidos para os Fields do modelo de dados
     segundo o Fillable, um dicionário de dados do tipo key: string, value: string
     ex: 'name':'Nome do Cliente'
     pode ser usado para enviar no pacote de Resposta.
    """
     return list

def fieldmask(list = {string,string}):
    """Adicione Mascaras para exibição seguindo os Fillables , as mascaras 
      ajudam no tratamento de dados como formatação do CNPJ, CEP, etc..
    """
    return list

def rules(Dict = {string,RulesEnum}):
    """Adicione Regras para os campos do modelo segundo o Fillable, as Regras serão validadas 
    por uma camada Validate para previnir desastres ao executar transações
    e você pode definir regras para serem enviadas para o Client-Side
    Não de preocupe é apenas um Dicionário de dados do Tipo Key: String e value: RulesEnum
    RulesEnum é um Enumerado com as propriedades naturais características de banco de dados
    por ex: notnull diz que esse Field não poderá ser null,
           uniquekey diz que esse Field está configurado no banco de dados para ser uma chave única na tabela, ou seja 
           só pode existir na mesma tabela 1 registro com esse valor.
    Aqui está um exmplo de como funciona
    
     rules({
         'cnpj',Rules.notnull,
         'nome',Rules.uniquekey
     }) 
     
    """
    return Dict

