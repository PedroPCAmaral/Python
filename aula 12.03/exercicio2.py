numero = input("Digite um número: ")
base = int(input("Digite a base (8, 10 ou 16): "))

valor = int(numero, base)

print("Decimal:", valor)
print("Hexadecimal:", hex(valor))
print("Octal:", oct(valor))
