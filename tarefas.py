import os 

tarefas = []

def adicionaTarefa(tarefa):
   novaTarefa = (tarefa, "pendente")
   tarefas.append(novaTarefa)

def exibeTarefas():
   if not tarefas:
       print('A lista esta vazia')
       return
   for tarefa in tarefas:
      print(f'{tarefa[0]} - Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas
    novaLista = []
    for t in tarefas:
        novaLista.append(t if t[0] != tarefa else (tarefa, 'concluída'))
    tarefas = novaLista

def removerTarefa(tarefa):
    global tarefas
    tarefas = [t for t in tarefas if t[0] != tarefa]

def buscarTarefa(tarefa):
    resultado = [t for t in tarefas if t[0].lower() == tarefa.lower()]
    if resultado:
        for titulo, status in resultado:
            print(f'Encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada: {tarefa}')
    # for t in tarefas:
    #     if t[0] == tarefa:
    #         print(f'Tarefa encontrada: {t[0]} Status: {t[1]}')  
    #         return
    # print(f'Não achei: {tarefa}') 


while True:
    os.system('clear')

    print('Boas vindas ao gerenciador de lista de tarefas')
    print()
    print('O que você quer fazer agora?')
    print('1 - Listar tarefa')
    print('2 - Adicionar Tarefa')
    print('3 - Remover Tarefa')
    print('4 - Marcar Tarefa como Concluida')
    print('5 - Buscar Tarefa')
    print('6 - Sair')
    opcao = int(input('Digite uma opção: '))

    match opcao: 
        case 1:
            exibeTarefas()
        case 2:
            tarefa = input("Digite a tarefa: ")
            adicionaTarefa(tarefa)
        case 3:
            tarefa = input("Digite a tarefa: ")
            removerTarefa(tarefa)
        case 4:
            tarefa = input("Digite a tarefa: ")
            concluirTarefa(tarefa)
        case 5:
            tarefa = input("Digite a tarefa: ")
            buscarTarefa(tarefa)
        case 6:
            break
        case _:
            print('Opçao invalida')
    print()
    input('Pressione ENTER para continuar...')



# adicionaTarefa('Arrumar a cama')
# adicionaTarefa('Lavar a louça')
# exibeTarefas()
# buscarTarefa('limpar o quarto')
# print('Agora vou concluir...')
# concluirTarefa('Arrumar a cama')
# exibeTarefas()
# removerTarefa('Arrumar a cama')
# exibeTarefas()
