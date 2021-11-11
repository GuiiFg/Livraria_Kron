
def get_livros ():

    import pandas as pd

    df = pd.read_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";")

    return df

def criar_modificar(
    id,
    nome,
    genero,
    quantidade,
    autor,
    ano,
    edicao,
    paginas):

    import pandas as pd

    df = pd.read_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";")

    df = df[df['id'] != int(id)]

    add = pd.DataFrame({
        "id": [int(id)],
        "nome": [nome],
        "genero": [genero],
        "quantidade_loco": [int(quantidade)],
        "quantidade_cliente": [0],
        "autor": [autor],
        "ano": [int(ano)],
        "edicao": [edicao],
        "paginas": [int(paginas)]
    })

    df = pd.concat([df, add])

    df = df.sort_values(by=['id'])

    df.to_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";", index=False)

def excluir(
    id):

    import pandas as pd

    df = pd.read_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";")

    df = df[df['id'] != int(id)]
    
    df = df.sort_values(by=['id'])

    df.to_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";", index=False)
