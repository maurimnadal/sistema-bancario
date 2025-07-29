    def depositar(saldo, valor):
    if valor < 0:
        raise ValueError("Valor de depósito inválido")
    return saldo + valor
