class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
    def mostrar_saldo(self):
        print("Saldo de:", self.__saldo)
    def mostrarTitular(self):
        print("Correntista: ", self.__titular)
conta = ContaBancaria("Maria")
conta.depositar(2699)
conta.sacar(1588)
conta.mostrar_saldo()
conta.mostrarTitular()