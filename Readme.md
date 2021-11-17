# Seja Bem vindo a Livraria Kron 📚

## Inspirações e Referências:
- **StotySet**: Imagens/ilustrações;
- **Lisandry Kron**: Idéia inicial e nome do projeto.

### 🗃️ Criamos um ambiente em python na pasta "env" para facilitar quando for rodar o site!

### 🗄️ Nós usamos o MySql!
 - Caso queira montar ele na sua maquina, já deixamos a Query pronto, só da play! 😉

### 📌 Faça bom uso do projeto para o que desejar! ele foi criado para fins educativos!

### 📌 Caso tenha alguma duvida, abra uma Issue ⚠️, será um prazer poder ajudar você!

## Organização

### 🛠️ O projeto fui construido de maneira organizada visando uma fácil compreenção! 

### 📂 env:
- Ambiente virtual do Python, com todos os pacotes que você irá precisar!
  
### 📂 json:
- Arquivo *.json das configurações de acesso ao banco, segue um modelo:

            nome: database_config.json

            content:
            {
                "localhost":{
                    "user": "-nome do usuario do seu banco-" ,
                    "password": "-senha do usuario do seu banco-"
                }
            }

### 📂 libs:
- Libs criadas por nós para ajudar a na manipulção dos dados e o Dao(lib que faz **TODAS** as comunicações com o database)

### 📂 static:
- Arquivos *.css, eles ficam nesta pasta por necessidade do Flask!

### 📂 templates:
- Arquivos *.html, eles ficam nesta pasta por necessidade do Flask!

### 📝 main.py:
- É onde tudo acontece e onde você irá iniciar o projeto!

#### Os arquivos soltos são informações sobre o projeto!