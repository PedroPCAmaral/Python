texto = input("Digite o texto: ")
n = int(input("Deslocamento: "))

resultado = ""

for letra in texto:
    if letra.isalpha():
        resultado += chr(ord(letra) + n)
    else:
        resultado += letra

print(resultado)
