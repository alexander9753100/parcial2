#saludo de bienvenida
print("BIENVENIDO A NUESTRO PROGRAMA") 

while True:
    try:
        N = int(input("\nPor favor ingresa un número entero positivo: "))
        if N <= 0:
            raise ValueError
        break
    except ValueError:
        print("\nEl número ingresado no es válido. por favor Intente de nuevo.")

total = 0.0
for i in range(1, N+1):
    total += 1.0/i

print("\nEl resultado de la serie es: ", total)


print("\nfin del programa\n")
