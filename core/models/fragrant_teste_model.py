
from fragrant_model_abstract import Afterpost, BeforeEdit, Beforepost, FragrantModelAbstract as modelabstract, fieldalias, fieldmask, fillable, rules
from fragrant_model_rules import RulesEnum as Rules

class Cliente(modelabstract):
  def __init__(self): 
      
     fillable([                        
            'nome',
            'razao',
            'cnpj'            
        ])
    
     fieldalias({
         'nome':'Nome do Cliente ',
         'razao':'Razão Social do Cliente',
         'cnpj':'Doc CNPJ'
        
     }) 
     
     fieldmask({
        'cnpj':'##.###.###/###-##' 
     }) 
     
     rules({
         'cnpj',Rules.notnull,
         'nome',Rules.uniquekey
     }) 
     
     # Eventos - Programação Orientada a Eventos 
     # Programação orientada a eventos é um paradigma de programação. Diferente de programas tradicionais 
     # que seguem um fluxo de controle padronizado, o controle de fluxo de programas orientados a evento 
     # são guiados por indicações externas, chamadas eventos
     
     # Eventos que serão Assinados por classes como Controllers ou Provedores de serviços para 
     # Manipulação dos eventos Single-Thread do Modelo , nao é um Padrão Observable, são eventos de 
     # Insântia única que respondem a um comportamento específico 
     # After Post é executado antes de acionar a Transação Post do DAO com o Banco de dados , 
     # Você pode definir ações para sua aplicação.
     Afterpost()
     
     Beforepost()
     
     BeforeEdit()
        
   
          