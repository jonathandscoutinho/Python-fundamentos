# Operadores de comparação / relacionais

# Iguais a: ==
# Diferentes de: !=
# Maior que: >
# Menor que: <
# Maior ou igual a: <=
# Menor ou igual a: >=

a = 3
b = 3

print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}") # True
print(f"{a} > {b}: {a > b}") # True
print(f"{a} < {b}: {a < b}") # False
print(f"{a} >= {b}: {a >= b}") # True
print(f"{a} <= {b}: {a <= b}") # False

age = 99

print(age)
if age >= 18 and age <= 100:
    print("Você é maior de idade")
elif age >= 0 and age < 18:
    print("Você é menor de idade")
else:
    print("Idade não encontrada")