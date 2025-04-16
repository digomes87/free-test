def contador(max):
    i = 0
    while i < max:
        yield i
        i += 1


for numero in contador(9):
    print(numero)


def alternar():
    yield "Primeiro"
    yield "Segundo"
    yield "Terceiro"


# Usando o gerador
for item in alternar():
    print(item)


def contador_personalizado():
    valor = 0
    while True:
        increment = yield valor
        if increment is not None:
            valor += increment
        else:
            valor += 1


# Usando o gerador
gen = contador_personalizado()
print(next(gen))  # 0
print(gen.send(5))  # 5
print(next(gen))  # 6
print(gen.send(10))  # 16
