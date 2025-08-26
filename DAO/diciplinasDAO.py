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

def criar_disciplina(codigo, nome):
    if not isinstance(codigo, int) or codigo <= 0:
        print("Código inválido.")
        return False
    if not isinstance(nome, str) or len(nome.strip()) < 3 or not all(x.isalpha() or x.isspace() for x in nome):
        print("Nome inválido.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM disciplinas WHERE codigodisc = %s", (codigo,))
        if cursor.fetchone():
            print("Código já existe.")
            return False
        sql = "INSERT INTO disciplinas (codigodisc, nomedisc) VALUES (%s, %s)"
        cursor.execute(sql, (codigo, nome.strip()))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao criar disciplina: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def ler_disciplinas():
    conn = conectar()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplinas")
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Erro ao ler disciplinas: {err}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def ler_disciplina_por_codigo(codigo):
    if not isinstance(codigo, int) or codigo <= 0:
        print("Código inválido.")
        return None
    conn = conectar()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM disciplinas WHERE codigodisc = %s", (codigo,))
        return cursor.fetchone()
    except mysql.connector.Error as err:
        print(f"Erro ao buscar disciplina: {err}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def atualizar_disciplina(codigo, nome):
    if not isinstance(codigo, int) or codigo <= 0:
        print("Código inválido.")
        return False
    if not isinstance(nome, str) or len(nome.strip()) < 3 or not all(x.isalpha() or x.isspace() for x in nome):
        print("Nome inválido.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        sql = "UPDATE disciplinas SET nomedisc=%s WHERE codigodisc=%s"
        cursor.execute(sql, (nome.strip(), codigo))
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhuma disciplina encontrada para atualizar.")
            return False
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar disciplina: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def deletar_disciplina(codigo):
    if not isinstance(codigo, int) or codigo <= 0:
        print("Código inválido para deletar.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM disciplinasxprofessores WHERE coddisciplina = %s", (codigo,)) #-
        if cursor.fetchone():
            print("Não é possível deletar: disciplina relacionada a professores.")
            return False
        cursor.execute("DELETE FROM disciplinas WHERE codigodisc = %s", (codigo,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhuma disciplina encontrada para deletar.")
            return False
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao deletar disciplina: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()