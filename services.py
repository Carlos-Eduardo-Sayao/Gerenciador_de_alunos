from database.conexao import *

def cadastrar_aluno(aluno):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO alunos(turma_id,matricula,nome) VALUES (%s,%s,%s)"

    valores = (aluno.turma_id,aluno.matricula,aluno.nome)
    cursor.execute(sql,valores )

    conn.commit()
    aluno.id = cursor.lastrowid
    conn.close()

def cadastrar_turma(turma):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO turmas(letra,nivel_ensino,serie,ano) VALUES (%s,%s,%s,%s)" 
    valores = (turma.letra,turma.nivel_ensino,turma.serie,turma.ano)
    cursor.execute(sql,valores)

    conn.commit()
    turma.id = cursor.lastrowid
    conn.close()

def cadastrar_nota(nota):
    conn = conectar()
    cursor = conn.cursor()

    sql = "INSERT INTO notas(aluno_id,materia,unidade,pontuacao) VALUES (%s,%s,%s,%s)"
    valores = (nota.aluno_id,nota.materia,nota.unidade,nota.pontuacao)
    cursor.execute(sql,valores)
    nota.id = cursor.lastrowid

    conn.commit()
    conn.close()

def deletar_aluno(aluno_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM alunos WHERE id = %s"
    valores = (aluno_id,)
    cursor.execute(sql,valores)
    if cursor.rowcount > 0:
        conn.commit()
        return 1
    conn.close()
    return 0

def deletar_turma(turma_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM turmas WHERE id = %s"
    valores = (turma_id,)
    cursor.execute(sql,valores)
    if cursor.rowcount > 0:
        conn.commit()
        return 1
    conn.close()
    return 0

def atualizar_aluno(campo,novo_valor,aluno_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = f"UPDATE alunos SET {campo} = %s WHERE id = %s"
    valores = (novo_valor,aluno_id)
    cursor.execute(sql,valores)
    conn.commit()
    conn.close()

def atualizar_turma(campo,novo_valor,turma_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = f"UPDATE turmas SET {campo} = %s WHERE id = %s"
    valores = (novo_valor,turma_id)
    cursor.execute(sql,valores)
    conn.commit()
    conn.close()

def atualizar_nota(materia,unidade,aluno_id,novo_valor):
    conn = conectar()
    cursor = conn.cursor()
    sql =f"UPDATE notas SET pontuacao = %s WHERE aluno_id = %s AND materia = %s AND unidade = %s"
    valores = (novo_valor,aluno_id,materia,unidade)
    cursor.execute(sql,valores)
    conn.commit()
    conn.close()
    
def buscar_turma_id(letra,nivel_ensino,serie,ano):
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id FROM turmas WHERE letra = %s AND nivel_ensino = %s  AND serie = %s AND ano = %s"
    valores = (letra,nivel_ensino,serie,ano)
    cursor.execute(sql,valores)
    resultado = cursor.fetchone()

    conn.close()

    if resultado:
        return resultado[0]
    else:
        return None
    
def buscar_aluno_id(matricula):
    conn = conectar()
    cursor = conn.cursor()

    sql = "SELECT id FROM alunos WHERE matricula = %s"
    valores = (matricula,)
    cursor.execute(sql,valores)
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return resultado[0]
    
def mostrar_turmas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id,letra,nivel_ensino,serie,ano FROM turmas")
    for id,letra,nivel_ensino,serie,ano in cursor.fetchall():
        print(f"ID:{id}--Nível de ensino:{nivel_ensino}--Turma:{serie}{letra}--Ano:{ano}")
    conn.close()

def mostrar_alunos(turma_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT id , turma_id , matricula , nome FROM alunos WHERE turma_id = %s"
    valores = (turma_id,)
    cursor.execute(sql,valores)
    for id , id_turma , matricula , nome in cursor.fetchall():
        print(f"ID:{id}--Turma ID:{id_turma}--Matrícula:{matricula}--Nome:{nome}")
    conn.close()

def mostrar_notas(aluno_id):
    conn = conectar()
    cursor = conn.cursor()
    sql = "SELECT materia , unidade , pontuacao FROM notas WHERE aluno_id = %s"
    valores = (aluno_id,)
    cursor.execute(sql,valores)
    for materia , unidade , pontuacao in cursor.fetchall():
        print(f"Matéria:{materia}--Unidade:{unidade}ª--Nota:{pontuacao}")
    conn.close()
    
