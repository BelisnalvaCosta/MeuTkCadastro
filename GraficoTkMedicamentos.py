# Criando Janela:
import sqlite3

import pandas as pd
import tkinter as tk

janela = tk.Tk()
janela.title('Cadastrar medicamentos')
janela.geometry("330x350")


def cadastrar_medicamentos():
    conexao = sqlite3.connect('medicamentos.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("INSERT INTO medicamentos VALUES (:nome,:conteudo,:tipo,:validade,:prescricao)",
              {
                  'nome': entry_nome.get(),
                  'conteudo': entry_conteudo.get(),
                  'tipo': entry_tipo.get(),
                  'validade': entry_validade.get(),
                  'prescricao': entry_prescricao.get()
              })

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()

    # #Apaga os valores das caixas de entrada
    entry_nome.delete(0, "end")
    entry_conteudo.delete(0, "end")
    entry_tipo.delete(0, "end")
    entry_validade.delete(0, "end")
    entry_prescricao.delete(0, "end")


def exporta_medicamentos():
    conexao = sqlite3.connect('medicamentos.db')
    c = conexao.cursor()

    # Inserir dados na tabela:
    c.execute("SELECT *, oid FROM medicamentos")
    medicamentos_cadastrados = c.fetchall()
    # print(medicamentos_cadastrados)
    medicamentos_cadastrados = pd.DataFrame(medicamentos_cadastrados,
                                        columns=['nome', 'conteudo', 'tipo', 'validade', 'prescricao', 'Id_banco'])
    medicamentos_cadastrados.to_excel('medicamentos.xlsx')

    # Commit as mudanças:
    conexao.commit()

    # Fechar o banco de dados:
    conexao.close()


# Rótulos Entradas:
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_conteudo = tk.Label(janela, text='Conteúdo')
label_conteudo.grid(row=1, column=0, padx=10, pady=10)

label_tipo = tk.Label(janela, text='Tipo')
label_tipo.grid(row=2, column=0, padx=10, pady=10)

label_validade = tk.Label(janela, text='Validade')
label_validade.grid(row=3, column=0, padx=10, pady=10)

label_prescricao = tk.Label(janela, text='Prescrição')
label_prescricao.grid(row=3, column=0, padx=10, pady=10)

# Caixas Entradas:
entry_nome = tk.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_conteudo = tk.Entry(janela, width=35)
entry_conteudo.grid(row=1, column=1, padx=10, pady=10)

entry_tipo = tk.Entry(janela, width=35)
entry_tipo.grid(row=2, column=1, padx=10, pady=10)

entry_validade = tk.Entry(janela, width=35)
entry_validade.grid(row=3, column=1, padx=10, pady=10)

entry_prescricao = tk.Entry(janela, width=35)
entry_prescricao.grid(row=3, column=1, padx=10, pady=10)

# Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar medicamentos', command=cadastrar_medicamentos)
botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

# Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_medicamentos)
botao_exportar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)

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
janela.title('Cadastrar de medicamentos')
