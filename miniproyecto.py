print("Análisis estadístico de datos")

datos = [10, 20, 30, 40, 50]

print("Datos:", datos)

suma = sum(datos)
print("Suma:", suma)

promedio = sum(datos) / len(datos)
print("Promedio:", promedio)

cantidad = len(datos)
print("Cantidad de datos:", cantidad)

print("\n--- Resultados del análisis ---")

maximo = max(datos)
print("Máximo:", maximo)

minimo = min(datos)
print("Mínimo:", minimo)

rango = max(datos) - min(datos)
print("Rango:", rango)

print("\n--- Operaciones extra sobre los datos ---")
ordenados = sorted(datos)
mediana = ordenados[len(ordenados) // 2]
print("Mediana:", mediana)

ordenados = sorted(datos)
print("Datos ordenados", ordenados)

pares =[x for x in datos if x % 2 == 0]
print("Cantidad de numeros pares:",
      len(pares))
