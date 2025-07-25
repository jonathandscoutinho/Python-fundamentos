# Estrutura de dados - Listas

# Listas

# Listas são coleções de itens em uma ordem específica. Podem ter qualquer tipo de dado, inclusive outras listas.

empty_list = []
print(empty_list)

# Listas de números inteiros
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])  # Acessando o primeiro elemento
print(numbers[1])  # Acessando o segundo elemento
print(numbers[-1])  # Acessando o último elemento
print(numbers[-2])  # Acessando o penúltimo elemento

# Listas de strings
fruits = ["maca", "banana", "laranja"]
print(fruits)
print(fruits[0])  # Acessando o primeiro elemento
print(fruits[1])  # Acessando o segundo elemento
print(fruits[-1])  # Acessando o último elemento
print(fruits[-2])  # Acessando o penúltimo elemento

# Listas mistas
mixed_list = [1, "maca", 3.14, True]
print(mixed_list)
print(mixed_list[0])  # Acessando o primeiro elemento
print(mixed_list[1])  # Acessando o segundo elemento
print(mixed_list[-1])  # Acessando o último elemento
print(mixed_list[-2])  # Acessando o penúltimo elemento

# Listas aninhadas
nested_list = [[1, 2, 3], ["maca", "banana", "laranja"], [True, False]]
print(nested_list)
print(nested_list[0])  # Acessando o primeiro elemento
print(nested_list[1])  # Acessando o segundo elemento
print(nested_list[-1])  # Acessando o último elemento
print(nested_list[-2])  # Acessando o penúltimo elemento

# Adicionando elementos a uma lista
# O método append adiciona um elemento ao final da lista
print(fruits)
fruits.append("uva")
print(fruits)

# Removendo elementos de uma lista
# O método remove o ultimo item da lista
print(fruits.pop(1))  # Remove e retorna o segundo elemento

# O método remove remove o primeiro item com o valor especificado
fruits.remove("laranja")  # Remove a primeira ocorrência de "laranja"
print(fruits)

# O metodo remove remove o primeiro item pelo index especificado
fruits.remove(fruits[0])  # Remove o primeiro elemento

# Ordenar uma lista
numberts = [5, 2, 9, 1, 5, 6]
numbers.sort()  # Ordena a lista em ordem decrescente
print(numbers)

# O metodo sort() pode receber o parametro reverse=True para ordenar em ordem decrescente
numbers.sort(reverse=True)  # Ordena a lista em ordem crescente
print(numbers)

# O metodo sort() não funciona em listas mistas
mixed_list.sort()  # Isso causará um erro, pois a lista contém tipos diferentes
print(mixed_list)