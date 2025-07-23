# Operadores lógicos
# And, or, not - e, ou, não

verdadeiro = True
falso = False

# Se pelo menos um dos valores for False, o resultado é False
# A rera geral é, leia a expressão E e se pelo menos um valor for False, o resultado é False
print(verdadeiro and verdadeiro)  # True
print(verdadeiro and falso)        # False
print(falso and verdadeiro)         # False
print(falso and falso)             # False
print("---------------------")

# Se pelo menos um dos valores for True, o resultado é True
# A regra geral é, leia a expressão OU e se pelo menos um valor for True, o resultado é True
print(verdadeiro or verdadeiro)    # True
print(verdadeiro or falso)         # True
print(falso or verdadeiro)          # True
print(falso or falso)              # False
print("---------------------")

print(not verdadeiro)               # False
print(not falso)                   # True

valid_password = True

print(f" valid_password: {valid_password}")