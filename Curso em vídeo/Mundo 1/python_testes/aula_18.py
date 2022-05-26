# Variáveis compostas

galera = []
dado   = []
total_maior = 0
total_menor = 0

for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade!')
        total_maior = total_maior + 1
    else:
        print(f'{pessoa[0]} é menor de idade!')
        total_menor = total_menor + 1
print(f'Temos {total_maior} maiores e {total_menor} menores de idade')
