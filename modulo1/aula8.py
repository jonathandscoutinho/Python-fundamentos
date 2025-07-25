# Estrutura de dados

# Tuplas

# Tuplas são coleções de itens em uma ordem específica, mas são imutáveis, ou seja, não podem ser alteradas após a criação.
# A tupla é definida com parênteses () e os itens são separados por vírgulas.
# Tuplas podem conter qualquer tipo de dado, inclusive outras tuplas.

empty_tuple = ()
print(empty_tuple)

# Tuplas de números inteiros
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(numbers[0])  # Acessando o primeiro elemento
print(numbers[1])  # Acessando o segundo elemento

# Tuplas de strings
fruits = ("maca", "banana", "laranja")
print(fruits)
print(fruits[0])  # Acessando o primeiro elemento
print(fruits[1])  # Acessando o segundo elemento
print(fruits[2])  # Acessando o terceiro elemento   

# Tuplas mistas
mixed_tuple = (1, "maca", 3.14, True)
print(mixed_tuple)
print(mixed_tuple[0])  # Acessando o primeiro elemento
print(mixed_tuple[1])  # Acessando o segundo elemento
print(mixed_tuple[3])  # Acessando o último elemento

# Tuplas aninhadas
nested_tuple = ((1, 2, 3), ("maca", "banana", "laranja"), (True, False))
print(nested_tuple) 
print(nested_tuple[0])  # Acessando o primeiro elemento
print(nested_tuple[1])  # Acessando o segundo elemento
print(nested_tuple[2])  # Acessando o terceiro elemento

# Desempacotamento de tuplas
print
a, b, c, d, e = numbers
print(a)  # Acessando o primeiro elemento
print(b)  # Acessando o segundo elemento
print(c)  # Acessando o terceiro elemento
print(d)  # Acessando o quarto elemento
print(e)  # Acessando o quinto elemento

# O desempacotamento de tuplas permite trocar valores de variáveis
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)  # Agora a é 2 e b é 1

# Outros metodos de tuplas
# O método count retorna o número de ocorrências de um elemento na tupla
print(numbers.count(1))  # Saída: 1
print(numbers.count(6))  # Saída: 0

# O método index retorna o índice da primeira ocorrência de um elemento na tupla
print(numbers.index(3))  # Saída: 2
# print(numbers.index(6))  # Isso causaria um erro, pois 6 não
# está na tupla
# print(numbers.index(6, 0, 3))  # Isso causaria um erro, pois 6 não está na tupla
# O método index pode receber um intervalo de índices para buscar o elemento

# O método index pode receber um intervalo de índices para buscar o elemento
print(numbers.index(3, 0, 4))  # Saída: 2
# O método index pode receber um intervalo de índices para buscar o elemento  