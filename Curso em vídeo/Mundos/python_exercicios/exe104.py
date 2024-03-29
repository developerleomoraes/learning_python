''' Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
    'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
    Ex: n = leiaInt('Digite um n: ')'''
    
    
# Criando as funções
def leia_int(msg):
    ok = False
    valor = 0 
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('/033[0;31mERRO! Digite um número inteiro válido/033[0;31m')
        if ok:
            break
    return valor
    

# Main

n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
