class Menu:
    op: int = 999999

    def __call__(self):
        while self.op != 0:
            self.get_option()

    def get_option(self):
        print("1. Inserir COMPRA")
        print("2. Inserir VENDA")
        print("3. Cotação de ação")
        print("0. SAIR")

        self.op = int(input("Opção: "))
