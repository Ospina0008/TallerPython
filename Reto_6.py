# ==========================================
# 1. CLASIFICADOR DE EDADES
# ==========================================

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 11:
    print("Niño")
elif edad >= 12 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")


# ==========================================
# 2. OPERADOR TERNARIO
# ==========================================

temperatura = float(input("\nIngrese la temperatura: "))

# Operador ternario
mensaje = "Hace calor" if temperatura > 25 else "Está fresco"

print(mensaje)

# Operador ternario dentro de una f-string
print(f"Temperatura: {temperatura}°C - {'Hace calor' if temperatura > 25 else 'Está fresco'}")


# ==========================================
# 3. MENÚ CON MATCH-CASE
# ==========================================

opcion = input("""
===== MENÚ =====
1. Consultar nota
2. Ver promedio
3. Ayuda
4. Salir
Seleccione una opción: 
""")

match opcion:
    case "1":
        print("Tu nota es: 4.5")

    case "2":
        print("Tu promedio es: 4.2")

    case "3":
        print("Seleccionaste la opción de ayuda.")

    case "4":
        print("Saliendo del programa...")

    case _:
        print("Opción no válida.")


# ==========================================
# 4. NIVEL JEFE - BUG DEL ORDEN
# ==========================================

nota = 5.0

print("\n===== PRUEBA DEL CÓDIGO INCORRECTO =====")

# Código original con el orden incorrecto
if nota >= 3.0:
    print("Aprobado")
elif nota >= 4.5:
    print("Excelente")
else:
    print("Reprobado")


# ==========================================
# CÓDIGO CORREGIDO
# ==========================================

print("\n===== CÓDIGO CORREGIDO =====")

if nota >= 4.5:
    print("Excelente")
elif nota >= 3.0:
    print("Aprobado")
else:
    print("Reprobado")