from inventory_report.inventory.product import Product


def test_cria_produto():
    id = 1
    nome_do_produto = 'Nicotine Polacrilex'
    nome_da_empresa = 'Target Corporation'
    data_de_fabricacao = '2021-02-18'
    data_de_validade = '2023-09-17'
    numero_de_serie = 'CR25 1551 4467 2549 4402 1'
    instrucoes_de_armazenamento = 'instrucao 1'

    new_product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento
    )

    assert new_product.id == id
    assert new_product.nome_do_produto == nome_do_produto
    assert new_product.nome_da_empresa == nome_da_empresa
    assert new_product.data_de_fabricacao == data_de_fabricacao
    assert new_product.data_de_validade == data_de_validade
    assert new_product.numero_de_serie == numero_de_serie
    assert new_product.instrucoes_de_armazenamento == 'instrucao 1'
