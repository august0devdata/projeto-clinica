from utils.gerir_banco import conexao
import os 

def menu_consultas(cpf):
    while True:
        
       

        print("""
        ----------------------------
        |   GERENCIAR CONSULTAS    |
        ----------------------------
        | 1 | Marcar Consulta      |
        ----------------------------
        | 2 | Visualizar Consultas |
        ----------------------------
        | 3 | Atualizar Consulta   |
        ----------------------------
        | 4 | Deletar Consulta     |
        ----------------------------
        | 5 | Voltar               |
        ----------------------------
        """)
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            marcar_consulta(cpf)
        elif opcao == 2:
            visualizar_consultas(cpf)
        elif opcao == 3:
            atualizar_consulta(cpf)
        elif opcao == 4:
            deletar_consulta(cpf)
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")

def marcar_consulta(cpf):
 
    os.system("cls || clear")
    cursor = conexao.cursor()
    
    try:
        
        cursor.execute("""
            SELECT m.id, m.nome, e.tipo_especialidade 
            FROM clinica.medicos m
            JOIN clinica.especialidades e ON m.id_especialidade = e.id
        """)
        
        medicos = cursor.fetchall()

        if medicos:
            print("Selecione um médico:")
            for medico in medicos:
                print(f"ID: {medico[0]}, Nome: {medico[1]}, Especialidade: {medico[2]}")

     
            medico_id = int(input("Digite o ID do Médico: "))
        else:
            print("Nenhum médico encontrado.")
            return
        
        
        data_consulta = input("Data da consulta (YYYY-MM-DD): ")
        hora_consulta = input("Hora da consulta (HH:MM): ")

   
        cursor.execute("""
            INSERT INTO clinica.consultas (data_consulta, hora_consulta, id_medico, id_paciente)
            VALUES (%s, %s, %s, %s)
        """, (data_consulta, hora_consulta, medico_id, cpf))
        conexao.commit()

        print("Consulta marcada com sucesso!")
        
    except Exception as e:
        print("Erro ao marcar consulta:", e)
    finally:
        cursor.close()


def visualizar_consultas(cpf):
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT c.id, c.data_consulta, c.hora_consulta, m.nome 
            FROM clinica.consultas c
            JOIN clinica.medicos m ON c.id_medico = m.id
            JOIN clinica.pacientes p ON c.id_paciente = p.id
            WHERE p.cpf = %s
            ORDER BY c.data_consulta
        """, (cpf,))
        consultas = cursor.fetchall()

        if consultas:
            for consulta in consultas:
                print(f"ID: {consulta[0]}, Data: {consulta[1]}, Hora: {consulta[2]}, Médico: {consulta[3]}")
        else:
            print("Nenhuma consulta encontrada.")

    except Exception as e:
        print("Erro ao visualizar consultas:", e)
        conexao.rollback()  
        cursor.close()


def atualizar_consulta(cpf):
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT c.id, c.data_consulta, c.hora_consulta, m.nome 
            FROM clinica.consultas c
            JOIN clinica.medicos m ON c.id_medico = m.id
            JOIN clinica.pacientes p ON c.id_paciente = p.id
            WHERE p.cpf = %s
            ORDER BY c.data_consulta
        """, (cpf,))
        consultas = cursor.fetchall()

        if consultas:
            print("Consultas encontradas:")
            for consulta in consultas:
                print(f"ID: {consulta[0]}, Data: {consulta[1]}, Hora: {consulta[2]}, Médico: {consulta[3]}")

            
            consulta_id = input("Digite o ID da consulta que deseja atualizar: ")

            
            nova_data = input("Nova Data (YYYY-MM-DD): ")
            novo_horario = input("Novo Horário (HH:MM): ")

            
            cursor.execute("""
                UPDATE clinica.consultas
                SET data_consulta = %s, hora_consulta = %s
                WHERE id = %s AND id_paciente = %s
            """, (nova_data, novo_horario, consulta_id, cpf))

            conexao.commit()
            print("Consulta atualizada com sucesso!")

        else:
            print("Nenhuma consulta encontrada.")

    except Exception as e:
        print("Erro ao atualizar consulta:", e)
        conexao.rollback()  
    finally:
        cursor.close()


def deletar_consulta(cpf):
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT c.id, c.data_consulta, c.hora_consulta, m.nome 
            FROM clinica.consultas c
            JOIN clinica.medicos m ON c.id_medico = m.id
            JOIN clinica.pacientes p ON c.id_paciente = p.id
            WHERE p.cpf = %s
            ORDER BY c.data_consulta
        """, (cpf,))
        consultas = cursor.fetchall()

        if consultas:
            print("Consultas encontradas:")
            for consulta in consultas:
                print(f"ID: {consulta[0]}, Data: {consulta[1]}, Hora: {consulta[2]}, Médico: {consulta[3]}")

            
            consulta_id = input("Digite o ID da consulta que deseja excluir: ")

            cursor.execute("""
                DELETE FROM clinica.consultas
                WHERE id = %s AND id_paciente = %s
            """, (consulta_id, cpf))
            conexao.commit()

            print("Consulta deletada com sucesso!")

        else:
            print("Nenhuma consulta encontrada.")

    except Exception as e:
        print("Erro ao deletar consulta:", e)
        conexao.rollback()  
    finally:
        cursor.close()

