# Estudando uma estrutura de parada no python

num = s = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    s = num + s
print(f'A soma vale {s}')




