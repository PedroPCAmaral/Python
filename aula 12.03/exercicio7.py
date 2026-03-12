frase = input("Digite uma frase: ").lower()

contador = 0

for letra in frase:
    if letra in "aeiou":
        contador += 1

print("Vogais:", contador)
