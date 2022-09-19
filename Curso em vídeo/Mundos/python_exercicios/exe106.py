'''
Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''

# global

# importante bibliotecas
from time import sleep

c = ('\033[m',          # 0 - No color
     '\033[0;30;41m',   # 1 - Red
     '\033[0;30;42m',   # 2 - Green
     '\033[0;30;43m',   # 3 - Yellow
     '\033[0;30;44m',   # 4 - Blue
     '\033[0;30;45m',   # 5 - Purple
     '\033[7;30m'       # 6 - White
     )

# Criando Funções
def ajuda(com):
    título(f'Acessando o manual do programa \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)



# Main
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca >'))
    if comando.strip().upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
