from abc import ABC

class FragrantControllerAbstract(ABC):
    
    """Use o método para prover uma rota index inicial do controller"""
    def index():
        pass  
    
    """Use o método para prover uma rota index inicial do controller"""
    def route():
        pass
    
    """Use o método para prover uma rota index inicial do controller"""
    def view():
        pass        
    
    """Use o método para prover uma rota de criação para o controller"""
    def create():
        pass
    
    """Use o método para prover uma rota de gravação no Banco de dados do controller"""
    def store():
        pass
    
    """Use o método para prover uma rota de gravação no Banco de dados do controller"""
    def show():
        pass
    
    """Use o método para prover uma rota de edição dos dados do controller"""
    def edit():
        pass
    
    """Use o método para prover uma rota para deletar/destroir dados do banco de dados no controller"""
    def destroy():
        pass
    
    """Use o método para prover uma rota Update de dados no banco de dados no controller"""
    def update():
        pass
    
    