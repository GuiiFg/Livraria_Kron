import hashlib

from . import conn as Connect_db

def fazer_login (nick:str, senha:str):
    import pandas as pd
    from .. import Cliente

    df = Connect_db.Query_clientes("SELECT * FROM Clientes_tb")

    df = df[df['nick'] == nick]

    if len(df) != 1:
        return [False]

    senha_banco = list(df.senha)[0]

    senha = hashlib.md5(senha.encode())

    if senha_banco == senha.hexdigest():

        tipo = list(df.tipo)[0]

        if int(tipo) == 1:

            user = [ Cliente.Cliente(
                nome = row.nome,
                nick = row.nick,
                tipo = row.tipo

            ) for index, row in df.iterrows()]

        else:
            user = [ Cliente.CI(
                nome = row.nome,
                nick = row.nick,
                tipo = row.tipo

            ) for index, row in df.iterrows()]

        return [True, user, tipo]

        
    else:
        return [False]


def criar_cliente(nome, nick, senha):

    senha = hashlib.md5(senha.encode())

    senhacod = senha.hexdigest()


    query = f"""
    INSERT INTO Clientes_tb VALUES(
        '{nome}',
        '{nick}',
        '{senhacod}',
        '1'
    );
    """

    Connect_db.Insert_clientes(query)
    