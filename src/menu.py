from src.util.log import Log


class Menu:
    op: int = 999999

    def __init__(self):
        while self.op != 0:
            self.get_option()

    def get_option(self):
        Log.log_date_time(f"Menu exibido")
        print("1. Inserir COMPRA")
        print("2. Inserir VENDA")
        print("3. Cotação de ação")
        print("0. SAIR")

        self.op = int(input("Opção: "))
        Log.log_date_time(f"Opção {self.op}")
