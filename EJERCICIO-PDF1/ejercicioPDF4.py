

while True:
    num = int(input("Ingrese número entero: "))
    if num % 3 == 0 and num % 5 == 0:
        print("El número es divisible por 3 y por 5.")
    else:
        print("El número NO es divisible por 3 y por 5.")
    
    opcion = input("¿Desea continuar? (si/no): ").lower()
    
    if opcion != 'si':
        print("Finalizado")
        break
    
        
# numero = int(input("Ingrese un número entero: "))


# if numero % 3 == 0 and numero % 5 == 0:
#     print(f"El número {numero} es divisible por 3 y por 5.")
# else:
#     print(f"El número {numero} NO es divisible por 3 y por 5.")
