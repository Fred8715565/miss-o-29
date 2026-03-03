# loop_conta_letras.py

texto = input("Digite um texto: ")

maiusculas = 0
minusculas = 0

for letra in texto:
    if letra.isupper():
        maiusculas += 1
    elif letra.islower():
        minusculas += 1

print("Número de letras maiúsculas:", maiusculas)
print("Número de letras minúsculas:", minusculas)