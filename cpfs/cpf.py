import random

def generate_cpf():
    # Gera os primeiros nove dígitos do CPF
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    sum_1 = sum([(10 - i) * cpf[i] for i in range(9)])
    digit_1 = 11 - (sum_1 % 11)
    if digit_1 >= 10:
        digit_1 = 0
    cpf.append(digit_1)

    # Calcula o segundo dígito verificador
    sum_2 = sum([(11 - i) * cpf[i] for i in range(10)])
    digit_2 = 11 - (sum_2 % 11)
    if digit_2 >= 10:
        digit_2 = 0
    cpf.append(digit_2)

    # Formata o CPF no padrão XXX.XXX.XXX-XX
    cpf_str = ''.join(map(str, cpf))
    formatted_cpf = f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"
    return formatted_cpf

# Gera um CPF válido
print(generate_cpf())
