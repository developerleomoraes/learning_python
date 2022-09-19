
# importando biblioteca pessoa
from pessoa import Pessoa

pessoa_1 = Pessoa('Léo', 26)
pessoa_2 = Pessoa('João', 34)

pessoa_1.falar('POO')
pessoa_2.comer('Sorvete')
pessoa_1.comer('Churrasco')

print(pessoa_1.get_ano_nascimento())
