'''
Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).
'''

num1= float(input("Por favor, ingresa el número 1: "))
num2= float(input("Por favor, ingresa el número 2: "))
texto= "Holaaa"
suma= num1+num2
resta= num1-num2
mult= num1*num2

print(f"La suma es: {suma}. La resta es: {resta}. La multiplicación: {mult}")
if num2!=0:
    print(f"División: {num1/num2}")
else:
    print("No se puede dividir por 0")


