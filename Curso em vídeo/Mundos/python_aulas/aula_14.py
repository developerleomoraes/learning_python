# Estudando o while

número = 1
par = 0
impar = 0
while número != 0:
    número = int(input('Digite um valor: '))
    if número != 0:
        if número % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
    
print('Você digitou {} pares e {} números impares'.format(par, impar))
