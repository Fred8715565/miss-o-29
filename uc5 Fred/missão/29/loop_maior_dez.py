
maiores_que_dez = []
soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero > 10:
        maiores_que_dez.append(numero)
        soma += numero

print("Números maiores que 10 digitados:", maiores_que_dez)
print("Soma dos números maiores que 10:", soma)