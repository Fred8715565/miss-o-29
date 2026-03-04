senha = input("Digite a senha: ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

caracteres_especiais = "!@#$%&*()-_=+[]{};:,.?/"

if len(senha) >= 8:
    
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_especial = True

    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        print("Senha válida e forte!")
    else:
        print("Senha inválida! Não atende a todos os requisitos.")
else:
    print("Senha inválida! Deve ter no mínimo 8 caracteres.")
