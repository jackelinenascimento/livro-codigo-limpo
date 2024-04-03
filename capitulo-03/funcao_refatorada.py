def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # Remover pontos e traços

    if not possui_tamanho_valido(cpf) or not possui_digitos_validos(cpf) or possui_digitos_repetidos(cpf):
        imprimir_validacao_cpf(False)
        return False

    if not possui_digito_verificador_valido(cpf, 9) or not possui_digito_verificador_valido(cpf, 10):
        imprimir_validacao_cpf(False)
        return False

    imprimir_validacao_cpf(True)
    return True


def possui_tamanho_valido(cpf):
    return len(cpf) == 11


def possui_digitos_validos(cpf):
    return cpf.isdigit()


def possui_digitos_repetidos(cpf):
    return len(set(cpf)) == 1


def possui_digito_verificador_valido(cpf, indice):
    pesos = range(2, 12)
    digito = int(cpf[indice])
    digito_calculado = sum(int(cpf[i]) * pesos[i] for i in range(indice)) % 11
    digito_calculado = 0 if digito_calculado == 10 else digito_calculado
    return digito_calculado == digito


def imprimir_validacao_cpf(valido):
    if valido:
        print("CPF válido")
    else:
        print("CPF inválido")