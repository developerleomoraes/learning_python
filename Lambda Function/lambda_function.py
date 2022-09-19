# Estudando a expressão lambda

''' Digamos que você está avaliando o preço de um serviço e quer saber 
    quanto de imposto será cobrado sobre o serviço. O imposto é correspondente
    a 30% do valor do produto'''

preco = 1000

#def calcular_imposto(preco):
#   return preco * 0.3

#print(calcular_imposto(preco))



#calcular_imposto2 = lambda x: x * 0.3

#print(calcular_imposto2(preco))

precos = [100, 500, 10, 25]

impostos = list(map(lambda x: x * 0.3, precos))

print(impostos)
