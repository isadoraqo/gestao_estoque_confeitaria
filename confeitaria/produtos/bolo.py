from confeitaria.produtos import Produto

class Bolo(Produto):
    def __init__(self, codigo, tipo_produto,  nome, descricao, unidade_medida, quantidade_estoque, data_validade, sabor):
        super().__init__(codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque, data_validade, sabor)