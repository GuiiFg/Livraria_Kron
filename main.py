from os import access
from flask import Flask, render_template, redirect, request
from flask_cors import CORS


from libs import Sessao
from libs import Dao
from libs import Produtos

sessao = Sessao.Nova_sessao()

app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def index():
    if sessao.is_loged == True:
        return redirect("/homepage") 
    else:
        return render_template("index.html")


@app.route("/homepage")
def homepage():
    if sessao.is_loged == True: 
        livros = Dao.Get_livros()

        if sessao.filtro != "":
            import pandas as pd

            livros = livros[[sessao.filtro in x for x in livros['nome']]]            

        lista_livros = [ Produtos.Livro(
            id = row.id,
            nome = row.nome, 
            genero = row.genero,
            quantidade_loco = row.quantidade_loco,
            quantidade_cliente = row.quantidade_cliente,
            autor = row.autor,
            ano = row.ano,
            edicao = row.edicao,
            paginas = row.paginas
        ) for index, row in livros.iterrows()]

        return render_template("homepage.html", tipo_acesso = int(sessao.tipo_usuario), listadelivros = lista_livros,
        texto_filtro = sessao.filtro)
    else:
        return redirect("/")


@app.route("/gerenciar")
def gerenciar():
    if sessao.is_loged == True: 
        return render_template("gerenciar.html", tipo_acesso= int(sessao.tipo_usuario))
    else:
        return redirect("/")

@app.route("/alugar")
def alugar():
    if sessao.is_loged == True: 
        return render_template("alugar.html", tipo_acesso= int(sessao.tipo_usuario))
    else:
        return redirect("/")

@app.route("/log_out")
def sair():
    
    sessao.Sair()

    return redirect("/")


# ------------- Rotas post
@app.route("/entrar", methods=["POST"])
def entrar():

    user = request.form['user']
    senha = request.form['senha']

    response = Dao.Fazer_login(user, senha)

    if response[0]:
        sessao.is_loged = True
        sessao.tipo_usuario = response[2]
        sessao.usuario_data = response[1]

        return redirect("/homepage")

    else:
        return redirect("/")



@app.route("/modificar_livro", methods=["POST"])
def modificar_livro():
    
    id = request.form['id']
    nome = request.form['nome']
    genero = request.form['genero']
    quantidade = request.form['quantidade']
    autor = request.form['autor']
    ano = request.form['ano']
    edicao = request.form['edicao']
    paginas = request.form['paginas']

    Dao.Modificar_livro(
        id,
        nome,
        genero,
        quantidade,
        autor,
        ano,
        edicao,
        paginas
    )

    return redirect('/gerenciar')

@app.route("/registrar_livro", methods=["POST"])
def registrar_livro():
    
    nome = request.form['nome']
    genero = request.form['genero']
    quantidade = request.form['quantidade']
    autor = request.form['autor']
    ano = request.form['ano']
    edicao = request.form['edicao']
    paginas = request.form['paginas']

    Dao.Registrar_livros(
        nome,
        genero,
        quantidade,
        autor,
        ano,
        edicao,
        paginas
    )

    return redirect('/gerenciar')

@app.route("/excluir-livro", methods=["POST"])
def excluir_livro():
    
    id = request.form['id']

    Dao.Excluir_livro(id)

    return redirect('/gerenciar') 


@app.route("/pesquisar", methods=["POST"])
def pesquisar():
    
    nome = request.form['nome_livro']

    sessao.filtro = nome

    return redirect('/homepage') 



if __name__ == "__main__":

    app.run(debug=True, port=3000)
