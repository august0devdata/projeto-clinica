import bcrypt
from utils.gerir_banco import conexao

def cadastrar_paciente(nome, email, telefone, cpf, senha):
    cursor = conexao.cursor()

    try:
        senha_criptografada = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("""
            INSERT INTO clinica.pacientes (nome, email, telefone, cpf, senha)
            VALUES (%s, %s, %s, %s, %s)
        """, (nome, email, telefone, cpf, senha_criptografada))
        conexao.commit()
        print("Paciente cadastrado com sucesso!")

    except Exception as e:
        print("Erro ao cadastrar paciente:", e)

    finally:
        cursor.close()

def login_paciente(cpf, senha):
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT senha FROM clinica.pacientes WHERE cpf = %s", (cpf,))
        resultado = cursor.fetchone()

        if resultado:
            senha_armazenada = resultado[0]  

            if isinstance(senha_armazenada, memoryview):
                senha_armazenada = bytes(senha_armazenada)

            
            if bcrypt.checkpw(senha.encode('utf-8'), senha_armazenada):
                print("Login bem-sucedido!")
                return True
            else:
                print("Senha incorreta.")
                return False
        else:
            print("Usuário com esse CPF não encontrado.")
            return False
        
    except Exception as e:
        print(f"Erro ao tentar fazer login: {e}")
        return False
    
    finally:
        cursor.close()

