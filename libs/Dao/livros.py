
def get_livros ():

    import pandas as pd

    df = pd.read_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";")

    return df

def criar_modificar(
    id = None,
    nome = None,
    genero = None,
    quantidade = None,
    autor = None,
    ano = None,
    edicao = None,
    paginas = None):

    import pandas as pd

    df = pd.read_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";")

    df = df[df['id'] != int(id)]
    dfcom = df[df['id'] == int(id)]

    if len(dfcom) == 1:

        dfcom["id"] = int(id) if id != None else dfcom["id"]
        dfcom["nome"] = nome if nome != None else dfcom["nome"]
        dfcom["genero"] = genero if genero != None else dfcom["genero"]
        dfcom["quantidade_loco"] = int(quantidade) if quantidade != None else dfcom["quantidade_loco"]
        dfcom["quantidade_cliente"] = 0
        dfcom["autor"] = autor if autor != None else dfcom["autor"]
        dfcom["ano"] = int(ano) if ano != None else dfcom["ano"]
        dfcom["edicao"] = edicao if edicao != None else dfcom["edicao"]
        dfcom["paginas"] = int(paginas) if paginas != None else dfcom["paginas"]

        add = dfcom

    else:

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



def alugar(
    id = None,
    nome = None,
    genero = None,
    quantidade = None,
    autor = None,
    ano = None,
    edicao = None,
    paginas = None):

    import pandas as pd

    df = pd.read_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";")

    df = df[df['id'] != int(id)]
    dfcom = df[df['id'] == int(id)]

    dfcom["id"] = int(id) if id != None else dfcom["id"]
    dfcom["nome"] = nome if nome != None else dfcom["nome"]
    dfcom["genero"] = genero if genero != None else dfcom["genero"]
    dfcom["quantidade_loco"] = int(list(dfcom["quantidade_loco"])[0]) - 1
    dfcom["quantidade_cliente"] = int(list(dfcom["quantidade_cliente"])[0]) + 1
    dfcom["autor"] = autor if autor != None else dfcom["autor"]
    dfcom["ano"] = int(ano) if ano != None else dfcom["ano"]
    dfcom["edicao"] = edicao if edicao != None else dfcom["edicao"]
    dfcom["paginas"] = int(paginas) if paginas != None else dfcom["paginas"]

    df = pd.concat([df, dfcom])

    df = df.sort_values(by=['id'])

    df.to_csv("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros.csv", ";", index=False)
