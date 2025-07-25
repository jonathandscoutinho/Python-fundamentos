# Estrutura de Dados - Dicionários
# Dicionário é uma coleção de pares chave-valor
# onde cada chave é única e mapeia para um valor.
# Dicionários são mutáveis e podem ser alterados após a criação.

# Exemplo de dicionário
empty_dict = {}
print(empty_dict)  # Saída: {}

# Dicionário com dados de uma pessoa
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}
print(pessoa)  # Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Dicionario com numeros inteiros onde as chaves são os números e os valores são string
numeros = {
    1: "um",
    2: "dois",
    3: "tres"
}
print(numeros)  # Saída: {1: 'um', 2: 'dois', 3: 'tres'}
# Acessando valores em um dicionário
print(pessoa["nome"])  # Saída: João
print(numeros[1])  # Saída: um

# Dicionario com string onde as chaves são os strings e os valores são numeros inteiros
frutas = {
    "maca": 1,
    "banana": 2,
    "laranja": 3
}
print(frutas)  # Saída: {'maca': 1, 'banana': 2, 'laranja': 3}

# Dicionário com diferentes tipos de dados
dados = {
    "nome": "João",
    "idade": 30,
    "altura": 1.75,
    "habilidades": ["programação", "matemática", "comunicação"]
}
print(dados)  # Saída: {'nome': 'João', 'idade': 30, 'altura': 1.75, 'habilidades': ['programação', 'matemática', 'comunicação']}   

# Adicionando novos pares chave-valor
pessoa["email"] = "joao@example.com"
print(pessoa)  # Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo', 'email': '


# Modificar um valor existente
# Basta modificar o valor associado a uma chave existente
pessoa["idade"] = 31
print(pessoa)  # Saída: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo', 'email': 'joao@example.com'}

# Metodo pop
# Remove um par chave-valor do dicionário
# e retorna o valor associado à chave removida.
pessoa.pop("email")
print(pessoa)  # Saída: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo'}    

# O metodo pop pode receber um segundo argumento
# que é o valor padrão a ser retornado caso a chave não exista.
email = pessoa.pop("email", "Email não encontrado")
print(email)  # Saída: Email não encontrado

# O metodo pop remove o ultimo elemento do dicionário
ultimo_item = pessoa.popitem()
print(ultimo_item)  # Saída: ('cidade', 'São Paulo')