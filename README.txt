Funcionalidade a atribuir:
    verificações de erros:
        se os nomes são strings e apenas letras ( cadastros );
        se os cpf estão em formato de cpf - inteiros de 11 digitos (cadastros);
        

        se a materia está na lista de materias ( criar turma);
        se o professor está na lista de professores ( atribuir professor a turma);
        se o aluno está na lista de professores ( atribuir aluno a turma);

    adicionar opção de visualização dos CPFs;

Bugs:
    Especificados nas funções:
        designar_aluno();
        mostrar_turmas();
    
    Suposições:
        Acredito que o mesmo bug de designar_aluno() esteja acontecendo em desgnar_professor() e de alguma forma afetando remover_aluno()

Observações:
    Nos menus, existe um 'try/except' que pode deixar um pouco lenta a depuração, sugiro comentá-los