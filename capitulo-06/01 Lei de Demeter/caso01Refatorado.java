lass Cliente {
    public void solicitarPedido(Produto produto) {
        // Busca o fornecedor do produto através do serviço de pedidos
        Fornecedor fornecedor = ServicoPedidos.obterFornecedor(produto);

        // Verifica se o fornecedor tem o produto em estoque
        if (ServicoPedidos.possuiEstoque(produto, fornecedor)) {
            // Envia o pedido para o fornecedor através do serviço de pedidos
            ServicoPedidos.enviarPedido(produto, fornecedor);
        } else {
            // Informa o cliente que o produto não está disponível
            System.out.println("Produto não disponível em estoque");
        }
    }
}

class ServicoPedidos {
    public static Fornecedor obterFornecedor(Produto produto) {
        // Implementar lógica para buscar o fornecedor do produto
    }

    public static boolean possuiEstoque(Produto produto, Fornecedor fornecedor) {
        // Implementar lógica para verificar se o fornecedor tem o produto em estoque
    }

    public static void enviarPedido(Produto produto, Fornecedor fornecedor) {
        // Implementar lógica para enviar o pedido para o fornecedor
    }
}