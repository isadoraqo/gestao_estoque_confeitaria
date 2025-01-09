from datetime import date

class Produto:
    def __init__(self, codigo, tipo_produto, nome, descricao, unidade_medida, quantidade_estoque, data_validade, sabor):
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.unidade_medida = unidade_medida
        self.quantidade_estoque = quantidade_estoque
        self.sabor = sabor
        self.data_validade = data_validade
        self.tipo_produto = tipo_produto

    def adicionar_estoque(self, quantidade):
        self.quantidade_estoque += quantidade

    def remover_estoque(self, quantidade):
        if self.quantidade_estoque >= quantidade:
            self.quantidade_estoque -= quantidade
        else:
            raise ValueError("Quantidade insuficiente em estoque.")