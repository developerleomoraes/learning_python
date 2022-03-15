# Nessa aula, vamos aprender operações com String no Python. 
# As principais operações que vamos aprender são o Fatiamento de String, 
# Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join()

# Fatiamento
'''frase = ('Curso em vídeo python ')
print(frase[9::3])'''

# Análise
#frase = ('Curso em vídeo python')

#len(frase)
#frase.count('o', 0, 13)

#frase.find('Android')
#'Curso' in frase


# Transformação
#frase = 'Curso em vídeo Python'
#print(frase.replace('Python', 'Android'))
#print(frase.upper())
#print(frase.lower())
#print(frase.capitalize())
#print(frase.title())

#frase = 'Curso em vídeo'

'''frase.strip()
frase.rstrip()
frase.lstrip()'''

# Divide a cadeia de palavras em listas e cada cadeia de caracteres se torna uma string dentro da lista
#frase.split()
#'-'.join(frase)


frase = 'Curso em Vídeo Python'

dividido = frase.split()
print(dividido[0])


