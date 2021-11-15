
lista = [None, 1, 2, 3, None]

for x in lista:
    id = x

    var = int(id) if id != None else True

    print(f"---------------- {var}")