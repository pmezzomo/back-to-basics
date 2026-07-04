nomes = [
    'Joao',
    'Antonio',
    'Maria',
    'Ana',
    'Anacleto',
    'Bianca',
    'Fernando',
    'Andre'
]

tabela = {} 

for nome in nomes:
    # qtd = len(nome)
    qtd = nome[0]
    if qtd not in tabela:
        tabela[qtd] = []
    tabela[qtd].append(nome)

print(tabela)


