'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO'''

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))
média  = (nota_1 + nota_2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota_1, nota_2, média))

if média >= 5 and média <7:
    print('O aluno está em RECUPERAÇÃO!')
elif média < 5:
    print('O aluno está REPROVADO!')
elif média > 7:
    print('O aluno está APROVADO!')
    

#Minha resolução
#Importação de bibliotecas
#from time import sleep

#nota_1 = float(input('Digite a primeira nota: '))
#nota_2 = float(input('Digite a segunda nota: '))
#média = (nota_1 + nota_2) / 2

#print('CALCULANDO A MÉDIA...')
#sleep(3)

#if média < 5.0:
    #print('''Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}
    #O aluno está REPROVADO!'''.format(nota_1, nota_2, média))
#elif média < 5.0 and média > 6.9:
    #print('''Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}
          #O aluno está de RECUPERAÇÃO!'''.format(nota_1, nota_2, média))
#elif média > 7.0:
      #print('''Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}
             #O aluno está de APROVADO!'''.format(nota_1, nota_2, média))

