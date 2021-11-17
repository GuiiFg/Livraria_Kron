
def Get_multas(nick):
    from . import conn as Connet_db

    import pandas as pd

    df = Connet_db.Query_multas(
        f"SELECT * FROM Multas_tb WHERE cliente = '{nick}'")

    return df
