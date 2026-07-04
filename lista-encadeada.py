lista = {
    'valor': 4,
    'proximo': None
}

print(lista)

# novo = {
#     'valor': 8,
#     'proximo': None
# }

# lista['proximo'] = novo
# print(lista)

def exibeLista():
    if not lista:
        print('Lista Vazia')
        return
    elemento = lista

    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']
    
    print('.')

def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = {'valor': elemento, 'proximo': None}
        return
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = {'valor': elemento, 'proximo': None}


print('Adicionando o 5...')
adicionaNoFim(5)
exibeLista()
print('Adicionando o 14...')
adicionaNoFim(14)
exibeLista()
print('Adicionando o 25...')
adicionaNoFim(25)
exibeLista()
print(lista)