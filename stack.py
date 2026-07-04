def criaPilha():
    return[]

def insereNaPilha(pilha, elemento):
    pilha.append(elemento)

def removeDaPilha(pilha):
    return pilha.pop()

fila = criaPilha()
print(fila)
insereNaPilha(fila, 8)
insereNaPilha(fila, 3)
insereNaPilha(fila, 4)
insereNaPilha(fila, 5)
print(f'Removendo: {removeDaPilha(fila)}')
print(fila)

