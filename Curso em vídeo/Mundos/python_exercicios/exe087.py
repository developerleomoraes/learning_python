''' Aprimore o desafio anterior, mostrando no final:      
    A) A soma de todos os valores pares digitados.                                                 
    B) A soma dos valores da terceira coluna.                                 
    C) O maior valor da segunda linha.'''

# Colocando os valores dentro da matriz
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
maior = 0
soma_coluna = 0


for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-' * 30)      
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
        # Resolvendo a letra A
        if matriz[linha][coluna] % 2 == 0:
            soma_pares = soma_pares + matriz[linha][coluna]
    print()

print('-' *30)
print(f'A soma dos valores pares é {soma_pares}')

# Resolvendo a letra B
for linha in range(0, 3):
    soma_coluna = soma_coluna + matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna}')

#Rsolvendo a letra C
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')

