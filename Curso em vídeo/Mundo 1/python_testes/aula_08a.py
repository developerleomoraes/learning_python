#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos 
# import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar 
# vários recursos adicionais nos seus programas utilizando módulos built-in 
# e módulos externos, oferecidos no Pypi.

from math import sqrt, floor

número = int(input('Digite um número: '))
raiz = sqrt(número)
print('A raiz de {} é igual a {:.2f}'.format(número, floor(raiz)))


#from math import sqrt, floor

#num = int(input('Digite um número: '))
#raiz = sqrt(num)
#print('A raiz de um {} é igual a {:.2f}'. format(num, floor(raiz)))




