CREATE DATABASE Livraria_Kron;

USE Livraria_Kron;

CREATE TABLE Clientes_tb(
    nome VARCHAR(100) NOT NULL,
    nick VARCHAR(50) NOT NULL PRIMARY KEY, 
    senha VARCHAR(400) NOT NULL,
    tipo ENUM( '0', '1') NOT NULL
);

CREATE TABLE Livros_tb(
	  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    genero VARCHAR (100),
    quantidade_loco INT NOT NULL,
    quantidade_cliente INT NOT NULL,
    autor VARCHAR(100) NOT NULL,
    ano VARCHAR(4),
    edicao VARCHAR(30),
    paginas VARCHAR(40)
);


CREATE TABLE Alugados_tb(
 	  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ci VARCHAR(200) NOT NULL,
    cliente VARCHAR (200),
    nome_livro VARCHAR (200),
    id_livro INT NOT NULL,
    dia_in VARCHAR(10) NOT NULL,
    dia_out VARCHAR(10) NOT NULL
);


CREATE TABLE Multas_tb(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR (200) NOT NULL,
    valor INT NOT NULL,
    pago ENUM('sim', 'nao') NOT NULL
);