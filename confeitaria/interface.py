from datetime import date
from produtos import (
    BoloCaseiro, 
    BoloDePote, 
    FatiaDeBolo, 
    Brownie, 
    PaoDeQueijo, 
    Pudim, 
    Embalagem
)

from acoes_produto import (
    cadastrar_produto, 
    listar_produtos,
    buscar_produto,
    adicionar_ao_estoque,
    remover_do_estoque,
    gerar_relatorio,
)

def exibir_menu():
    print("\n===== Menu de Gerenciamento =====")
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Buscar Produto")
    print("4 - Adicionar ao Estoque")
    print("5 - Remover do Estoque")
    print("6 - Gerar Relatório")
    print("7 - Sair")
    print("===================================")

def main():
    produtos = [
        # Bolos Caseiros
        BoloCaseiro(1, "Bolo", "Bolo de Aipim", "Massa de aipim, topo com coco ralado.", "Unidade", 10, date(2024, 1, 15), "Aipim com coco"),
        BoloCaseiro(2, "Bolo", "Bolo de Limão Siciliano", "Massa de limão siciliano, cobertura de mousse de limão siciliano.", "Unidade", 5, date(2024, 1, 10), "Limão siciliano"),
        BoloCaseiro(3, "Bolo", "Bolo de laranja", "Massa de laranja, topo com calda de laranja e laranjas caramelizadas.", "Unidade", 12, date(2024, 1, 20), "Laranja"),
        # Bolos de Pote
        BoloDePote(4, "Bolo de Pote", "Bolo de Pote Sensação", "Massa branca, recheado com camadas de creme de chocolate, brownie, mousse de morango, biscoiro, creme de chocolate e mousse de morango.", "Unidade", 8, date(2024, 1, 12), "Morango"),
        BoloDePote(5, "Bolo de Pote", "Bolo de Pote de Chocolate", "Massa se chocolate, recheado com camadas de ganache de chocolate, chantilly de chocolate e brigadeiro.", "Unidade", 10, date(2024, 1, 18), "Chocolate"),
        BoloDePote(6, "Bolo de Pote", "Bolo de Pote de Ninho", "Massa branca, recheado com camadas de nutella e mousse de leite em pó.", "Unidade", 7, date(2024, 1, 14), "Ninho"),
        # Fatias de Bolo
        FatiaDeBolo(7, "Fatia de Bolo", "Fatia de Maracujá e Chocolate", "Massa de cacau, 2 camadas de recheio creme de chocolate e 1 camada de mousse de maracujá.", "Unidade", 15, date(2024, 1, 11), "Maracujá com chocolate"),
        FatiaDeBolo(8, "Fatia de Bolo", "Fatia de Bolo de Cenoura", "Fatia de bolo de cenoura, recheada com 2 camadas de creme de chocolate.", "Unidade", 12, date(2024, 1, 13), "Cenoura"),
        FatiaDeBolo(9, "Fatia de Bolo", "Redvelvet", "Massa redvevelt, recheada com 2 camadas de creamcheese e 1 camada de gelia de frutas vemelhas.", "Unidade", 10, date(2024, 1, 16), "Redvevelt"),
        # Brownies
        Brownie(10, "Brownie", "Brownie Tradicional", "Massa de cacau.", "Unidade", 20, date(2024, 1, 22), "chocolate"),
        Brownie(11, "Brownie", "Brownie com Chocolate Branco", "Massa de cacau, com gotas de chocolate branco.", "Unidade", 18, date(2024, 1, 25), "chocolate branco"),
        Brownie(12, "Brownie", "Brownie com Doce de Leite", "Massa redvelvet, com recheio cremoso de doce de leite.", "Unidade", 15, date(2024, 1, 28),"chocolate branco"),
        # Pães de Queijo Congelados
        PaoDeQueijo(13, "Pão de Queijo", "Pão de Queijo Tradicional", "Pão de queijo tradicional congelado.", "Pacote", 30, date(2024, 2, 10), True),
        PaoDeQueijo(14, "Pão de Queijo", "Pão de Queijo Recheado", "Pão de queijo congelado recheado com goiabada.", "Pacote", 25, date(2024, 2, 15), True),
        # Pudins
        Pudim(15, "Pudim", "Pudim de Leite Condensado", "Pudim tradicional grande de leite condensado.", "Unidade", 10, date(2024, 1, 8), "Leite"),
        # Embalagens
        Embalagem(16, "Embalagem", "Caixa para Bolo", "Caixa de papelão para bolo.", "Unidade", 50, "Papelão", "20x20x10", date(2030, 2, 11), ""),
        Embalagem(17, "Embalagem", "Pote para Bolo de Pote", "Pote de plástico reutilizável.", "Unidade", 45, "Plástico", "250ml", date(2028, 1, 4), ""),
        Embalagem(18, "Embalagem", "Saco para Pão de Queijo", "Saco plástico transparente.", "Unidade", 150, "Plástico", "20x30", date(2029, 4, 12), ""),
    ]

    while True:
        exibir_menu()  # Exibe o menu
        opcao = input("\nEscolha uma opção: ")  # Captura a opção do usuário

        if opcao == "1":
            cadastrar_produto(produtos)  # Chama a função para cadastrar produto
        elif opcao == "2":
            listar_produtos(produtos)  # Chama a função para listar produtos
        elif opcao == "3":
            buscar_produto(produtos)  # Chama a função para buscar produto
        elif opcao == "4":
            adicionar_ao_estoque(produtos)  # Chama a função para adicionar ao estoque
        elif opcao == "5":
            remover_do_estoque(produtos)  # Chama a função para remover do estoque
        elif opcao == "6":
            gerar_relatorio(produtos)  # Chama a função para gerar relatório
        elif opcao == "7":
            print("Saindo...")  # Mensagem de saída
            break  # Encerra o loop e o programa
        else:
            print("Opção inválida! Tente novamente.")  # Caso a opção seja inválida
