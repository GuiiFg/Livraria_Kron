
def Query_clientes (query:str):
    import pandas as pd
    import mysql.connector

    mydb = mysql.connector.connect( host='localhost',
                                    database='Livraria_Kron',
                                    user='root',
                                    password='Root1234.',
                                    auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()

    mycursor.execute(query)

    myresult = mycursor.fetchall()

    x = pd.DataFrame(myresult)

    map_name = {
        0: "nome",
        1: "nick",
        2: "senha",
        3: "tipo",
    }

    x = x.rename(columns=map_name)

    mydb.close()

    return x

def Query_livros (query:str):
    import pandas as pd
    import mysql.connector

    mydb = mysql.connector.connect( host='localhost',
                                    database='Livraria_Kron',
                                    user='root',
                                    password='Root1234.',
                                    auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()

    mycursor.execute(query)

    myresult = mycursor.fetchall()

    x = pd.DataFrame(myresult)

    map_name = {
        0: "id",
        1: "nome",
        2: "genero",
        3: "quantidade_loco",
        4: "quantidade_cliente",
        5: "autor",
        6: "ano",
        7: "edicao",
        8: "paginas",
    }

    x = x.rename(columns=map_name)

    mydb.close()

    return x



def Insert_livros (query:str):
    import pandas as pd
    import mysql.connector

    mydb = mysql.connector.connect( host='localhost',
                                    database='Livraria_Kron',
                                    user='root',
                                    password='Root1234.',
                                    auth_plugin='mysql_native_password')

    mycursor = mydb.cursor()

    try:
        mycursor.execute(query)

        mydb.commit()

    except:
        mydb.rollback()

    mydb.close()




"""
import pandas as pd


livros = pd.read_excel("C:/Users/Faria/Documents/Estudos/Livraria Kron/database/livros_list.xlsx")


for index, row in livros.iterrows():

    query = f"
    INSERT INTO Livros_tb(nome, genero, quantidade_loco, quantidade_cliente, autor, ano, edicao, paginas) VALUES(
    	'{row.nome}',
        '{row.genero}',
        8,
        0,
        '{row.autor}',
        '{row.ano}',
        '{row.edicao}',
        '{row.paginas}'
    );
    "

    print(query)

    Insert_livros(query)"""
