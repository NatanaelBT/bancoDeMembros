def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO: Nada digitado.\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    txt = txt.upper()
    print(linha())
    print(f'\033[33m{txt.center(42)}\033[m')
    print(linha())


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}'.upper())
        c += 1
    print(linha())
    opcao = leiaInt('Sua Opção: ')
    return opcao


