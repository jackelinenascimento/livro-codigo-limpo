class Cliente {
    public void solicitarPedido(Produto produto) {
        // Busca o fornecedor do produto
        Fornecedor fornecedor = produto.obterFornecedor();

        // Verifica se o fornecedor tem o produto em estoque
        if (fornecedor.possuiEstoque(produto)) {
            // Envia o pedido para o fornecedor
            fornecedor.enviarPedido(produto);
        } else {
            // Informa o cliente que o produto não está disponível
            System.out.println("Produto não disponível em estoque");
        }
    }
}