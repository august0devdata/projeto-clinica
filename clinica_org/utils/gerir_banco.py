import psycopg2 as pg
import pandas as pd
import os
from utils import gerir_usuarios as users


user_bd = 1
senha_bd = 1
banco = 1
port = 1
host_bd = 1


def conectar_bd():

    try:
        conexao = pg.connect(
            dbname=banco,
            user=user_bd,
            password=senha_bd,
            host=host_bd,
            port=port
        )

        print("Conexão estabelecida com sucesso!")
        return conexao
    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
conexao = conectar_bd()


