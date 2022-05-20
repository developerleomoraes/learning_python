'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os
valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''

#Criando uma lista onde serão armazenados vários valores

valores_total = []
ímpares       = []
pares         = []


while True:
    valores_total.append(int(input('Digite um valor: ')))
    resposta = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resposta in 'N':
        break
    
#for valor in valores_total:
for indice, valor in enumerate(valores_total):
    if valor %2 == 0:
        pares.append(valor)
        pares.sort()
    else:
        ímpares.append(valor)
        ímpares.sort()
      
        
print(f'Os valores totais digitados foram {valores_total}!')
print(f'Os valores ímpares foram {pares}!')
print(f'Os valores ímpares foram {ímpares}!')
