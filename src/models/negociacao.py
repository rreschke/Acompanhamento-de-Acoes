from datetime import datetime


class Negociacao:
    id: str
    id_ativo: int
    direcao: str
    observacao: str
    data: datetime
    preco_unit: float
    quantidade: float

    def __init__(self, id, id_ativo,
                       direcao, observacao,
                       data, preco_unit, quantidade):
        self.id = id
        self.id_ativo = id_ativo
        self.direcao = direcao
        self.observacao = observacao
        self.data = data
        self.preco_unit = preco_unit
        self.quantidade = quantidade

    def get_total_price(self):
        return self.preco_unit * self.quantidade
    