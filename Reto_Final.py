# ==========================================
# PROYECTO: SISTEMA DE NOTAS
# ==========================================

print("==========================================")
print("       SISTEMA DE NOTAS DEL ESTUDIANTE")
print("==========================================")

# Nombre del estudiante
nombre = input("Ingrese el nombre del estudiante: ")

# Cantidad variable de notas
cantidad = int(input("¿Cuántas notas desea ingresar?: "))

notas = []

# Ingresar las notas
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i + 1}: "))

    while nota < 0 or nota > 5:
        print("La nota debe estar entre 0.0 y 5.0.")
        nota = float(input(f"Ingrese nuevamente la nota {i + 1}: "))

    notas.append(nota)


# ==========================================
# CALCULAR EL PROMEDIO
# ==========================================

promedio = sum(notas) / len(notas)

print("\n==========================================")
print("RESULTADOS")
print("==========================================")

print(f"Estudiante: {nombre}")
print(f"Notas: {notas}")
print(f"Promedio: {promedio:.2f}")


# ==========================================
# CLASIFICACIÓN DEL ESTUDIANTE
# ==========================================

if promedio >= 4.5:
    mensaje = "¡Excelente trabajo! Tu desempeño es sobresaliente."
elif promedio >= 4.0:
    mensaje = "¡Muy bien! Tienes un desempeño destacado."
elif promedio >= 3.0:
    mensaje = "Aprobaste. Puedes seguir mejorando."
else:
    mensaje = "No aprobaste. Debes reforzar tus conocimientos."

print(mensaje)


# ==========================================
# BUG COMUNICATIVO: PUNTOS PARA LLEGAR A 4.0
# ==========================================

puntos_faltantes = 4.0 - promedio

if puntos_faltantes > 0:
    print(f"Te faltan {puntos_faltantes:.2f} puntos para llegar a 4.0.")
else:
    print("¡Felicitaciones! Ya superaste la nota de 4.0.")


# ==========================================
# MENÚ CON MATCH-CASE
# ==========================================

print("\n==========================================")
print("MENÚ")
print("==========================================")
print("1. Ver promedio")
print("2. Ver clasificación")
print("3. Ver puntos para llegar a 4.0")
print("4. Ver cantidad de notas")
print("5. Salir")

opcion = input("Seleccione una opción: ")

match opcion:
    case "1":
        print(f"Tu promedio es: {promedio:.2f}")

    case "2":
        print(mensaje)

    case "3":
        if puntos_faltantes > 0:
            print(f"Te faltan {puntos_faltantes:.2f} puntos para llegar a 4.0.")
        else:
            print("¡Felicitaciones! Ya superaste la nota de 4.0.")

    case "4":
        print(f"Ingresaste {len(notas)} notas.")

    case "5":
        print("Gracias por utilizar el sistema.")

    case _:
        print("Opción no válida.")