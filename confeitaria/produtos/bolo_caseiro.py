from confeitaria.produtos.bolo import Bolo
from datetime import date

class BoloCaseiro(Bolo):
    def __init__(self, codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque, data_validade, sabor):
        super().__init__(codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque, data_validade, sabor)