import mysql.connector

def conectar():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            port=3306,
            database="univap"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def criar_dxp(codigodisciplinanocurso, coddisciplina, codprofessor, curso, cargahoraria, anoletivo):
    if not all(isinstance(x, int) and x > 0 for x in [codigodisciplinanocurso, coddisciplina, codprofessor, curso, cargahoraria, anoletivo]):
        print("Todos os campos devem ser inteiros positivos.")
        return False
    if anoletivo < 2000 or anoletivo > 2100:
        print("Ano letivo inválido.")
        return False
    if cargahoraria < 1 or cargahoraria > 1000:
        print("Carga horária inválida.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM disciplinas WHERE codigodisc = %s", (coddisciplina,))
        if not cursor.fetchone():
            print("Disciplina não existe.")
            return False
        cursor.execute("SELECT 1 FROM professores WHERE registro = %s", (codprofessor,))
        if not cursor.fetchone():
            print("Professor não existe.")
            return False
        cursor.execute("SELECT 1 FROM disciplinasxprofessores WHERE codigodisciplinanocurso = %s", (codigodisciplinanocurso,))
        if cursor.fetchone():
            print("Código da relação já existe.")
            return False
        sql = """INSERT INTO disciplinasxprofessores 
            (codigodisciplinanocurso, coddisciplina, codprofessor, curso, cargahoraria, anoletivo)
            VALUES (%s, %s, %s, %s, %s, %s)"""
        valores = (codigodisciplinanocurso, coddisciplina, codprofessor, curso, cargahoraria, anoletivo)
        cursor.execute(sql, valores)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao criar relação: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def ler_dxp():
    conn = conectar()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplinasxprofessores")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro ao ler relações: {err}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def deletar_dxp(codigodisciplinanocurso):
    if not isinstance(codigodisciplinanocurso, int) or codigodisciplinanocurso <= 0:
        print("Código inválido para deletar relação.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM disciplinasxprofessores WHERE codigodisciplinanocurso = %s", (codigodisciplinanocurso,)) #-
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhuma relação encontrada para deletar.")
            return False
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao deletar relação: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()