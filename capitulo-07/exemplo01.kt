// exemplo de exceção não verificada 

fun divide(a: Int, b: Int): Int {
    if (b == 0) {
        throw ArithmeticException("Divisão por zero não é permitida.")
    }
    return a / b
}

fun main() {
    try {
        val resultado = divide(10, 0)
        println("Resultado: $resultado")
    } catch (e: ArithmeticException) {
        println("Erro: ${e.message}")
    }
}