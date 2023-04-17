class Vendedor():
    
    def __init__(self,nome_vendedor,vendas):
        self.vendedor=nome_vendedor
        self.vendas=vendas
        self.meta=500
        self.bonus=0
        
    def vendeu(self, quantidade_vendas):
        self.vendas=quantidade_vendas
        self.calcula_bonus()
        
    def calcula_bonus(self):
        if self.vendas > self.meta:
            self.bonus=30
        else:
            self.bonus=0