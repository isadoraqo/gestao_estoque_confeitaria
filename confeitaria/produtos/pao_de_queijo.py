from datetime import date
from confeitaria.produtos import Produto

class PaoDeQueijo(Produto):
    def __init__(self, codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque, data_validade, congelado):
        super().__init__(codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque,data_validade, congelado)
        self.congelado = congelado
        