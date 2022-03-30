# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0
for contador in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(contador)))
    if num % 2 == 0:
        soma = soma + num
        contador = contador + 1
print('Você informou {} números PARES e a soma foi {}'.format(contador, soma))

