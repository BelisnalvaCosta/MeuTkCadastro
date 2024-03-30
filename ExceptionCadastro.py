from asyncio import SelectorEventLoop
import tkinter as tk
import sqlite3

def cadastrar_cliente():
    try:
        conexao = sqlite3.connect('clientes.db')
        c = conexao.cursor()

        # Inserir dados na tabela
        nome = input_nome.get()
        sobrenome = input_sobrenome.get()
        email = input_email.get()
        telefone = input_telefone.get()

        c.execute("INSERT INTO clientes VALUES (?, ?, ?, ?)",
                  (nome, sobrenome, email, telefone))

        # Commit as mudanças
        conexao.commit()

        # Fechar a conexão
        conexao.close()

        # Fechar a janela
        janela.destroy()

    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")

# Configuração da janela principal
janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry("330x350")

# Campos de entrada
input_nome = tk.Entry(janela)
input_sobrenome = tk.Entry(janela)
input_email = tk.Entry(janela)
input_telefone = tk.Entry(janela)

input_nome.pack()
input_sobrenome.pack()
input_email.pack()
input_telefone.pack()

# Botão para cadastrar cliente
btn_cadastrar = tk.Button(janela, text="Cadastrar Cliente", command=cadastrar_cliente)
btn_cadastrar.pack()

# Exception
class ExceptionCadastro(Exception):
    def TextError(Self, TextError):
        try:
            TextError = str(input("Digite os dados: "))
            TextError = str(input("Insira outros dados: "))
            Resultado = print(f"cadastro efetuado com sucesso")
            
        except TextError as e:
            print(f'Erro: Dados incorretos, digite novamente({e.self_text}).')

janela.mainloop()
