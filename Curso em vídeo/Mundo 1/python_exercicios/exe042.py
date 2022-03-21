'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

# Analisando triângulos e dizendo quais seus tipos

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input("Terceiro segmento: "))

# Verificando se forman um triângulo
if r1 < r2 + r3 and r2< r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')            
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
    
