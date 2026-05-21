from models.aluno import *

class Turma:
    def __init__(self,letra,nivel_ensino,serie,ano,id=None):
        self.id = id
        self.letra = letra 
        self.nivel_ensino = nivel_ensino
        self.serie = serie
        self.ano = ano
        
    
    
