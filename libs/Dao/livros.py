
def get_livros():

    from . import conn as Connect_db

    import pandas as pd

    df = Connect_db.Query_livros("SELECT * FROM Livros_tb")

    return df


def get_livros_alugados(nick):

    from . import conn as Connect_db

    import pandas as pd

    df = Connect_db.Query_alugados(
        f"SELECT * FROM Alugados_tb WHERE cliente = '{nick}'")

    return df


def modificar_livros(
        id=None,
        nome=None,
        genero=None,
        quantidade=None,
        autor=None,
        ano=None,
        edicao=None,
        paginas=None):

    from . import conn as Connect_db

    query_def = "UPDATE Livros_tb SET "
    query = "UPDATE Livros_tb SET "

    mods = [
        [nome, "nome"],
        [genero, "genero"],
        [quantidade, "quantidade_loco"],
        [autor, "autor"],
        [ano, "ano"],
        [edicao, "edicao"],
        [paginas, "paginas"]
    ]

    for x in mods:
        value = x[0]
        name = x[1]

        if value != '':
            if query == query_def:
                query += f" {name}='{value}'"
            else:
                query += f", {name}='{value}'"

    query += f" WHERE id = {int(id)}"

    Connect_db.Insert_livros(query)


def Registrar_livros(
        nome=None,
        genero=None,
        quantidade=None,
        autor=None,
        ano=None,
        edicao=None,
        paginas=None):

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
        ci,
        nick_cliente,
        id_livro,
        data):

    from . import conn as Connect_db

    from datetime import datetime

    df = Connect_db.Query_livros(
        f"SELECT * FROM Livros_tb WHERE id = '{int(id_livro)}'")

    nome_livro = list(df.nome)[0]
    quantidade_loco = list(df.quantidade_loco)[0]
    quantidade_cliente = list(df.quantidade_cliente)[0]

    query = f"UPDATE Livros_tb SET quantidade_loco={int(quantidade_loco) - 1}, quantidade_cliente = {int(quantidade_cliente) + 1} WHERE id = {int(id_livro)}"

    Connect_db.Insert_livros(query)

    now = datetime.now()
    format = "%d/%m/%Y"
    dia_in = now.strftime(format)

    query = f"""INSERT INTO Alugados_tb(ci, cliente, nome_livro, id_livro, dia_in, dia_out ) VALUES(
        '{ci}',
        '{nick_cliente}',
        '{nome_livro}',
        {id_livro},
        '{dia_in}',
        '{data}'
        );"""

    Connect_db.Insert_Alugados(query)


def devolver(
        nick_cliente,
        id_livro):

    from . import conn as Connect_db
    from datetime import datetime

    df_alugados = Connect_db.Query_alugados(
        f"SELECT * FROM Alugados_tb WHERE cliente = '{nick_cliente}' and id_livro = {int(id_livro)}")

    data = list(df_alugados.dia_out)[0]
    format = "%Y-%m-%d"
    dt_devolucao = datetime.strptime(data, format)
    now = datetime.now()

    if dt_devolucao < now:

        diferenca = dt_devolucao - now
        dias = diferenca.days

        valor = dias * - 1

        query = f"""
        INSERT INTO Multas_tb(cliente, valor, pago) VALUES(
            '{nick_cliente}',
            {valor},
            'nao'
        );
        """

        Connect_db.Insert_Multas(query)

    df = Connect_db.Query_livros(
        f"SELECT * FROM Livros_tb WHERE id = '{int(id_livro)}'")

    quantidade_loco = list(df.quantidade_loco)[0]
    quantidade_cliente = list(df.quantidade_cliente)[0]

    query = f"UPDATE Livros_tb SET quantidade_loco={int(quantidade_loco) + 1}, quantidade_cliente = {int(quantidade_cliente) - 1} WHERE id = {int(id_livro)}"

    Connect_db.Insert_livros(query)

    query = f"""
    DELETE FROM Alugados_tb WHERE cliente = '{nick_cliente}' and id_livro = {int(id_livro)};
    """

    Connect_db.Insert_Alugados(query)


"""if nome != '':
        if query == query_def:
            query += f" nome='{nome}'"
        else:
            query += f", nome='{nome}'"
    
    if genero != '':
        if query == query_def:
            query += f" genero='{genero}'"
        else:
            query += f", genero='{genero}'"

    if quantidade != '':
        if query == query_def:
            query += f" quantidade_loco='{quantidade}'"
        else:
            query += f", quantidade_loco='{quantidade}'"

    if autor != '':
        if query == query_def:
            query += f" autor='{autor}'"
        else:
            query += f", autor='{autor}'"

    if edicao != '':
        if query == query_def:
            query += f" edicao='{edicao}'"
        else:
            query += f", edicao='{edicao}'"

    if ano != '':
        if query == query_def:
            query += f" ano='{ano}'"
        else:
            query += f", ano='{ano}'"

    if paginas != '':
        if query == query_def:
            query += f" paginas='{paginas}'"
        else:
            query += f", paginas='{paginas}'" """
