#Realizando um programa que mostra o número inteiro
# e seu sucessor e antecessor

print(' **** Mostrando o sucessor e antecessor do seu número ****\n\n')

numero = int(input('Digite um número: '))
sucessor   = numero + 1
antecessor = numero - 1

print('O seu número é {}, e o sucessor dele é {} e o antecessor {}!'.format(numero, sucessor, antecessor))
