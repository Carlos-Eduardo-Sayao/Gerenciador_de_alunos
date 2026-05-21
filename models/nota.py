class Nota:
    def __init__(self,aluno_id,materia,unidade,pontuacao,id=None):
        self.id = id
        self.aluno_id = aluno_id
        self.materia = materia
        self.unidade = unidade
        self.pontuacao = pontuacao