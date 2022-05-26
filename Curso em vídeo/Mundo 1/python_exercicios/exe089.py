''' Faça um programa que leia nome e peso de várias pessoas,    
    guardando tudo em uma lista. No final, mostre:     
    A) Quantas pessoas foram cadastradas.            
    B) Uma listagem com as pessoas mais pesadas.    
    C) Uma listagem com as pessoas mais leves.'''
    

#Criando variáveis
cadastro = []
dados_paciente = []
maior = 0
menor = 0

# Laço para captar os dados e manuzea-los entre as listas
while True:
    dados_paciente.append(str(input('Nome: ')))
    dados_paciente.append(float(input('Peso: ')))
    
# Verificando qual o maior e o menor peso
    if len(cadastro) == 0:
        maior = menor = dados_paciente[1]
    else:
        if dados_paciente[1] > maior:
            maior = dados_paciente[1]
        else:
            dados_paciente[1] < menor
            menor = dados_paciente[1]
                
    cadastro.append(dados_paciente[:])
    dados_paciente.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta in 'Nn':
        break



print('-' * 30)
print(f'os dados foram {cadastro}')
print(f'Ao todo foram cadastradas {len(cadastro)} pessoas')
print(f'O maior peso foi de {maior}Kg, e o menor foi de {menor}Kg.')

