# 1. uso basico de while

numero = 1

while numero <=5:
    print(numero)
    numero += 1


# 2. uso basico de for

frutas = ["manzana", "platano", "naranja"]

for fruta in frutas:
    print(fruta)


# 3. condicion en un ciclo

for numero in range(1,11):
    if numero % 2 == 0:
        print(numero, "par")
        break

# 4. ciclo anidado

for i in range(1,4):
    print(f"tabla del {i}")

    for j in range(1,11):
        print(f"{i}x{j}={i*j}")

    print()


# 5. uso de continue

nombres = ["Camila", "Pedro", "Juan", "Emilio"]

for nombre in nombres:
    if nombre == "Juan":
        continue # salta esta iteración y no imprime "Juan"

    print(nombre)

# este programa recorre una lista de nombres e imprime cada uno,
# excepto "Juan". El ciclo termina automáticamente cuando se recorren
# todos los elementos de la lista.