def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")  # Remover pontos e traços
    if len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido")
        return False

    # Verificar se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        print("CPF inválido")
        return False

    # Verificar o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    if digito1 == 10:
        digito1 = 0
    if digito1 != int(cpf[9]):
        print("CPF inválido")
        return False

    # Verificar o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    if digito2 == 10:
        digito2 = 0
    if digito2 != int(cpf[10]):
        print("CPF inválido")
        return False

    print("CPF válido")
    return True