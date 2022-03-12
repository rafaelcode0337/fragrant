
from fragrant_model_abstract import FragrantModelAbstract as modelabstract, fieldalias, fieldmask, fillable, rules
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
        
   
          