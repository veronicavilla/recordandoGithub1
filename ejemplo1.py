#soy un comentario de linea
nombreUsuario="Verónica Montoya"
edadUsuario=26
estatura=1.60
esHinchaDeAlgunEquipo=True #esto es un comentario de bloque(''')

print(f"Su nombre es: {nombreUsuario} y tiene {edadUsuario} años.")

comidasFavoritas=["Frijoles", "pasta", "mazamorra", "pizza"]
print(comidasFavoritas)
print(comidasFavoritas[2])

#Entradas por teclado:
lugarTrabajoUsuario=input("Digita el lugar de trabajo: ")
print(f"Usted trabaja en {lugarTrabajoUsuario}")
numeroUno=int(input("Digita un numero: "))
numeroDos=int(input("Digita un segundo numero: "))
sumatoriaDeLosNumeros=numeroUno + numeroDos
print(f"La suma {numeroUno} + {numeroDos} = {sumatoriaDeLosNumeros}")