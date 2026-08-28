# --- 1. CALCULADORA DE PROMEDIO ---
print("--- 1. CALCULADORA DE PROMEDIO ---")
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
print(f"El promedio de tus notas es: {promedio:.2f}")

# --- 2. FICHA DE PERFIL ---
print("\n--- 2. FICHA DE PERFIL ---")
nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
ciudad = input("¿De qué ciudad eres? ")

print(f"¡Hola! Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}. Si las matemáticas no fallan, cumpliré 30 años en el año {2026 + (30 - edad)}.")

# --- 4. NIVEL JEFE: TABLA DE ESTUDIANTES ---
print("\n--- 4. NIVEL JEFE: TABLA DE ESTUDIANTES ---")
print(f"{'NOMBRE':<12} | {'EDAD':<5} | {'CIUDAD':>12}")
print("-" * 35)
print(f"{'Ana':<12} | {22:<5} | {'Bogotá':>12}")
print(f"{'Carlos':<12} | {25:<5} | {'Medellín':>12}")
print(f"{'Sofía':<12} | {19:<5} | {'Armenia':>12}")