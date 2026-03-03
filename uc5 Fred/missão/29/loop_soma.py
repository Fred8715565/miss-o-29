soma = 0

while True:
    numero = int(input("Digite um número inteiro (0 para parar): "))
    
    if numero == 0:
        break
    
    soma += numero
    print("Soma atual:", soma)

print("Soma final:", soma)