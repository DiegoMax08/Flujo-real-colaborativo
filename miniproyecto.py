datos = [10, 20, 30, 40, 50]

ordenados = sorted(datos)
mediana = ordenados[len(ordenados) // 2]
print("Mediana:", mediana)

ordenados = sorted(datos)
print("Datos ordenados", ordenados)

pares =[x for x in datos if x % 2 == 0]
print("Cantidad de numeros pares:",
      len(pares))