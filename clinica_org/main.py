import os
from utils import gerir_pacientes, gerir_consultas

def menu_principal():
    while True:
        os.system("cls || clear")
        
        print("""
        ----------------------------
        |     MENU PRINCIPAL       |
        ----------------------------
        | 1 | Login de Paciente    |
        ----------------------------
        | 2 | Cadastrar Paciente   |
        ----------------------------
        | 3 | Sair                 |
        ----------------------------
        """)

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                cpf = input("Digite seu CPF: ")
                senha = input("Digite sua senha: ")
                if gerir_pacientes.login_paciente(cpf, senha):
                    print("Login realizado com sucesso!")
                    menu_pos_login(cpf)  
                else:
                    print("CPF ou senha inválidos.")

            elif opcao == 2:
                nome = input("Nome: ")
                email = input("Email: ")
                telefone = input("Telefone: ")
                cpf = input("CPF: ")
                senha = input("Senha: ")
                gerir_pacientes.cadastrar_paciente(nome, email, telefone, cpf, senha)

            elif opcao == 3:
                print("Saindo...")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite um número válido!")

def menu_pos_login(cpf):
    while True:
        os.system("cls || clear")
        print("""
        ----------------------------
        |   MENU DE CONSULTAS      |
        ----------------------------
        | 1 | Gerenciar Consultas  |
        ----------------------------
        | 2 | Sair                 |
        ----------------------------
        """)

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 1:
                gerir_consultas.menu_consultas(cpf) 
            elif opcao == 2:
                break  
            else:
                print("Opção inválida.")

        except ValueError:
            print("Digite um número válido!")


menu_principal()
