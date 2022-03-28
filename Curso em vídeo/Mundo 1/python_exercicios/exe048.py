# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.


soma = 0
num = 0

for cont in range(1, 501, 2):
    if cont % 3 == 0:
        num = num + 1
        soma = soma + cont
print('A soma de todos os {} valores solicitados é {}'.format(num, soma))
