from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone=telefone
        self.cnpj=cnpj
        self.numero=numero
        self.clientes=[]
        self.caixa=0
        self.emprestimos=[]

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nivel recomendado. Caixa Atual: {self.caixa}.')
        else:
            print(f'O valor de caixa está ok. Caixa Atual: {self.caixa}.')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não é possível. Dinheiro não disponível no caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000) # chama o método __init__ da super classe agência
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self,valor):
        self.caixa += valor
        self.caixa_paypal -= valor

class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa=1000000

class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa=10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio) #aplico o método da classe superior
        else:
            print('O Cliente não tem o património mínimo necessário.')



if __name__ =='__main__':

# programa
    agencia1=Agencia(227810308, 123456789, 4560)
    AgenciaPremium
    agencia1.verificar_caixa()

    agencia1.emprestar_dinheiro(1500, 9873654321, 0.02)
    print(agencia1.emprestimos)

    agencia1.adicionar_cliente('Daniel', 220954771, 50000)

    print(agencia1.clientes)

    print('-'*20)
    agencia_virtual = AgenciaVirtual('www.agenciavirtual.pt',2224444, 123456789)


    agencia_virtual.verificar_caixa()

    print(agencia_virtual.__dict__)

    print('-'*20)

    agencia_comum1 = AgenciaComum(220954771, 2500000)

    agencia_comum1.verificar_caixa()
    print(agencia_comum1.__dict__)

    print('-'*20)

    agencia_premium1=AgenciaPremium(123456789, 3500000)

    print(agencia_premium1.__dict__)

    print('-'*20)

    agencia_virtual.verificar_caixa()
    agencia_virtual.depositar_paypal(20000)
    print(agencia_virtual.caixa)
    print(agencia_virtual.caixa_paypal)

    agencia_premium1.adicionar_cliente('Daniel', 152023654,10000)
    print(agencia_premium1.clientes)

    agencia_premium1.adicionar_cliente('Pai_Daniel', 777888999,5000000000)
    print(agencia_premium1.clientes)