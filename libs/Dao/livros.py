
def get_livros ():

    from . import conn as Connet_db

    import pandas as pd

    df = Connet_db.Query_livros("SELECT * FROM Livros_tb")

    return df

def modificar_livros(
    id = None,
    nome = None,
    genero = None,
    quantidade = None,
    autor = None,
    ano = None,
    edicao = None,
    paginas = None):

    print("entrei")

    from . import conn as Connect_db

    query = "UPDATE Livros_tb SET "

    if nome != '':
        query += f" nome='{nome}'"
    
    if genero != '':
        query += f", genero='{genero}'"

    if quantidade != '':
        query += f", quantidade_loco='{quantidade}'"

    if autor != '':
        query += f", autor='{autor}'"

    if edicao != '':
        query += f", edicao='{edicao}'"

    if ano != '':
        query += f", ano='{ano}'"

    if paginas != '':
        query += f", paginas='{paginas}'"

    query += f" WHERE id = {int(id)}"


    print(query)

    Connect_db.Insert_livros(query)

    


def Registrar_livros(
    nome = None,
    genero = None,
    quantidade = None,
    autor = None,
    ano = None,
    edicao = None,
    paginas = None):

    from . import conn as Connect_db
    
    query = f"""
    INSERT INTO Livros_tb(nome, genero, quantidade_loco, quantidade_cliente, autor, ano, edicao, paginas) VALUES(
    	'{nome}',
        '{genero}',
        '{quantidade}',
        0,
        '{autor}',
        '{ano}',
        '{edicao}',
        '{paginas}'
    );
    """

    Connect_db.Insert_livros(query)


def excluir(
    id):

    from . import conn as Connect_db
    
    query = f"""
    DELETE FROM Livros_tb WHERE id = {int(id)};
    """

    Connect_db.Insert_livros(query)



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
