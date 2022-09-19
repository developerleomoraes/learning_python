''' Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
    o primeiro que indique o n a calcular e outro chamado show, que será
    um valor lógico (opcional) indicando se será mostrado ou não na tela 
    o processo de cálculo do fatorial.'''

# Functions
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número

    Args:
        n (int): O valor a ser calculado
        show (bool, optional): Mostra ou não a conta

    Returns:
        Int: O valor de Fatorial de um número n
    """
    fat = 1
    for cont in range(n, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat = fat * cont
    return fat

# Main
print(fatorial(5, show=True))
help(fatorial)
