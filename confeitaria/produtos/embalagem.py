from confeitaria.produtos import Produto

class Embalagem(Produto):
    def __init__(self, codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque,material, tamanho, data_validade, sabor):
        super().__init__(codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque, data_validade, sabor)
        self.material = material
        self.tamanho = tamanho