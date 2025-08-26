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

def criar_professor(registro, nome, telefone, idade, salario):
    if not isinstance(registro, int) or registro <= 0:
        print("Registro inválido.")
        return False
    if not isinstance(nome, str) or len(nome.strip()) < 3 or not all(x.isalpha() or x.isspace() for x in nome):
        print("Nome inválido.")
        return False
    if not isinstance(telefone, str) or not telefone.isdigit() or len(telefone) < 8:
        print("Telefone inválido.")
        return False
    if not isinstance(idade, int) or idade < 18 or idade > 120:
        print("Idade inválida. Professor deve ser maior de idade e menor que 120.")
        return False
    if not isinstance(salario, (int, float)) or salario <= 0:
        print("Salário inválido.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM professores WHERE registro = %s", (registro,))
        if cursor.fetchone():
            print("Registro já existe.")
            return False
        sql = "INSERT INTO professores (registro, nomeprof, telefoneprof, idadeprof, salarioprof) VALUES (%s, %s, %s, %s, %s)"
        valores = (registro, nome.strip(), telefone, idade, salario)
        cursor.execute(sql, valores)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao criar professor: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def ler_professores():
    conn = conectar()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM professores")
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as err:
        print(f"Erro ao ler professores: {err}")
        return []
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def ler_professor_por_registro(registro):
    if not isinstance(registro, int) or registro <= 0:
        print("Registro inválido.")
        return None
    conn = conectar()
    if conn is None:
        return None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM professores WHERE registro = %s", (registro,))
        resultado = cursor.fetchone()
        return resultado
    except mysql.connector.Error as err:
        print(f"Erro ao buscar professor: {err}")
        return None
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def atualizar_professor(registro, nome, telefone, idade, salario):
    if not isinstance(registro, int) or registro <= 0:
        print("Registro inválido.")
        return False
    if not isinstance(nome, str) or len(nome.strip()) < 3 or not all(x.isalpha() or x.isspace() for x in nome):
        print("Nome inválido.")
        return False
    if not isinstance(telefone, str) or not telefone.isdigit() or len(telefone) < 8:
        print("Telefone inválido.")
        return False
    if not isinstance(idade, int) or idade < 18 or idade > 120:
        print("Idade inválida. Professor deve ser maior de idade e menor que 120.")
        return False
    if not isinstance(salario, (int, float)) or salario <= 0:
        print("Salário inválido.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        sql = "UPDATE professores SET nomeprof=%s, telefoneprof=%s, idadeprof=%s, salarioprof=%s WHERE registro=%s"
        valores = (nome.strip(), telefone, idade, salario, registro)
        cursor.execute(sql, valores)
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhum professor encontrado para atualizar.")
            return False
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao atualizar professor: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()

def deletar_professor(registro):
    if not isinstance(registro, int) or registro <= 0:
        print("Registro inválido para deletar.")
        return False
    conn = conectar()
    if conn is None:
        return False
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM disciplinasxprofessores WHERE codprofessor = %s", (registro,)) #-
        if cursor.fetchone():
            print("Não é possível deletar: professor relacionado a disciplinas.")
            return False
        cursor.execute("DELETE FROM professores WHERE registro = %s", (registro,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhum professor encontrado para deletar.")
            return False
        return True
    except mysql.connector.Error as err:
        print(f"Erro ao deletar professor: {err}")
        return False
    finally:
        if 'cursor' in locals():
            cursor.close()
        conn.close()