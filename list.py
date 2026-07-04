# lista = [1,2,3,4,5,6,7,8,9]
# lista.append(4)
# list.pop(0)

def criaFila():
    return[]

def insereNaFila(fila, elemento):
    fila.append(elemento)

def removeDaFila(fila):
    return fila.pop(0)

fila = criaFila()
print(fila)
insereNaFila(fila, 8)
insereNaFila(fila, 3)
insereNaFila(fila, 4)
insereNaFila(fila, 5)
print(f'Removendo: {removeDaFila(fila)}')
print(fila)

