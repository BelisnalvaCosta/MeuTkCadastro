# Função para adicionar medicamento ao estoque
from GraficoTkMedicamentos import cadastrar_medicamentos


def adicionar_medicamentos() -> None:
    nome = input("Digite o nome do medicamento: ")
    cadastrar_medicamentos.append(nome)
    print(f"Medicamento '{nome}' adicionado ao estoque com sucesso!")
    
# Exception

def TextError(Self, TextError):
    try:
        TextError = str(input("Digite os dados: "))
        TextError = str(input("Insira outros dados: "))
        Resultado = print(f"cadastro efetuado com sucesso")
            
    except TextError as e:
        print(f'Erro: Dados incorretos, digite novamente({e.self_text}).')    

# Exemplo de uso da função
adicionar_medicamentos()
