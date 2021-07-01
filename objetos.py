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
        
        self.nota = None

class Turma:
    def __init__(self, _nome_turma, _materia, _professor, _alunos, _notas_alunos):
        self._nome_turma = _nome_turma
        self._materia = _materia
        self._professor = _professor
        self._alunos = _alunos
        self._notas_alunos = _notas_alunos

        self.tamanho_turma = len(_alunos)

