'''
Validación de acceso:
Solicita usuario, contraseña y rol (admin, editor, visitante). Verifica si las credenciales
son válidas y muestra los permisos disponibles según el rol. Usa múltiples condicionales
y lógica anidada.

'''
usuario= input("Por favor, ingresa el usuario: ")
contraseña= input("Por favor, ingresa tu contraseña: ")
rol= input("Por favor, ingresa tu rol (admin/editor/visitante): ").lower()

usuarios_validos={
    "admin":"a123",
    "editor":"e123",
    "visitante":"v123",
}
if usuario in usuarios_validos and usuarios_validos[usuario]==contraseña:
    print(f"Rol {rol.upper()}")
    print("Permisos concedidos")
    if rol=="admin":
        print("Crear usuarios")
        print("Editar usuarios")
    elif rol=="editor":
        print("Todos menos eliminar")
    elif rol=="visitante":
        print("Solo puede ver")
    else:
        print("No existe el rol")
else:
    print("Acceso denegado")
    
        