#Criando os objetos
class Materia:
    def __init__(self, _nome_materia):    
        self._nome_materia = _nome_materia

class Professor:
    def __init__(self, _primeiro_nome, _sobrenome, _cpf):
        self._primeiro_nome = _primeiro_nome
        self._sobrenome = _sobrenome
        self._cpf = _cpf

class Aluno:
    def __init__(self, _primeiro_nome, _sobrenome, _cpf):
        self._primeiro_nome = _primeiro_nome
        self._sobrenome = _sobrenome
        self._cpf = _cpf