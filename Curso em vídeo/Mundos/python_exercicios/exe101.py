''' Crie um programa que tenha uma função chamada voto()
    que vai receber como parâmetro o ano de nascimento de uma pessoa,
    retornando um valor literal indicando se uma pessoa tem voto
    NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''


# Funções

def voto(ano):
    from datetime import date
    
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO É OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO É OBRIGATÓRIO'
    
    
# Main

nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))

