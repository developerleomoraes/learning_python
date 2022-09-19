# Class
class Produto:
    def __init__(self, nome, preco):
        self.nome  = nome
        self.preco = preco
        
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        return self.preco
    
    # Getter
    @property
    def nome(self):
        return self._nome
    
    #Setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
        
    
    # Getter
    @property
    def preco(self):
        return self._preco
    
    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))   
        self._preco = valor
        
    

# Main        
produto_1 = Produto('CAMISETA', 50)
produto_1.desconto(30)
print(produto_1.nome, produto_1.preco)

produto_2 = Produto('CANECA', 'R$15')
produto_2.desconto(10)
print(produto_2.nome, produto_2.preco)
