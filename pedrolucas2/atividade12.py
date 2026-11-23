def validar_cpf (cpf: str) -> bool:
    cpf = "".join(filter(str.isdigit,cpf))


    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False


    soma1 = sum(int(cpf[i]) * (10 - i)for i in range(9))
    digito1 = (soma1 * 10 % 11) % 10

    soma2 = sum(int(cpf[i]) * (10 - i) for i in range(10))
    digito2 = (soma2 * 10 % 11) % 10

    return cpf[-2:] == f"{digito1}{digito2}"
print(validar_cpf('123.456.789-00'))