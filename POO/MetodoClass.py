from random import randint


class Pessoa:
    
    ano_atual = 2022
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nas(self):
        print(self.ano_atual - self.idade)
        
    
    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)
    
    @staticmethod
    def gera_Id():
        rand = randint(10000, 19999)
        return rand
    
    
    
# main   
#p1 = Pessoa.por_ano_nasc('Léo', 1985)
p1 = Pessoa('Léo', 35)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nas()
print(Pessoa.gera_Id())
print(p1.gera_Id())
