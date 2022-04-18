# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while

# Enunciado
print('<<< GERADOR DE PA >>>')
print('-=' * 12)

# Variáveis
primeiro_num = int(input('Digite o primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro_num
contador = 1

# Programa em si
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razão
    contador = contador + 1
print('FIM')
