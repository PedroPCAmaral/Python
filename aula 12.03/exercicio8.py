num = input("Digite 4 dígitos: ")

a = (int(num[0]) + 7) % 10
b = (int(num[1]) + 7) % 10
c = (int(num[2]) + 7) % 10
d = (int(num[3]) + 7) % 10

print(c, d, a, b)
