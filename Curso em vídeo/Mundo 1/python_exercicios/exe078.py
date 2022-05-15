'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''

maior = 0
menor = 0

valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
            

print('-' * 30)
print(f'Você digitou os valores {valores}')


# Minha resolução
# Criando uma lista que recebe 5 valores do usuário
'''valores = [float(input('Digite um valor: ')),
           float(input('Digite um valor: ')),
           float(input('Digite um valor: ')),
           float(input('Digite um valor: ')),
           float(input('Digite um valor: ')),]'''

# Printando o maior e meno valor usando as funções max e min
'''print(f'\nO maior valor encontrado foi {max(valores)}')
print(f'O menor valor encontrado foi {min(valores)}')'''
