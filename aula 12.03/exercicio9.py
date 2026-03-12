num = input("Digite o número criptografado: ")

a = int(num[2])
b = int(num[3])
c = int(num[0])
d = int(num[1])

a = (a - 7) % 10
b = (b - 7) % 10
c = (c - 7) % 10
d = (d - 7) % 10

print(a, b, c, d)
