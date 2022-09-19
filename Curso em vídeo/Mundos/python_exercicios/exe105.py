'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
   e vai retornar um dicionário com as seguintes informações:

    – Quantidade de notas                                                                                                                                                 
    – A maior nota                                                                                                                                                               
    – A menor nota                                                                                                                                                             
    – A média da turma                                                                                                                                                    
    – A situação (opcional)'''
    
# Criando a função
def notas(*n, sit=False):
    """
    -> Função para calcular a nota de vários alunos

    Args:
        n: Uma ou mais notas dos alunos (ilimitado)
        sit (bool, optional): Indica se deve ou não adicionar a situação

    Returns: Dicionário com várias informações sobre a situação da turma
        
    """
    r= {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Ok!'
        elif r['Média'] >= 5: 
            r['Situação'] = 'Razoável!'
        else:
            r['Situação'] = 'Ruim!'

    return r



# Main
resposta = notas(9, 5.5, 2.5, 10, 6.5, sit=True)
print(resposta)

help(notas)
