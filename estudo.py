import re

def testar_forca_senha(senha):
    """Verifica a força de uma senha com base em alguns critérios."""
    pontuacao = 0
    criterios = []

    # Critério 1: Comprimento mínimo (ex: 8 caracteres)
    if len(senha) >= 8:
        pontuacao += 1
        criterios.append("✅ Pelo menos 8 caracteres")
    else:
        criterios.append("❌ Pelo menos 8 caracteres")

    # Critério 2: Pelo menos uma letra maiúscula
    if re.search(r'[A-Z]', senha):
        pontuacao += 1
        criterios.append("✅ Pelo menos uma letra maiúscula")
    else:
        criterios.append("❌ Pelo menos uma letra maiúscula")

    # Critério 3: Pelo menos uma letra minúscula
    if re.search(r'[a-z]', senha):
        pontuacao += 1
        criterios.append("✅ Pelo menos uma letra minúscula")
    else:
        criterios.append("❌ Pelo menos uma letra minúscula")

    # Critério 4: Pelo menos um número
    if re.search(r'[0-9]', senha):
        pontuacao += 1
        criterios.append("✅ Pelo menos um número")
    else:
        criterios.append("❌ Pelo menos um número")

    # Critério 5: Pelo menos um caractere especial
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        pontuacao += 1
        criterios.append("✅ Pelo menos um caractere especial")
    else:
        criterios.append("❌ Pelo menos um caractere especial")

    print("Critérios atendidos:")
    for criterio in criterios:
        print(criterio)

    print(f"\nPontuação da senha: {pontuacao}/5")

    if pontuacao == 5:
        print("Força da senha: Muito Forte 💪")
    elif pontuacao >= 3:
        print("Força da senha: Forte 👍")
    elif pontuacao >= 1:
        print("Força da senha: Moderada 👌")
    else:
        print("Força da senha: Fraca 👎")

# Solicitar a senha ao usuário
senha_digitada = input("Digite a senha para testar: ")

# Testar a força da senha
testar_forca_senha(senha_digitada)