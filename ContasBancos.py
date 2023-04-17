from datetime import datetime
import pytz
import time
from random import randint


class ContaCorrente:
    """
    Cria um objeto de ContaCorrente para gerir as contas dos clientes.

    Atributos:
        nome(string): Nome do cliente
        cpf(string): CPF do cliente. Deve ser inserido com pontos e traços
        agencia: Agência responsável pela conta do cliente
        num_conta: Número de conta corrente do cliente
        transacoes: histórico de transações do cliente
    """

    @staticmethod #método estático -> não depende de nenhuma informação da classe
    def _data_hora():
        fuso_PT= pytz.timezone('Portugal')
        horario_PT=datetime.now(fuso_PT)
        return horario_PT.strftime("%d/%m/%Y %H:%M:%S")

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia=agencia
        self._num_conta=num_conta
        self._transacoes=[]
        self.cartoes=[]

    def consultar_saldo(self):
        """
        Exibe o saldo atual da conta do cliente.
        Não tem parametros necessários.
        """
        print('O seu saldo atual é R${:,.2f}.'.format(self._saldo))

    def depositar(self,valor):
        self._saldo += valor
        self.consultar_saldo()
        self._transacoes.append((valor, f'Saldo: {self._saldo}', ContaCorrente._data_hora()))

    def _limite_conta(self): #método privado -> começa por underscore (apenas é utilizado na classe)
        self._limite=-1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('Não existe saldo suficiente para levantar R${:,.2f}.'.format(valor))
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, f'Saldo: {self._saldo}', ContaCorrente._data_hora()))

    def consultar_limite(self):
        print('o limite da conta é R${:,.2f}.'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print(f'Histórico de transações {self.nome}:')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)
        print('_' * 20)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, f'Saldo: {self._saldo}', ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, f'Saldo: {conta_destino._saldo}', ContaCorrente._data_hora()))

class CartaoCredito:

    @staticmethod  # método estático -> não depende de nenhuma informação da classe
    def _data_hora():
        fuso_PT = pytz.timezone('Portugal')
        horario_PT = datetime.now(fuso_PT)
        return horario_PT

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000,9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

        @property #método get
        def senha(self):
            return self._senha

        @senha.setter #método set
        def senha(self, valor):
            if len(valor) == 4 and valor.isnumeric():
                self._senha = valor
            else:
                print('Nova senha inválida')

