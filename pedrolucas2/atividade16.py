class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = [f"Conta criada com saldo: R$ {saldo_inicial:.2f}"]

    def depositar(self, valor: float):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: +R$ {valor:.2f}")

    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.historico.append(f"Saque: -R$ {valor:.2f}")
            return True
        print("Saldo insuficiente ou valor inválido.")
        return False

    def transferir(self, destino: "ContaBancaria", valor: float):
        if self.sacar(valor):
            destino.depositar(valor)
            self.historico[-1] = f"Transferência enviada para {destino.titular}: -R$ {valor:.2f}"

    def exibir_extrato(self):
        print(f"\n--- Extrato de {self.titular} ---")
        for item in self.historico:
            print(item)
        print(f"Saldo Atual: R$ {self.saldo:.2f}")

c1 = ContaBancaria("Ana", 1000)
c2 = ContaBancaria("Carlos", 200)
c1.transferir(c2, 350)
c1.exibir_extrato()