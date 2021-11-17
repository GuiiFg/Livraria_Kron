
def Get_multas(nick):
    from . import conn as Connet_db

    df = Connet_db.Query_multas(
        f"SELECT * FROM Multas_tb WHERE cliente = '{nick}'")

    return df

def Pagar_multas(id):

    from . import conn as Connet_db

    df = Connet_db.Insert_Multas(
        f"UPDATE Multas_tb SET pago = 'sim' WHERE id = {int(id)}")

    return df