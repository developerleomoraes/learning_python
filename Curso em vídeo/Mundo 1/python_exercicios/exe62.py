# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


# Enunciado
print('<<< GERADOR DE PA >>>')
print('-=' * 12)

# Variáveis
primeiro_num = int(input('Digite o primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro_num
contador = 1
total = 0
mais = 10

# Programa em si
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razão
        contador = contador + 1
    print('PAUSA')

    mais = int(input('Quantos termos vocês quer mostrar a mais? '))
print('FIM')
print('Progessão finalizada com {} termos msotrados'.format(total))
