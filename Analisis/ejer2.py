'''
Registro de personas

Registrar 3 personas con:
- nombre
- edad

Mostrar:
cuántas son mayores de edad
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad

   
personas= [None]*3
contador=0
mayores=0

while contador<3:
    nombre= input("Por favor, ingresa el nombre: ")
    edad= input("Por favor, ingresa la edad: ")
    personas[contador]= Persona(nombre, edad)
    contador+=1
    


