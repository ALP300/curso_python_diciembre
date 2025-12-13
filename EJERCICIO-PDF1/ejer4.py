'''Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F'''

def calcular_nota(calificacion):

    if calificacion < 0 or calificacion > 100:
        return "Error: La calificación debe estar entre 0 y 100."

    if calificacion >= 90:
        return "A"
    elif calificacion >= 80:
        return "B"
    elif calificacion >= 70:
        return "C"
    elif calificacion >= 60:
        return "D"
    else:
        return "F"
try:
    
    entrada = input("Introduce la calificación numérica (0-100): ")
    
    
    numero = float(entrada)
    
     
    letra = calcular_nota(numero)
    print(f"Tu calificación es: {letra}")

except ValueError:
    print("Por favor, introduce un número válido.")