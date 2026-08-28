# --- 1. LA CALCULADORA TOTAL ---
print("--- 1. CALCULADORA TOTAL ---")
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

print(f"\nResultados para {n1} y {n2}:")
print(f"{'Suma (+):':<15} {n1 + n2:>10}")
print(f"{'Resta (-):':<15} {n1 - n2:>10}")
print(f"{'Multiplicación (*):':<15} {n1 * n2:>10}")
print(f"{'División (/):':<15} {n1 / n2:>10}")
print(f"{'Div. Entera (//):':<15} {n1 // n2:>10}")
print(f"{'Módulo (%):':<15} {n1 % n2:>10}")
print(f"{'Exponente (**):':<15} {n1 ** n2:>10}")

# --- 2. DETECTOR DE NÚMEROS ---
print("\n--- 2. DETECTOR DE NÚMEROS ---")
num = int(input("Ingresa un número entero: "))

es_par = (num % 2 == 0)
es_multiplo_3 = (num % 3 == 0)
esta_en_rango = (1 <= num <= 100) # Comparación encadenada

print(f"¿Es par? {es_par}")
print(f"¿Es múltiplo de 3? {es_multiplo_3}")
print(f"¿Está entre 1 y 100? {esta_en_rango}")

# --- 3. FILTRO DE TIENDA ---
print("\n--- 3. FILTRO DE TIENDA ---")
precio = 45.0
talla = "M"
color = "Negro"
hay_stock = True

# Una sola expresión lógica
cumple_filtro = (precio < 50.0) and (talla == "M") and (color == "Negro") and hay_stock
print(f"Buscamos: Menos de $50, talla M, color Negro y con stock.")
print(f"¿El producto cumple lo que buscas? {cumple_filtro}")

# --- 4. NIVEL JEFE ---
print("\n--- 4. NIVEL JEFE ---")
print("10 / 2  =", 10 / 2)
print("10 // 3 =", 10 // 3)
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)