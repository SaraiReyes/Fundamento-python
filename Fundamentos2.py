#   if
dato=10
if dato>0 and dato<9:
    print(f'{dato} es mayor qué 0 y menor qué 9')
elif dato>10 :
    print(f'{dato} es mayor qué 10')
else:
    print(f'{dato} es menor qué 0')


################################################################################################################

#   Arrays (listas)
arrelo=["Computadora","Mouse",1,4.1,2,True]
print(arrelo) #imprimir todo el arreglo
print(arrelo[1])#imprimir una posición
print(arrelo[2:5])# imprimir de x a y posición
print(arrelo[3:])# imprimir de x posición hasta terminar el arreglo

################################################################################################################


#   Funciones en listas
arrelo=["Computadora","Paleta","Mouse",1,4.1,2,True]
print(len(arrelo))
arrelo.append(8)#agregar al final
print(arrelo)
arrelo.insert(2,"Hola")#agregar en x posición un elemento
print(arrelo)
arrelo.extend(["valor",50,False])#agregar un conjunto de elementos al final
print(arrelo)
# concatenacion
arrelo1=["Paleta","Mouse",1,4.1,2,True]
arrelo2=["Nuevo",5,6,False]
arreglo3=arrelo1+arrelo2
print(arreglo3)
# buscar un valor
print("Paleta" in arreglo3)
print("c" in arreglo3)
#buscar posicion
print(arreglo3.index("Paleta"))
#cantidad de veces que se repite un valor
print(arreglo3.count("Paleta"))
#Borrar datos
arreglo3.remove("Nuevo")
print(arreglo3)
#camniar valor cambia la última posición por la primera
arreglo3.reverse()
print(arreglo3)
#Borrar todo
arreglo3.clear()
print(arreglo3)

## Ordenar
arreglo3=[2,9,3,0,1,6,24]
print(arreglo3)
arreglo3.sort()# de menor a mayo
print(arreglo3)
arreglo3.sort(reverse=True)# de mayora menor
print(arreglo3)


################################################################################################################
#   While
numero=0
while numero<10:
    numero+=1
    print(numero)

digito=int(input("Dame un número mayor a 10: "))
while digito<10:
    print("por favor ingresa un número mayor a 5: ")
    digito=int(input("Dame un número mayor a 5 "))

print("el cuadrado de ese número es ",digito**2)
################################################################################################################
#   for

for i in [1,7,3,7,2,7,1]:
    print(f'El valor es {i}')
# sumar los números de 1 añ 100
resultSuma=0
# range lo que hace es tomar el valor que le das y retrocede 1 hasta llegar a 0
for i in range(101):
    resultSuma+=i;

print(f'La suma total de todos los números del 0 al 100 {resultSuma}')
################################################################################################################
# conjuntos

conjuntoa={2,5,3,7}
conjuntob={5,9,3,1}
# comparación
print(conjuntoa==conjuntob)
# Unión
print(conjuntoa|conjuntob)
# intersección
print(conjuntoa&conjuntob)
# diferencia
print(conjuntoa-conjuntob)
print(conjuntob-conjuntoa)
# diferencia simetrica
print(conjuntoa^conjuntob)
