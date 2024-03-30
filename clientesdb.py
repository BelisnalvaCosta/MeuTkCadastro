import sqlite3

# Criando o banco de dados
conexao = sqlite3.connect('clientes.db')

# Criando o cursor
c = conexao.cursor()

# Criando a tabela de clientes
c.execute("""
    CREATE TABLE clientes (
        nome text,
        sobrenome text,
        email text,
        telefone text
    )
""")

# Commit as mudanças
conexao.commit()

# Fechar o banco de dados
conexao.close()

def listar_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()

    for cliente in clientes:
        print(f"Nome: {cliente[0]} {cliente[1]} | E-mail: {cliente[2]} | Telefone: {cliente[3]}")

    # Fechar a conexão
    conexao.close()

