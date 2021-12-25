class Acao:
    id: int
    ticker: str
    empresa: str
    setor: str
    subsetor: str
    segmento: str
    cnpj: str

    def __init__(self, id, ticker, empresa,
                           setor, subsetor,
                           segmento, cnpj):
        self.id = id
        self.ticker = ticker
        self.empresa = empresa
        self.setor = setor
        self.subsetor = subsetor
        self.segmento = segmento
        self.cnpj = cnpj

    def get_cnpj_string(self):
        c = self.cnpj
        return c[0:2]+"."+c[2:5]+"."+c[5:8]+"/"+c[8:12]+"-"+c[12:14]

