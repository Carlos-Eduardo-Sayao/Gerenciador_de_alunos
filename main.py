from services import *
from models.turma import *
from models.aluno import *
from models.nota import *
print("==Sistema de Gerenciador de Alunos==")
while True:
    print("Escolha uma opção:")
    print("0-Encerrar")
    print("1-Cadastrar turma")
    print("2-Cadastrar aluno")
    print("3-Cadastrar nota do aluno")
    print("4-Deletar aluno")
    print("5-Deletar turma")
    print("6-Atualizar dados do aluno")
    print("7-Atualizar dados da turma")
    print("8-Atualizar nota")
    print("9-Mostrar turmas cadastradas")
    print("10-Mostrar alunos cadastrados")
    print("11-Mostrar Notas dos aluno")

    opcao = int(input(">"))
    if opcao == 1:
        nivel_ensino = input("Digite o nível de ensino escolar:").title().strip()
        serie = int(input("Digite a série escolar:"))
        letra = input("Digite a letra da turma:").upper().strip()
        ano = int(input("Digite o ano:"))
        turma = Turma(letra,nivel_ensino,serie,ano)
        cadastrar_turma(turma)
        print("Turma cadastrada com sucesso")
        print("-"*30)

    elif opcao == 2:
        print("<==Turmas cadastradas==>")
        mostrar_turmas()
        turma_id = int(input("Digite o id da turma do aluno que deseja cadastrar:"))
        matricula = input("Digite a matrícula do aluno(a):").strip()
        nome = input("Digite o nome do aluno(a):").title().strip()
        aluno = Aluno(turma_id,matricula,nome)
        cadastrar_aluno(aluno)
        print("Aluno(a) cadastrado com sucesso")
        print("-"*30)

    elif opcao == 3:
        matricula = input("Digite a matricula do aluno:").strip()
        aluno_id = buscar_aluno_id(matricula)
        materia = input("Digite a matéria:").title().strip()
        unidade = int(input("Digite a unidade:"))
        pontuacao = float(input(f"Digite a nota do aluno na {unidade}ª unidade:"))
        notas = Nota(aluno_id,materia,unidade,pontuacao)
        cadastrar_nota(notas)
        print("Nota Cadastrada com sucesso")
        print("-"*30)

    elif opcao == 4:
        matricula = input("Digite a matrícula do aluno que deseja deletar(OBS: suas notas serão deletadas automaticamente):").strip()
        aluno_id  = buscar_aluno_id(matricula)
        resultado = deletar_aluno(aluno_id)
        if resultado >0:
            print("Aluno deletado com sucesso")
            print("-"*30)
        else:
            print("Esse aluno não existe")
            print("-"*30)

    elif opcao == 5:
        print("<==Turmas cadastradas==>")
        mostrar_turmas()
        turma_id = int(input("Digite o id da turma que deseja deletar(OBS: os alunos dessa turma serão deletadas automaticamente):"))
        resultado = deletar_turma(turma_id)
        if resultado > 0:
            print("Turma deletada com sucesso")
            print("-"*30)
        else:
            print("Essa turma não existe")
            print("-"*30)

    elif opcao == 6:
        matricula = input("Digite a matrícula do aluno que deseja atualizar:")
        aluno_id = buscar_aluno_id(matricula)
        campos = {
            1:"matricula",
            2:"nome",
            3:"Sair"
        }
        while True:
            print("Escolha uma opção:")
            print("1-Atualizar matrícula")
            print("2-Atualizar nome")
            print("3-Sair")
            opcao = int(input(">"))
            campo = campos.get(opcao)
            if not campo:
                print("Opção inválida")
            elif opcao ==1:
                novo_valor = input("Digite a nova matrícula:").strip()
                atualizar_aluno(campo,novo_valor,aluno_id)
                matricula = novo_valor
                print("Aluno(a) atualizado com sucesso")
            elif opcao == 2:
                novo_valor = input("Digite o novo nome:").title().strip()
                atualizar_aluno(campo,novo_valor,aluno_id)
                print("Aluno(a) atualizado com sucesso")
            elif opcao == 3:
                print("Saindo...")
                break
        print("-"*30)

    elif opcao == 7:
        print("<==Turmas cadastradas==>")
        mostrar_turmas()
        turma_id = int(input("Digite o id da turma que deseja atualizar:"))
        campos = {
            1:"letra",
            2:"nivel_ensino",
            3:"serie",
            4:"ano",
            5:"Sair"
        }
        while True:
            print("Escolha uma opção:")
            print("1-Atualizar letra")
            print("2-Atualizar nível de ensino")
            print("3-Atualizar série")
            print("4-Atualizar ano")
            print("5-sair")
            opcao = int(input(">"))
            campo = campos.get(opcao)
            if not campo:
                print("opção inválida")
            elif opcao == 1:
                novo_valor = input("Digite a nova letra:").upper().strip()
                atualizar_turma(campo,novo_valor,turma_id)
                letra = novo_valor
                print("Turma atualizada com sucesso")
            elif opcao == 2:
                novo_valor = input("Digite o novo nível de ensino:").title().strip()
                atualizar_turma(campo,novo_valor,turma_id)
                nivel_ensino = novo_valor
                print("Turma atualizada com sucesso")
            elif opcao == 3:
                novo_valor = int(input("Digite a nova série escolar:"))
                atualizar_turma(campo,novo_valor,turma_id)
                serie = novo_valor
                print("Turma atualizada com sucesso")
            elif opcao == 4:
                novo_valor = int(input("Digite o novo ano:"))
                ano = novo_valor
                atualizar_turma(campo,novo_valor,turma_id)
                print("Turma atualizada com sucesso")
            elif opcao == 5:
                print("Saindo...")
                break
        print("-"*30)

    elif opcao == 8:
        matricula = input("Digite a matrícula do aluno que deseja atualizar a nota:").strip()
        materia = input("Digite matéria que deseja atualizar a nota:").title().strip()
        unidade = int(input("Digite a unidade que deseja atualizar a nota:"))
        novo_valor = float(input("Digite a nova nota:"))
        aluno_id = buscar_aluno_id(matricula)
        atualizar_nota(materia,unidade,aluno_id,novo_valor)
        print("Nota atualizada com sucesso")
        print("-"*30)

    elif opcao == 9:
        print("<==Turmas cadastradas==>")
        mostrar_turmas()
        print("-"*30)

    elif opcao == 10:
        print("<==Turmas cadastradas==>")
        mostrar_turmas()
        turma_id = int(input("Digite o id da turma que deseja ver os alunos cadastrados:"))
        print("<==Alunos cadastrados==>")
        mostrar_alunos(turma_id)
        print("-"*30)

    elif opcao == 11:
        matricula = input("Digite a matrícula do aluno:").strip()
        aluno_id = buscar_aluno_id(matricula)
        print("<==Notas==>")
        mostrar_notas(aluno_id)
        print("-"*30)

    elif opcao == 0:
        print("Encerrando...")
        print("-"*30)
        break

    else:
        print("Opção inválida , tente novamente")
        print("-"*30)


    