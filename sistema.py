#Importando os objetos e bibliotecas
from objetos import *
from operator import itemgetter
import os
import random

#Definindo as listas e listas de objetos
materias = []
professores = []
alunos = []
turmas = []

#Definindo variaveis auxiliares
lista_vazia = []
dicionario_vazio = {}

#Criando funcionalidades gerais
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

#Criando as funcionalidades do menu principal
def cadastrar_aluno():
    primeiro_nome = input("Digite o primeiro nome do aluno: ")
    primeiro_nome = primeiro_nome.strip().capitalize()
    while primeiro_nome.isalpha() == False:
        print("O nome deve conter apenas letras.")
        primeiro_nome = input("Digite o primeiro nome do aluno: ")

    sobrenome = input("Digite o sobrenome do aluno: ")
    sobrenome = sobrenome.strip().capitalize()
    while sobrenome.isalpha() == False:
        print("O sobrenome deve conter apenas letras.")
        sobrenome = input("Digite o sobrenome do aluno: ")
    
    cpf = input("Digite o CPF do aluno: ")
    cpf = cpf.strip()
    while len(cpf) != 11:
        print("O CPF deve conter os 11 dígitos numéricos")
        cpf = input("Digite o CPF do aluno: ")
        if cpf.isnumeric() == False:
            print("O CPF deve conter apenas números")
            cpf = input("Digite o CPF do aluno: ")

    alunos.append(Aluno(primeiro_nome, sobrenome, cpf))
    print(f"Aluno {primeiro_nome} {sobrenome} foi cadastrado com sucesso no CPF {cpf}.")
    menu_principal()

def cadastrar_professor():
    primeiro_nome = input("Digite o primeiro nome do professor: ")
    primeiro_nome = primeiro_nome.strip().capitalize()
    while primeiro_nome.isalpha() == False:
        print("O nome deve conter apenas letras.")
        primeiro_nome = input("Digite o primeiro nome do professor: ")

    sobrenome = input("Digite o sobrenome do professor: ")
    sobrenome = sobrenome.strip().capitalize()
    while sobrenome.isalpha() == False:
        print("O sobrenome deve conter apenas letras.")
        sobrenome = input("Digite o sobrenome do professor: ")
    
    cpf = input("Digite o CPF do professor: ")
    cpf = cpf.strip()
    while len(cpf) != 11:
        print("O CPF deve conter os 11 dígitos numéricos")
        cpf = input("Digite o CPF do professor: ")
        if cpf.isnumeric() == False:
            print("O CPF deve conter apenas números")
            cpf = input("Digite o CPF do professor: ")
    professores.append(Professor(primeiro_nome, sobrenome, cpf))
    print(f"Professor {primeiro_nome} {sobrenome} cadastrado com sucesso no CPF .")
    menu_principal()

def cadastrar_materia():
    nome_da_materia = input("Digite o nome da matéria: ")
    nome_da_materia = nome_da_materia.strip().capitalize()
    while nome_da_materia.isalpha() == False:
        print("O nome da matéria deve conter apenas letras.")
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

#Criando as funcionalidades do menu de turmas
def cadastrar_turma():
    materia = input("Insira o nome da matéria da turma: ")
    materia = materia.strip().capitalize()

    lista_materias = []
    for item in materias:
        lista_materias.append(item._nome_materia)
    if materia not in lista_materias:
        print("Matéria não cadastrada: ")
        print("Cadastre a matéria: ")
        cadastrar_materia()
        
    nome_da_turma = f"{materia}{random.randint(1000,9999)}"
    turmas.append(Turma(nome_da_turma,materia,None,lista_vazia,dicionario_vazio))
    clear()
    print(f"A turma {nome_da_turma} está pronta para receber os professores e os alunos \n")
    menu_turmas()

def designar_professor():
    turma_selecionada = input("Digite o nome da turma: ")
    turma_selecionada = turma_selecionada.strip().capitalize()
    todos_os_nomes = []
    for turma in turmas:
        todos_os_nomes.append(turma._nome_turma)
    if turma_selecionada not in todos_os_nomes:
        print("Turma não cadastrada")
        cadastrar_turma()
    else:
        for turma in turmas:
            if turma_selecionada == turma._nome_turma:
                professor = input("Digite o cpf do professor : ")
                todos_professores = []
                for item in professores:
                    todos_professores.append(item._cpf)
                if professor not in todos_professores:
                    print("Professor não cadastrado: ")
                    cadastrar_professor()

                turma._professor = professor
                print(f"O professor de CPF {professor} foi adicionado a turma {turma._nome_turma}")

    menu_turmas()

def designar_aluno():
    turma_selecionada = input("Digite o nome da turma: ")
    turma_selecionada = turma_selecionada.strip().capitalize()
    todos_os_nomes = []
    aluno = ''
    for turma in turmas:
        todos_os_nomes.append(turma._nome_turma)
    if turma_selecionada not in todos_os_nomes:
        print("Turma não cadastrada")
        cadastrar_turma()
    else:
        for turma in turmas:
            if turma_selecionada == turma._nome_turma:
                aluno = input("Digite o CPF do aluno: ")
                todos_alunos = []
            for item in alunos:
                todos_alunos.append(item._cpf)
            if aluno not in todos_alunos:
                print("Aluno não cadastrado: ")
                cadastrar_aluno()

            x = turma._alunos.copy()
            x.append(aluno)
            turma._alunos = x.copy()
            print(f"O aluno {aluno} foi adicionado a turma {turma._nome_turma}")
        menu_turmas()

def remover_aluno():
    turma_selecionada = input("Digite o nome da turma: ")
    turma_selecionada = turma_selecionada.strip().capitalize()
    todos_os_nomes = []
    aluno = ''
    for turma in turmas:
        todos_os_nomes.append(turma._nome_turma)
    if turma_selecionada not in todos_os_nomes:
        print("Turma não cadastrada")
        cadastrar_turma()
    else:
        for turma in turmas:
            if turma_selecionada == turma._nome_turma:
                aluno = input("Digite o CPF do aluno: ")
                todos_alunos = []
            for item in alunos:
                todos_alunos.append(item._cpf)
            if aluno not in todos_alunos:
                print("Aluno não cadastrado: ")
                cadastrar_aluno()
            try:
                turma._alunos.pop(turma._alunos.index(aluno))
            except:
                print("O aluno não está na turma. ")
                menu_turmas()
            print(f"O aluno de CPF {aluno} foi removido da {turma._nome_turma}")
            menu_turmas()

def atribuir_nota_aluno():
    aluno = input("Digite o CPF do aluno: ")
    todos_alunos = []
    for individuo in alunos:
        todos_alunos.append(individuo._cpf)
    if aluno not in todos_alunos:
        print("Aluno não encontrado")
        cadastrar_aluno()
    else:
        for individuo in alunos:
            if aluno == individuo._cpf:
                individuo.nota = input("Digite a nota do aluno: ")
                print(f"Nota {individuo.nota} atribuída ao aluno de CPF {individuo._cpf}")
                menu_turmas()

def mostrar_alunos_turma():
    turma_selecionada = input("Insira o nome da turma: ")
    turma_selecionada = turma_selecionada.strip().capitalize()
    turmas_atuais = []
    for turma in turmas:
        turmas_atuais.append(turma._nome_turma)
    if turma_selecionada in turmas_atuais:
        lista = sorted(turma._alunos)
        for nome in lista:
            print(nome)            
        menu_turmas()
    else:
        print("Turma não cadastrada")
        cadastrar_turma()

def mostrar_turmas():
    quantidades = []
    nomes = []
    tuplas = []
    for turma in turmas:
        turma.tamanho_turma = len(turma._alunos)
        quantidades.append(turma.tamanho_turma)
        nomes.append(turma._nome_turma)
    for i in range(0, len(quantidades)):
        tuplas.append((quantidades[i],nomes[i]))
    x = sorted(tuplas, key=lambda tuplas: tuplas[0], reverse=True)
    for i in range(0, len(tuplas)): 
        print(x[i][1])
    menu_turmas()

#Criando os menus
def menu_principal():
    print("[1] - Cadastrar Aluno \n[2] - Cadastrar Novo Professor \n[3] - Cadastrar Nova Matéria \n[4] - Mostrar Todos os Alunos")
    print("[5] - Mostrar Todos os Professores \n[6] - Mostrar Todas as Matérias \n[7] - Ir Para o Menu de Turmas \n[8] - Sair do Programa ")
    opcao = input("Digite o número correspondente a opção desejada: ")
    try:
        opcao = int(opcao)
    except:
        print("Digite apenas o número da opção selecionada")
    if opcao == 1:
            cadastrar_aluno()
    elif opcao == 2:
            cadastrar_professor()
    elif opcao == 3:
            cadastrar_materia()
    elif opcao == 4:
            mostrar_todos_alunos()
    elif opcao == 5:
            mostrar_todos_professores()
    elif opcao == 6:
            mostrar_todas_materias()
    elif opcao == 7:
            menu_turmas()
    elif opcao == 8:
            print("Sessão encerrada com sucesso")
    else:
            print("Opção não encontrada")


def menu_turmas():
    print("[1] - Cadastrar Nova Turma \n[2] - Designar Professor Para Turma \n[3] - Atribuir Alunos a Turma \n[4] - Remover Aluno da Turma")
    print("[5] - Adicionar Nota a Aluno \n[6] - Mostrar Alunos da Turma \n[7] - Mostrar Todas as Turmas\n[8] - Voltar ao Menu Principal")
    opcao = input("Digite o número correspondente a opção desejada: ")
    try:
        opcao = int(opcao)
    except:
        print("Digite apenas o número da opção selecionada")
    if opcao == 1:
        cadastrar_turma()
    elif opcao == 2:
        designar_professor()
    elif opcao == 3:
        designar_aluno()
    elif opcao == 4:
        remover_aluno()
    elif opcao == 5:
        atribuir_nota_aluno()
    elif opcao == 6:
        mostrar_alunos_turma()
    elif opcao == 7:
        mostrar_turmas()
    elif opcao == 8:
        menu_principal()
    else:
        print("Opção não encontrada")     

#Executando o código
clear()
menu_principal()



