# admin, user, guest

rule = input("Digite seu cargo: ")

if rule == "admin":
    print("Acesso total")
elif rule == "user":
    print("Acesso restrito")
elif rule == "guest":
    print("Acesso limitado")
else:
    print("Acesso negado")