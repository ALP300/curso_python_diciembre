'''
Registro de mascotas

Guardar 5 mascotas con:
nombre
tipo (perro, gato)
edad

Mostrar:

cuántas son perros
cuál es la mascota más joven
'''

class Mascotas:
    def __init__(self, nombre, tipo, edad):
        self.nombre= nombre
        self.tipo= tipo.lower()
        self.edad= edad

mascotas= [None]*2
contador=0
perros=0

while contador<2:
    nombre= input("Ingresa el nombre de la mascota: ") 
    tipo= input("Ingresa el tipo de la mascota: ") 
    edad= int(input("Ingresa la edad la mascota: "))
    mascotas[contador]= Mascotas(nombre, tipo, edad)
    contador+=1

menor= mascotas[0]
for i in range(contador):
    if mascotas[i].tipo=="perro":
        perros+=1
    if mascotas[i].edad<menor.edad:
        menor= mascotas[i]

print("Cantidad de perritos: ", perros)
print("El menor es: ", menor.edad)
    
