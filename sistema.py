#Definindo as listas e listas de objetos
materias = []
professores = []
alunos = []

#Importando os objetos
from objetos import *

#Criando as funcionalidades
    #Do menu principal
def cadastrar_aluno():
    primeiro_nome = input("Digite o primeiro nome do aluno: ")
    sobrenome = input("Digite o sobrenome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    alunos.append(Aluno(primeiro_nome, sobrenome, cpf))
    print(f"Aluno {primeiro_nome} {sobrenome} cadastrado com sucesso.")
    menu_principal()

def cadastrar_professor():
    primeiro_nome = input("Digite o primeiro nome do professor: ")
    sobrenome = input("Digite o sobrenome do professor: ")
    cpf = input("Digite o CPF do professor: ")
    professores.append(Professor(primeiro_nome, sobrenome, cpf))
    print(f"Professor {primeiro_nome} {sobrenome} cadastrado com sucesso.")
    menu_principal()

def cadastrar_materia():
    nome_da_materia = input("Digite o nome da matéria: ")
    materias.append(Materia(nome_da_materia))
    print(f"Matéria '{nome_da_materia}' cadastrada com sucesso.")
    menu_principal()

def mostrar_todos_alunos():
    i = 0
    #Criar opção de mostrar o CPF
    for aluno in alunos:
        print(f"{alunos[i]._primeiro_nome} {alunos[i]._sobrenome}")
        i += 1
    menu_principal()

def mostrar_todos_professores():
    i = 0
    #Criar opção de mostrar o CPF
    for professor in professores:
        print(f"{professores[i]._primeiro_nome} {professores[i]._sobrenome}")
        i += 1
    menu_principal()

def mostrar_todas_materias():
    i = 0
    for pmateria in materias:
        print(materias[i]._nome_materia)
        i += 1
    menu_principal()

#Criando os menus
def menu_principal():
    print("[1] - Cadastrar Aluno \n[2] - Cadastrar Novo Professor \n[3] - Cadastrar Nova Matéria \n[4] - Mostrar Todos os Alunos")
    print("[5] - Mostrar Todos os Professores \n[6] - Mostrar Todas as Matérias \n[7] - Ir Para o Menu de Turmas \n[8] - Sair do Programa ")
    opcao = input("Digite o número correspondente a opção desejada: ")
    if int(opcao) == 1:
        cadastrar_aluno()
    elif int(opcao) == 2:
        cadastrar_professor()
    elif int(opcao) == 3:
        cadastrar_materia()
    elif int(opcao) == 4:
        mostrar_todos_alunos()
    elif int(opcao) == 5:
        mostrar_todos_professores()
    elif int(opcao) == 6:
        mostrar_todas_materias()
    elif int(opcao) == 7:
        menu_turmas()
    elif int(opcao) == 8:
        print("Sessão encerrada com sucesso")
    else:
        print("Opção não encontrada")

def menu_turmas():
    print("Menu em construção")

#Executando o código
menu_principal()


