import sqlite3

# Criando o banco de dados
conexao = sqlite3.connect('medicamentos.db')

# Criando o cursor
c = conexao.cursor()

# Criando a tabela de medicamentos
c.execute("""
    CREATE TABLE medicamentos (
        nome text,
        conteudo tex,
        tipo text,
        validade date,
        prescricao text
    )
""")

# Commit as mudanças
conexao.commit()

# Fechar o banco de dados
conexao.close()

def listar_medicamentos():
    conexao = sqlite3.connect('medicamentos.db')
    c = conexao.cursor()

    c.execute("SELECT * FROM medicamentos")
    medicamentos = c.fetchall()

    for medicamentos in medicamentos:
        print(f"Nome: {medicamentos[0]} {medicamentos[1]} | Conteudo: {medicamentos[2]} | Tipo: {medicamentos[3]} | Validade: {medicamentos[4]} | Prescrição: {medicamentos[5]}")

    # Fechar a conexão
    conexao.close()
