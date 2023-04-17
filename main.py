from ContasBancos import ContaCorrente, CartaoCredito
from Agencia import AgenciaPremium, AgenciaComum, AgenciaVirtual
import time

#### Programa ####

# conta_daniel=ContaCorrente('Daniel', '111.222.333-45', '1234', '34062')
#
# #print(conta_daniel.saldo)
# #print(conta_daniel.cpf)
#
# #Depositar dinheiro
# conta_daniel.consultar_saldo()
# conta_daniel.depositar(10000)
# #conta_daniel.consultar_saldo()
#
# #Retirar dinheiro
# time.sleep(3)
# conta_daniel.sacar_dinheiro(500)
#
# # Consultar limite
# print('*** Saldo final ***')
# conta_daniel.consultar_saldo()
# conta_daniel.consultar_limite()
#
# print('_'*20)
# conta_daniel.consultar_historico_transacoes()
#
# print('_'*20)
# conta_maeDaniel=ContaCorrente('Teresa', '111.222.333-46', '5555', '656565')
#
# conta_daniel.transferir(1000, conta_maeDaniel)
#
# conta_daniel.consultar_historico_transacoes()
# conta_maeDaniel.consultar_historico_transacoes()
#
# #help(ContaCorrente)
#
# print('_'*20)
# cartao_daniel=CartaoCredito('Daniel', conta_daniel)
#
# print(cartao_daniel.titular) # saber o titular
# print(cartao_daniel.conta_corrente._num_conta) # saber a conta corrente associada ao cartão
#
# print(conta_daniel.cartoes[0].numero) # saber os cartes associados à conta corrente
#
# print(cartao_daniel.validade)
# print(cartao_daniel.cod_seguranca)
#
# print('_'*20)
#
# cartao_daniel.senha='12'
# print(cartao_daniel.senha)
#
# #consultar todos os atributos da classe (método de consulta) -> consulta de todos os elemntos da instâcia
#
# print(conta_daniel.__dict__)
# print(cartao_daniel.__dict__)

if __name__ =='__main__':
    agencia_premium_especial=AgenciaPremium(222333455,11552631)
    print(agencia_premium_especial.__dict__)