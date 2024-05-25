# Lei de Demeter

A Lei de Deméter, também conhecida como Princípio do Menor Conhecimento, é uma diretriz fundamental na programação orientada a objetos (POO) que visa reduzir o acoplamento entre classes e promover a modularidade e a reutilização de código. Ela foi proposta por Robert Martin em 1987 e se baseia na ideia de que cada objeto deve interagir apenas com seus "amigos imediatos", ou seja, com os objetos que ele possui como atributos ou que ele retorna de seus métodos.

Em outras palavras, a Lei de Deméter diz que um objeto deve evitar chamar métodos de objetos que ele não conhece diretamente. Em vez disso, ele deve delegar essa responsabilidade aos seus amigos imediatos, que por sua vez podem delegar para seus próprios amigos imediatos, e assim por diante. Essa cadeia de chamadas permite que os objetos permaneçam independentes e encapsulados, tornando o código mais fácil de entender, manter e modificar.

## Benefícios da Lei de Deméter:

Redução do acoplamento: Ao limitar as interações entre objetos, a Lei de Deméter diminui o acoplamento entre classes, tornando o código mais modular e flexível. Isso facilita a reutilização de classes em diferentes partes do programa e torna o código mais fácil de testar e depurar.
Maior clareza e legibilidade: O código que segue a Lei de Deméter tende a ser mais claro e legível, pois cada objeto tem uma responsabilidade bem definida e as interações entre os objetos são mais diretas e fáceis de entender. Isso facilita a compreensão e a manutenção do código, especialmente em projetos grandes e complexos.
Maior facilidade de manutenção: A Lei de Deméter torna o código mais fácil de manter, pois as mudanças em uma classe geralmente afetam apenas seus amigos imediatos, minimizando o impacto em outras partes do programa. Isso permite que os desenvolvedores façam alterações no código com mais confiança e sem se preocupar em causar efeitos colaterais indesejados.
Exemplos da Lei de Deméter em ação:

Cenário sem a Lei de Deméter:

Java
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

Neste exemplo, o método solicitarPedido da classe Cliente viola a Lei de Deméter, pois ele acessa diretamente o método obterFornecedor da classe Produto e o método possuiEstoque e enviarPedido da classe Fornecedor. Isso cria um acoplamento forte entre as três classes, tornando o código mais difícil de entender, manter e modificar.

Cenário com a Lei de Deméter:

Java
class Cliente {
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


Neste exemplo, o método solicitarPedido da classe Cliente segue a Lei de Deméter, pois ele interage apenas com o serviço de pedidos, que por sua vez é responsável por interagir com as classes Produto e Fornecedor. Isso reduz o acoplamento entre as classes e torna o código mais modular e fácil de manter.

Conclusão:

A Lei de Deméter é um princípio fundamental na POO que ajuda a escrever código