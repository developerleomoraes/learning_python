# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for

# Tabuada de um número

num = int(input('Digite um número para ver sua tabauda: '))
for cont in range(1, 11):
    print('{} x {:2} = {}'.format(num, cont, num*cont))
