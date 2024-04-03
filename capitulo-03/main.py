from funcao_original import validar_cpf

def main():
    cpf = input("Digite um CPF: ")
    resultado = validar_cpf(cpf)
    print(resultado)

if __name__ == "__main__":
    main()