    # Validations for a valid CPF:
    # 1. O CPF deve ter exatamente 11 dígitos e conter apenas dígitos
    # 2. O CPF não pode ter todos os dígitos iguais
    # 3. O primeiro dígito verificador deve estar correto:
    #    - Calcula-se o primeiro dígito verificador multiplicando cada dígito do CPF pelos pesos correspondentes e somando os resultados.
    #    - O resultado é dividido por 11 e o resto da divisão é obtido.
    #    - Se o resto for igual a 10, o primeiro dígito verificador é considerado como 0.
    #    - Caso contrário, o primeiro dígito verificador é igual ao resto da divisão.
    #    - Se o primeiro dígito verificador calculado for diferente do primeiro dígito verificador informado no CPF, o CPF é inválido.
    # 4. O segundo dígito verificador deve estar correto:
    #    - Calcula-se o segundo dígito verificador multiplicando cada dígito do CPF, incluindo o primeiro dígito verificador, pelos pesos correspondentes e somando os resultados.
    #    - O resultado é dividido por 11 e o resto da divisão é obtido.
    #    - Se o resto for igual a 10, o segundo dígito verificador é considerado como 0.
    #    - Caso contrário, o segundo dígito verificador é igual ao resto da divisão.
    #    - Se o segundo dígito verificador calculado for diferente do segundo dígito verificador informado no CPF, o CPF é inválido.
    # 5. Se todas as validações forem bem-sucedidas, o CPF é considerado válido.
    # 6. Se alguma validação falhar, o CPF é considerado inválido.


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

