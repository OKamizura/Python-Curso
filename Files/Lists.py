import random
estados_do_brasil = ["Minas Gerais", "São Paulo", "Rio de Janeiro" ]

print(estados_do_brasil[1])
#ultimo termo:

print(estados_do_brasil[-1])

# Inserir um novo termo no final da lista:
estados_do_brasil.append("Alagoas")

print(estados_do_brasil)

# Inserir um novo termo em qualquer lugar da lista:
estados_do_brasil.insert("Mato Grosso", 1)

# Apagar o primeiro termo com o valor:

estados_do_brasil.remove("Alagoas")

# Apagar o termo com o índice:

estados_do_brasil.pop(3)

print(random.choice(estados_do_brasil))

# Ou random_state = random.randint(0,2)
# print(estados_do_brasil[random_state])
