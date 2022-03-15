'''Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.'''

nome = input('Qual é o seu nome? ')
if nome == 'Leo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == "Maria" or nome =='Carla':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Cláudia Jéssica Julina':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(nome))
