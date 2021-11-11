import hashlib

def fazer_login (nick:str, senha:str):
    import pandas as pd

    from .. import Cliente

    df = pd.read_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/clientes.csv", ";")

    df = df[df['nick'] == nick]

    if len(df) != 1:
        return [False]

    senha_banco = list(df.senha)[0]

    senha = hashlib.md5(senha.encode())

    if senha_banco == senha.hexdigest():

        tipo = senha_banco = list(df.tipo)[0]

        if int(tipo) == 1:

            user = [ Cliente.Cliente(
                nome = row.nome,
                idade = row.idade,
                id = row.id,
                livros_alugados = row.livros_alugados

            ) for index, row in df.iterrows()]

        else:
            user = [ Cliente.CI(
                nome = row.nome,
                idade = row.idade,
                id = row.id

            ) for index, row in df.iterrows()]

        return [True, user, tipo]

        
    else:
        return [False]



    