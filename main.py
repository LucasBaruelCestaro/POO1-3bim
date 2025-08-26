from DAO import professoresDAO, diciplinasDAO, dxpDAO
from tabulate import tabulate
from colorama import Fore, Style, init

init(autoreset=True)

def print_table(data, headers):
    if not data:
        print(Fore.YELLOW + "Nenhum registro encontrado.")
    else:
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

def menu(titulo, opcoes):
    print(Fore.CYAN + f"\n--- {titulo} ---")
    for i, op in enumerate(opcoes):
        print(f"{i}. {op}")
    return input(Fore.GREEN + "Escolha: ")

def main():
    while True:
        op = menu("MENU PRINCIPAL", ["Sair", "Professores", "Disciplinas", "Disciplinas x Professores"])
        if op == "1":
            while True:
                op2 = menu("CRUD PROFESSORES", ["Voltar", "Listar", "Inserir", "Atualizar", "Deletar"])
                if op2 == "1":
                    dados = professoresDAO.ler_professores()
                    print_table(dados, ["Registro", "Nome", "Telefone", "Idade", "Salário"])
                elif op2 == "2":
                    try:
                        registro = int(input("Registro: "))
                        nome = input("Nome: ")
                        telefone = input("Telefone: ")
                        idade = int(input("Idade: "))
                        salario = float(input("Salário: "))
                        sucesso = professoresDAO.criar_professor(registro, nome, telefone, idade, salario)
                        if not sucesso:
                            print(Fore.RED + "Falha ao inserir professor. Verifique os dados.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "3":
                    try:
                        registro = int(input("Registro do professor a atualizar: "))
                        nome = input("Novo nome: ")
                        telefone = input("Novo telefone: ")
                        idade = int(input("Nova idade: "))
                        salario = float(input("Novo salário: "))
                        sucesso = professoresDAO.atualizar_professor(registro, nome, telefone, idade, salario)
                        if not sucesso:
                            print(Fore.RED + "Falha ao atualizar professor. Verifique os dados.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "4":
                    try:
                        registro = int(input("Registro do professor a deletar: "))
                        sucesso = professoresDAO.deletar_professor(registro)
                        if not sucesso:
                            print(Fore.RED + "Falha ao deletar professor. Verifique se não está relacionado a disciplinas.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "0":
                    break
        elif op == "2":
            while True:
                op2 = menu("CRUD DISCIPLINAS", ["Voltar", "Listar", "Inserir", "Atualizar", "Deletar"])
                if op2 == "1":
                    dados = diciplinasDAO.ler_disciplinas()
                    print_table(dados, ["Código", "Nome"])
                elif op2 == "2":
                    try:
                        codigo = int(input("Código: "))
                        nome = input("Nome: ")
                        sucesso = diciplinasDAO.criar_disciplina(codigo, nome)
                        if not sucesso:
                            print(Fore.RED + "Falha ao inserir disciplina. Verifique os dados.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "3":
                    try:
                        codigo = int(input("Código da disciplina a atualizar: "))
                        nome = input("Novo nome: ")
                        sucesso = diciplinasDAO.atualizar_disciplina(codigo, nome)
                        if not sucesso:
                            print(Fore.RED + "Falha ao atualizar disciplina. Verifique os dados.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "4":
                    try:
                        codigo = int(input("Código da disciplina a deletar: "))
                        sucesso = diciplinasDAO.deletar_disciplina(codigo)
                        if not sucesso:
                            print(Fore.RED + "Falha ao deletar disciplina. Verifique se não está relacionada a professores.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "0":
                    break
        elif op == "3":
            while True:
                op2 = menu("CRUD DISCIPLINAS x PROFESSORES", ["Voltar", "Listar", "Inserir", "Deletar"])
                if op2 == "1":
                    dados = dxpDAO.ler_dxp()
                    print_table(dados, ["CodDiscNoCurso", "CodDisciplina", "CodProfessor", "Curso", "CargaHorária", "AnoLetivo"])
                elif op2 == "2":
                    try:
                        codigodisciplinanocurso = int(input("Código da relação: "))
                        coddisciplina = int(input("Código da disciplina: "))
                        codprofessor = int(input("Código do professor: "))
                        curso = int(input("Curso: "))
                        cargahoraria = int(input("Carga horária: "))
                        anoletivo = int(input("Ano letivo: "))
                        sucesso = dxpDAO.criar_dxp(codigodisciplinanocurso, coddisciplina, codprofessor, curso, cargahoraria, anoletivo)
                        if not sucesso:
                            print(Fore.RED + "Falha ao inserir relação. Verifique os dados.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "3":
                    try:
                        codigodisciplinanocurso = int(input("Código da relação a deletar: "))
                        sucesso = dxpDAO.deletar_dxp(codigodisciplinanocurso)
                        if not sucesso:
                            print(Fore.RED + "Falha ao deletar relação. Verifique o código.")
                    except Exception:
                        print(Fore.RED + "Erro nos dados.")
                elif op2 == "0":
                    break
        elif op == "0":
            print(Fore.MAGENTA + "Saindo...")
            break

if __name__ == "__main__":
    main()