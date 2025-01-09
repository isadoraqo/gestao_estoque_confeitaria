# Sistema de Gerenciamento de Estoque para Confeitaria

Este projeto implementa um sistema de gerenciamento de estoque para uma confeitaria, utilizando a linguagem de programação Python. O sistema permite cadastrar produtos, listar o estoque, buscar produtos pelo código, adicionar e remover itens do estoque e gerar um relatório com as informações do estoque.

## Objetivo

O objetivo deste projeto é fornecer uma ferramenta simples e eficiente para gerenciar o estoque de uma confeitaria, permitindo que o usuário realize operações básicas de cadastro, consulta e atualização de produtos.

## Funcionalidades

- Cadastrar produtos: Permite cadastrar novos produtos com informações como nome, descrição, unidade de medida, quantidade em estoque e data de validade (para produtos perecíveis).
- Listar produtos: Exibe a lista de todos os produtos cadastrados no sistema, com suas informações detalhadas, como nome, descrição, código, tipo de produto, quantidade em estoque, unidade de medida e data de validade.
- Buscar produto: Permite buscar um produto pelo código e exibir suas informações.
- Adicionar ao estoque: Permite adicionar unidades a um produto existente no estoque.
- Remover do estoque: Permite remover unidades de um produto existente no estoque.
- Gerar relatório: Gera um relatório com a lista de produtos e suas quantidades em estoque.

---

## Estrutura do código

O projeto está organizado da seguinte forma:

```plaintext
├── main.py            # Arquivo principal para executar o programa
├── produtos/          # Pacote para as classes de produtos
│   ├── __init__.py    # Arquivo para inicializar o pacote
│   ├── produto.py     # Classe base Produto
│   ├── alimento.py    # Classe Alimento
│   ├── bolo.py        # Classe Bolo
│   ├── bolo_caseiro.py # Classe BoloCaseiro
│   ├── fatia_de_bolo.py # Classe FatiaDeBolo
│   ├── bolo_de_pote.py # Classe BoloDePote
│   ├── brownie.py     # Classe Brownie
│   ├── pao_de_queijo.py # Classe PaoDeQueijo
│   ├── pudim.py       # Classe Pudim
│   └── embalagem.py   # Classe Embalagem
├── acoes_produto.py   # Arquivo para as funções do menu
└── interface.py       # Arquivo para a interface do terminal
```

- **main.py:** Arquivo principal que executa o programa e inicia a interface do sistema.
- **produtos:** Pacote com as classes que representam os produtos da confeitaria. O arquivo __init__.py inicializa o pacote e permite a importação das classes de produtos.
- **acoes_produto.py:** Arquivo com as funções para manipular os produtos (cadastrar, listar, etc.).
- **interface.py:** Arquivo com a função para exibir o menu e interagir com o usuário no terminal.

---

## Como Rodar o Projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/isadoraqo/gestao_estoque_confeitaria.git
    ```
2. Navegue até o diretório do projeto:
  ```bash
cd gestao_estoque_confeitaria
  ```

3. Execute o arquivo principal main.py:
   ```bash
   python main.py
    ```
---

## Descrição das Classes

### Classe `Produto`

A classe `Produto` representa os itens no estoque da confeitaria. Cada produto tem um conjunto de atributos que descrevem suas características e métodos que permitem gerenciar a quantidade em estoque.

### Atributos:

- **codigo**: Código único do produto, utilizado para identificá-lo de forma única no sistema.
- **tipo_produto**: O tipo do produto (por exemplo, "Bolo", "Brownie", "Pudim").
- **nome**: Nome do produto (por exemplo, "Bolo de Chocolate").
- **descricao**: Descrição detalhada do produto.
- **unidade_medida**: A unidade de medida do produto (por exemplo, "unidade", "kg", "g").
- **quantidade_estoque**: Quantidade atual do produto disponível no estoque.
- **data_validade**: Data de validade do produto.
- **sabor**: Sabor do produto (por exemplo, "Chocolate", "Morango").

### Métodos:

- **adicionar_estoque(quantidade)**: Aumenta a quantidade do produto no estoque em uma quantidade especificada.
- **remover_estoque(quantidade)**: Diminui a quantidade do produto no estoque, desde que haja quantidade suficiente. Caso contrário, levanta um erro (`ValueError`) indicando que não há estoque suficiente.

---

### Classe `AcoesProduto`

A classe `AcoesProduto` contém métodos que realizam ações relacionadas ao gerenciamento dos produtos no estoque, como adicionar ou remover produtos, além de interagir com os dados dos produtos.

### Métodos:

### `cadastrar_produto`: Responsável por cadastrar um novo produto no estoque. Permite ao usuário definir:

- ***Categoria do produto*** (ex.: "bolo caseiro", "pão de queijo").  
- ***Nome***, ***descrição***, ***unidade de medida*** e ***quantidade inicial***.  
- ***Data de validade***.  

Validações:
- ***Categoria*** deve ser válida e previamente definida.  
- ***Quantidade inicial*** deve ser um número inteiro não negativo.  
- ***Data de validade*** deve estar no formato `AAAA-MM-DD`.  

**Funcionamento:**
A função cria uma instância do produto com base na categoria escolhida e adiciona à lista de produtos.  


### `listar_produtos`: Lista todos os produtos cadastrados no sistema.  

***Exibe:***
- ***Nome*** e ***tipo do produto***.  
- ***Descrição*** e ***quantidade disponível no estoque***.  

Caso nenhum produto esteja cadastrado, exibe uma mensagem informativa.  

### `buscar_produto`: Permite buscar um produto pelo ***código*** e exibe seus detalhes.  

***Exibe:***
- ***Nome***, ***tipo do produto*** e ***descrição***.  
- ***Quantidade disponível no estoque***.  

Caso o código não seja encontrado, exibe uma mensagem de erro.  

### `adicionar_ao_estoque`: Adiciona uma quantidade especificada a um produto existente no estoque.  

**Funcionamento:**
- Solicita o ***código do produto*** e a ***quantidade a ser adicionada***.  
- Atualiza o estoque e exibe a nova quantidade.  

Caso o código não seja encontrado ou a quantidade seja inválida, exibe uma mensagem de erro.  

### `remover_do_estoque`: Remove uma quantidade especificada de um produto existente no estoque.  

**Funcionamento:**
- Solicita o ***código do produto*** e a ***quantidade a ser removida***.  
- Atualiza o estoque e exibe a nova quantidade, desde que haja estoque suficiente.  

Caso o código não seja encontrado ou a quantidade seja inválida, exibe uma mensagem de erro.  


### `gerar_relatorio`: Gera um relatório com a lista de produtos e suas quantidades em estoque.  

#### Exibe:
- ***Código***, ***nome*** e ***quantidade disponível*** de cada produto.  

Caso nenhum produto esteja cadastrado, exibe uma mensagem informativa.  

---

### Classe `interface`

- ***exibir_menu***
Exibe o menu principal com as opções disponíveis para gerenciamento do estoque.  


### `main`
Função principal que gerencia o fluxo do programa.  

#### Funcionamento:
1. ***Inicialização***:  
   - Uma lista `produtos` é criada com instâncias pré-definidas de produtos, como bolos, brownies, pães de queijo, pudins e embalagens.  

2. ***Loop Principal***:  
   - O menu é exibido continuamente até que o usuário escolha a opção "7" (Sair).  
   - O programa aguarda a entrada do usuário para determinar qual ação executar.  

3. ***Ações Baseadas na Escolha***:  
   - ***1***: Chama a função `cadastrar_produto` para adicionar um novo item.  
   - ***2***: Chama a função `listar_produtos` para exibir todos os produtos.  
   - ***3***: Chama a função `buscar_produto` para procurar um produto pelo código.  
   - ***4***: Chama a função `adicionar_ao_estoque` para aumentar a quantidade de um produto.  
   - ***5***: Chama a função `remover_do_estoque` para reduzir a quantidade de um produto.  
   - ***6***: Chama a função `gerar_relatorio` para criar um relatório completo.  
   - ***7***: Exibe uma mensagem de saída e encerra o programa.  
   - ***Opção Inválida***: Exibe uma mensagem de erro e retorna ao menu.  

### Produtos Pré-Cadastrados
A lista `produtos` contém exemplos de produtos organizados por categorias, por ex.:  

- ***Bolos Caseiros***  
   - Ex.: Bolo de Aipim, Bolo de Limão Siciliano.  

Cada produto possui atributos como ***código***, ***nome***, ***descrição***, ***quantidade***, ***data de validade*** e outros específicos de cada tipo.  

### Fluxo de Uso
1. O programa exibe o menu principal.  
2. O usuário escolhe uma opção digitando o número correspondente.  
3. A ação selecionada é executada com base na entrada.  
4. O programa retorna ao menu até que o usuário escolha "7" (Sair).

---

### Classe `main`

Este arquivo serve como ponto de entrada para o sistema de gerenciamento da confeitaria, é o arquivo principal para execução do programa.

***Importações***

1. **`sys` e `os`**  
   - Utilizados para manipular o caminho do sistema e garantir que os módulos necessários sejam encontrados.  
   - A linha `sys.path.append(...)` adiciona o diretório pai do arquivo atual ao caminho de busca de módulos. Isso permite importar módulos localizados em pastas externas.  

2. **`main`**  
   - Importado da função principal `main` localizada em `confeitaria.interface`.  

### Estrutura

#### `if __name__ == "__main__":`
- Verifica se o arquivo está sendo executado diretamente (não importado como módulo).  
- Se verdadeiro, chama a função `main()` para iniciar o programa.  

---

### Classes do pacote `Produtos`

As classes no pacote produtos representam os diferentes tipos de itens que podem ser gerenciados no estoque da confeitaria. Elas são projetadas para encapsular as características e comportamentos de cada categoria de produto. Aqui está uma descrição geral:

***Classe Base: `Produto`***

É a classe genérica que define atributos e métodos comuns a todos os produtos, como id, categoria, nome, descricao, unidade, quantidade, e validade.
Serve como base para as demais classes, promovendo reutilização de código e facilitando a manutenção.

As demais classes são:
1. `***BoloCaseiro***`: Herda atributos da classe `bolo` e representa bolos caseiros tradicionais, geralmente vendidos inteiros.

2. `***BoloDePote***`: Herda atributos da classe `produtos` e representa bolos servidos em potes, com camadas de recheio e cobertura.

3. `***FatiaDeBolo***`: Herda atributos da classe `bolo` e eepresenta porções individuais de bolo, vendidas como fatias.

4. `***Brownie***` :Herda atributos da classe `produtos` e representa brownies, que são pequenos bolos densos à base de chocolate.

5. `***PaoDeQueijo***`: Herda atributos da classe `produtos` e representa pacotes de pães de queijo congelados, prontos para assar.

6. `***Pudim***`: Herda atributos da classe `produtos` e representa pudins, geralmente vendidos inteiros ou em porções.

7. `***Embalagem***`: Herda atributos da classe `produtos` e representa diferentes tipos de embalagens utilizadas para armazenar ou transportar os produtos da confeitaria.

---

## Conclusão

Este projeto oferece um sistema de gerenciamento de estoque simples e eficiente para confeitarias, utilizando a linguagem de programação Python e a programação orientada a objetos. O sistema permite cadastrar, listar, buscar, adicionar e remover produtos do estoque, além de gerar relatórios.
O projeto pode ser expandido com novas funcionalidades, como persistência de dados, interface gráfica e integração com outras ferramentas. Contribuições são bem-vindas e podem ser feitas através do repositório no GitHub.
