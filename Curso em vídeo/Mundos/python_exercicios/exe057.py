'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

# Variável
sexo = input('Informe o seu sexo [M/F/NB]: ').strip().upper()[0]

# Sistema de validação
while sexo not in 'MFNBmfnb':
    sexo = input('Dados inválidos, por favor informe seu sexo: ').strip().upper()[0]
print('Sexo {} registrado com suscesso!'.format(sexo))

