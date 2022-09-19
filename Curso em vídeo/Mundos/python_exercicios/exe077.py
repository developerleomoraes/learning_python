'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

print('Quais vogais temos nas seguintes palavras?')
palavras = ('Maria', 'Lapis', 'Banana', 'Maça',
         'Carta', 'Caderno', 'Banana', 'Maça',
         'Jose', 'Celular', 'Amanha', 'Maça',
         'Matias', 'Hoje', 'Cerveja', 'Carla',)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
