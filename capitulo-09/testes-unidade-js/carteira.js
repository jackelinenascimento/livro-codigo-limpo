// Definição da classe Carteira
class Carteira {
    constructor() {
        this.transacoes = [];
    }

    adicionarTransacao(descricao, valor) {
        if (typeof valor !== 'number') {
            throw new Error('O valor da transação deve ser numérico.');
        }

        // Calcula o saldo atual incluindo a nova transação
        const saldoPrevisto = this.calcularSaldo() + valor;

        // Verifica se o saldo previsto não é negativo
        if (saldoPrevisto < 0) {
            throw new Error('Não é possível realizar a transação. Saldo insuficiente.');
        }

        const transacao = { descricao, valor };
        this.transacoes.push(transacao);
    }

    calcularSaldo() {
        let saldo = 0;
        for (const transacao of this.transacoes) {
            saldo += transacao.valor;
        }
        return saldo;
    }

    obterHistorico() {
        return this.transacoes.slice(); // Retorna uma cópia das transações
    }
}

module.exports = Carteira; // Exporta a classe para uso em outros arquivos
