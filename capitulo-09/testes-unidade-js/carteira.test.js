const Carteira = require('./carteira');

describe('Testes da Classe Carteira com Regra de Negócio', () => {
    let carteira;

    beforeEach(() => {
        carteira = new Carteira();
    });

    test('Adicionar transação válida', () => {
        carteira.adicionarTransacao('Compra de livro', 50);
        carteira.adicionarTransacao('Salário', 1000);
        
        expect(carteira.obterHistorico()).toHaveLength(2);
        expect(carteira.calcularSaldo()).toBe(1050);
    });

    test('Adicionar transação inválida - saldo insuficiente', () => {
        carteira.adicionarTransacao('Depósito inicial', 100);
        expect(() => carteira.adicionarTransacao('Compra de celular', -150)).toThrow('Não é possível realizar a transação. Saldo insuficiente.');
        
        expect(carteira.obterHistorico()).toHaveLength(1); // Apenas o depósito inicial deve estar no histórico
        expect(carteira.calcularSaldo()).toBe(100); // Saldo deve permanecer 100
    });

    test('Adicionar transação inválida - valor não numérico', () => {
        expect(() => carteira.adicionarTransacao('Pagamento', 'abc')).toThrow('O valor da transação deve ser numérico.');
        
        expect(carteira.obterHistorico()).toHaveLength(0); // Nenhuma transação deve ter sido adicionada
        expect(carteira.calcularSaldo()).toBe(0); // Saldo deve permanecer 0
    });

    test('Calcular saldo com várias transações', () => {
        carteira.adicionarTransacao('Depósito inicial', 500);
        carteira.adicionarTransacao('Saque', -50);
        carteira.adicionarTransacao('Compra', -200);
        
        expect(carteira.calcularSaldo()).toBe(250); // Saldo final esperado após as transações
    });

    test('Obter histórico de transações', () => {
        carteira.adicionarTransacao('Depósito inicial', 500);
        carteira.adicionarTransacao('Saque', -50);
        
        const historico = carteira.obterHistorico();
        expect(historico).toHaveLength(2);
        expect(historico[0]).toEqual({ descricao: 'Depósito inicial', valor: 500 });
        expect(historico[1]).toEqual({ descricao: 'Saque', valor: -50 });
    });
});
