def desfazer_tarefa(tarefas):
    try:
        resposta = ('Você desfez sua ultima tarefa.', tarefas.pop())
    except IndexError as erro:
        print('Você não tem mais tarefas para serem desfeitas')
        resposta = erro

    return resposta, ('sua lista atualizada:', tarefas)

def refazer_tarefa(tarefas, tarefas_historico):
    try:
        pegando_ultimo = tarefas_historico[-1]
        tarefas.append(pegando_ultimo)
        print('Voce refez sua tarefa')
        resp = tarefas
    except IndexError as erro:
        print('Você não pode refazer, pois a lista está sem tarefas')
        resp = erro

    return resp

tarefas = []
tarefas_historico = []

while True:
    decisao = input('Qual função deseja: Listar ("l"), desfazer ultima tarefa ("u"), Refazer ultima ação ("r") ou se quiser add uma nova, apenas digite:')
    if decisao == 'l':
        print(list([listagem for listagem in tarefas]))
    elif decisao == 'u':
        print(desfazer_tarefa(tarefas))
    elif decisao == 'r':
        print(refazer_tarefa(tarefas, tarefas_historico))
    else:
        tarefas.append(decisao)
        tarefas_historico.append(decisao)
        print('Nova Tarefa adicionada com sucesso!')
        pass


"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""


def show_op(todo_list):
    print()
    print('Tarefas: ')
    print(todo_list)
    print()


def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Nada a desfazer')
        return

    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Nada a refazer')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Digite uma tarefa ou undo, redo, ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)


