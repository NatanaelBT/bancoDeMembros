from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arquivo = 'bancoDeMembros.txt'

if not (arquivoExiste(arquivo)):
    criarArquivo(arquivo)

cabecalho('SISTEMA DE MEMBROS')
while True:
    respota = menu(['listar membros', 'cadastrar membros', 'sair do sistema'])
    if respota == 1:
        # print('opção 1'.capitalize())
        lerArquivo(arquivo)
    elif respota == 2:
        # print('opção 2'.capitalize())
        cabecalho('novo cadastro')
        nome = str(input('Nome:'.upper())).upper()
        idade = leiaInt('Idade:'.upper())
        cadastrar(arquivo, nome, idade)
    elif respota == 3:
        print('saindo do sistema...'.capitalize())
        sleep(2)
        print('!!Tchau!!')
        break
    else:
        print('\033[31mErro: Digite uma opção válida\033[m')


