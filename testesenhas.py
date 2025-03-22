import re

def verificar_forca_senha(senha):
    # Critérios de força da senha
    comprimento_minimo = 8
    tem_maiuscula = re.search(r'[A-Z]', senha)
    tem_minuscula = re.search(r'[a-z]', senha)
    tem_numero = re.search(r'[0-9]', senha)
    tem_caracter_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)

    # Verificando o comprimento da senha
    if len(senha) < comprimento_minimo:
        return "A senha é muito curta. Recomenda-se pelo menos {} caracteres.".format(comprimento_minimo)

    # Verificando a presença de diferentes tipos de caracteres
    sugestoes = []
    if not tem_maiuscula:
        sugestoes.append("Adicionar pelo menos uma letra maiúscula.")
    if not tem_minuscula:
        sugestoes.append("Adicionar pelo menos uma letra minúscula.")
    if not tem_numero:
        sugestoes.append("Adicionar pelo menos um número.")
    if not tem_caracter_especial:
        sugestoes.append("Adicionar pelo menos um caractere especial (e.g., !@#$%^&*).")

    # Avaliando a força da senha
    if not sugestoes:
        return "A senha é forte. Parabéns!"
    else:
        return "A senha pode ser melhorada. Sugestões:\n" + "\n".join(sugestoes)

# Exemplo de uso
senha = input("Digite sua senha: ")
resultado = verificar_forca_senha(senha)
print(resultado)