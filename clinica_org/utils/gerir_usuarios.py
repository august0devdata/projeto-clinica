from utils import gerir_banco as bd
import os
import bcrypt as cript


def cadastrar_usuario(nome, email, telefone, cpf, senha):
    cursor = bd.conexao.cursor()
    senha_criptografada = cript.hashpw(senha.encode(), cript.gensalt())

    query = """
        INSERT INTO clinica.pacientes (nome, email, telefone, cpf, senha)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (nome, email, telefone, cpf, senha_criptografada)

    try:
        cursor.execute(query, valores)
        bd.conexao.commit()
        os.system("cls || clear")
        print("Cadastrado com sucesso!")
    except Exception as e:
        bd.conexao.rollback()
        print("Erro ao cadastrar o usuário:", e)
    finally:
        cursor.close()


def login_usuario(cpf, senha):
    cursor = bd.conexao.cursor()

    query = "SELECT cpf, senha FROM clinica.pacientes WHERE cpf = %s"

    try:
        cursor.execute(query, (cpf,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Usuário não encontrado!")
            return False

        cpf_armazenado, senha_armazenada = resultado

        if cript.checkpw(senha.encode(), senha_armazenada):
            print(f"Login bem-sucedido! Bem-vindo, usuário com CPF {cpf_armazenado}.")
            return True
        else:
            print("Senha incorreta!")
            return False

    except Exception as e:
        print("Erro ao realizar o login:", e)
        return False

    finally:
        cursor.close()

