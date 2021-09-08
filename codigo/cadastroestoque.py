from time import sleep 
from operator import itemgetter #para ordenar a lista
deposito = list() 
produto = dict()

print('Controle de estoque')
print('=-'*20)
menu = int(input('Deseja realizar cadastro?    [0 - sair          1 - sim          2 - não] '))

while menu == 1:
    produto['Código'] = int(input('Digite o código de produto para o cadastro: '))
    produto['Estoque'] = int(input('Informe a quantidade existente no estoque: '))
    produto['Mínimo'] = int(input('Informe o estoque mínimo necessário: '))
    deposito.append(produto.copy())     #copiei o produto para adicionar tudo numa lista de dicionário
    menu = int(input('Deseja realizar cadastro?    [0 - sair          1- sim          2 - não:] '))
    if menu == 2:
        deposito_ordenado = sorted(deposito, key=itemgetter('Código')) #para colocar em ordem crescente
        sleep(4) #o sleep foi para dar um realismo no sistema, demorando na resposta.
        print('Carregando dados, aguarde um instante...')
        print('=-'*50)
        print(deposito_ordenado)
        menu = int(input('0 - sair              1 - continuar '))
        if menu == 0:
            sleep(2)
            print('Encerrando o programa...')
if menu == 0:
    sleep(2)
    print('Encerrando o programa...')