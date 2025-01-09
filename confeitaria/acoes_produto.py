from datetime import date
from confeitaria.produtos import (
    BoloCaseiro,
    BoloDePote,
    FatiaDeBolo,
    Brownie,
    PaoDeQueijo,
    Pudim,
    Embalagem
)

def cadastrar_produto(produtos):
    """Função para cadastrar um novo produto no estoque."""
    print("\n===== Cadastro de Produto =====")
    
    while True:
        categoria = input("Digite a categoria do produto (ex: bolo caseiro, bolo de pote, fatia de bolo, etc): ")
        if categoria.lower() not in ["bolo caseiro", "bolo de pote", "fatia de bolo", "brownie", "pão de queijo", "pudim", "embalagem"]:
            print("Categoria inválida. Tente novamente.")
            continue 
        try:
            quantidade = int(input("Digite a quantidade inicial em estoque: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa. Tente novamente.")
                continue
        except ValueError:
            print("Quantidade inválida. Digite um número inteiro. Tente novamente.")
            continue
        
        unidade = input("Digite a unidade de medida (ex: Unidade, Pacote): ")
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        
        while True:
            validade = input("Digite a data de validade (AAAA-MM-DD): ")
            try:
                validade = date.fromisoformat(validade)
                break
            except ValueError:
                print("Data inválida. Tente novamente.")
                continue
        # Instanciação dos produtos por categoria:
        if categoria.lower() == "bolo caseiro":
            produto = BoloCaseiro(len(produtos) + 1, nome, descricao, unidade, quantidade, validade, categoria)
        elif categoria.lower() == "bolo de pote":
            produto = BoloDePote(len(produtos) + 1, nome, descricao, unidade, quantidade, validade, categoria)
        elif categoria.lower() == "fatia de bolo":
            produto = FatiaDeBolo(len(produtos) + 1, nome, descricao, unidade, quantidade, validade, categoria)
        elif categoria.lower() == "brownie":
            produto = Brownie(len(produtos) + 1, nome, descricao, unidade, quantidade, validade)
        elif categoria.lower() == "pão de queijo":
            produto = PaoDeQueijo(len(produtos) + 1, nome, descricao, unidade, quantidade, validade, True)
        elif categoria.lower() == "pudim":
            produto = Pudim(len(produtos) + 1, nome, descricao, unidade, quantidade, validade)
        elif categoria.lower() == "embalagem":
            material = input("Digite o material da embalagem: ")
            tamanho = input("Digite o tamanho da embalagem (ex: 20x20x10): ")
            produto = Embalagem(len(produtos) + 1, nome, descricao, unidade, quantidade, material, tamanho)
        
        produtos.append(produto)  # Adiciona o produto na lista de produtos
        print(f"Produto {nome} cadastrado com sucesso!")
        break  # Sai do loop principal após o cadastro ser concluído



def listar_produtos(produtos):
    """Lista todos os produtos cadastrados no sistema."""
    if not produtos:
        print("\nNenhum produto cadastrado.")
        return

    print("\n===== Lista de Produtos =====")
    for produto in produtos:
        print(f"\n  - {produto.nome} ({produto.tipo_produto})")
        print(f"    - Descrição: {produto.descricao}")
        print(f"    - Quantidade: {produto.quantidade_estoque}")

def buscar_produto(produtos):
    """Busca um produto pelo nome e exibe seus detalhes."""
    codigo = input("Digite o código do produto: ")
    try:
        codigo = int(codigo)
        for produto in produtos:
            if produto.codigo == codigo:
                print(f"\nProduto encontrado: {produto.codigo}")
                print(f"  - {produto.codigo.nome} ({produto.codigo.tipo_produto})")
                print(f"    - Descrição: {produto.codigo.descricao}")
                print(f"    - Quantidade: {produto.codigo.quantidade_estoque}")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("Código inválido.")


def adicionar_ao_estoque(produtos):
    """Função para adicionar unidades a um produto existente no estoque."""
    codigo = input("Digite o código do produto: ")
    try:
        codigo = int(codigo)
        for produto in produtos:
            if produto.codigo == codigo:
                quantidade = int(input("Digite a quantidade a adicionar: "))
                produto.adicionar_estoque(quantidade)
                print(f"\nEstoque do produto '{produto.nome}' atualizado. Novo estoque: {produto.quantidade_estoque}")
                return
        print("\nProduto não encontrado.")
    except ValueError:
        print("\nCódigo ou quantidade inválidos.")

def remover_do_estoque(produtos):
    """Função para remover unidades de um produto existente no estoque."""
    codigo = input("Digite o código do produto: ")
    try:
        codigo = int(codigo)
        for produto in produtos:
            if produto.codigo == codigo:
                quantidade = int(input("Digite a quantidade a remover: "))
                produto.remover_estoque(quantidade)
                print(f"\nEstoque do produto '{produto.nome}' atualizado. Novo estoque: {produto.quantidade_estoque}")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("Código ou quantidade inválidos.")

def gerar_relatorio(produtos):
    """Gera um relatório com a lista de produtos e suas quantidades em estoque."""
    if not produtos:
        print("\nNenhum produto cadastrado em estoque.")
        return

    print("\n===== Relatório de Estoque =====")
    for produto in produtos:
        print(f"- Código: {produto.codigo} - {produto.nome}: {produto.quantidade_estoque} unidades")