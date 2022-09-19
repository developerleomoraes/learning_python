# Aula sobre dicionários

estado = {}
brazil = []
for contador in range(0, 3):
    estado['UF']    = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brazil.append(estado.copy())
for estado in brazil:
    for value in estado.values():
        print(value, end=' ')
    print()
