import mysql.connector

def conectar():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "@1109Dudu",
        database = "sistema_gerenciador_aluno"
    )

    return conn

