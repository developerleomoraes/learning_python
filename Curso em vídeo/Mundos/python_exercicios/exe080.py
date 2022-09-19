'''Crie um programa onde o usuário possa digitar cinco valores numéricos 
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''

from turtle import pos

#Criando a lista
lista = []
for c in range(0,5):
    número = int(input('Digite um valor: '))
    
    # Para adicionar no final da lista
    if c == 0:
        lista.append(número)
        print('Primeiro número adicionado na lista')
    elif número > lista[-1]:
        lista.append(número)
        print('Adicionado ao final da lista!')
        
    # Para adicionar no meio da lista
    else:
        posição = 0
        while posição < len(lista):
            if número < lista[posição]:
                lista.insert(posição, número)
                print(f'Adicionado na posição {posição} da lista...')
                break
            posição = posição + 1
        
print('-' * 30)
print(f'Os valores digitados em ordem foram {lista}')
