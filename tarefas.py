tarefas = []

def adicionaTarefa(tarefa):
   novaTarefa = (tarefa, "pendente")
   tarefas.append(novaTarefa)

def exibeTarefas():
   for tarefa in tarefas:
      print(f'{tarefa[0]} - Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas
    novaLista = []
    for t in tarefas:
        novaLista.append(t if t[0] != tarefa else (tarefa, 'concluída'))
    tarefas = novaLista
       
   
adicionaTarefa('Arrumar a cama')
adicionaTarefa('Lavar a louça')
exibeTarefas()
print('Agora vou concluir...')
concluirTarefa('Arrumar a cama')
exibeTarefas()
