#pip install -U pylint --user para autoayuda

#imprimir en consola
print("hola mundo")
##########################################################################################################
# tipos de datos

#texto
texto="Hola"
texto2='Hola'
#boleanos
falsoVerdadero=False #True || False
#numeros
numero=5
numerodecimal=5.2
# imprimir número y el tipo de dato que python reconoce
print(texto, type(texto))
print(texto2, type(texto2))
print(falsoVerdadero, type(falsoVerdadero))
print(numero, type(numero))
print(numerodecimal, type(numerodecimal))

##########################################################################################################
# Operadores
    # Aritmeticos
'''
+       suma
-       resta
*       multiplicación
**      potencia
/       división
//      división entera
%       módulo

'''
n1=4
n2=56.3
suma=n1+n2
resta=n2-n1
multiplicacion=n1*n2
division=n2/n1
divisionEntera=n2//n1
potencia=5**2
modulo=9%3

print("la suma es",suma)
print("la resta es",resta)
print("la multiplicación es",multiplicacion)
print("la división es",division)
print("la división entera es es",divisionEntera)
print("la potencia es",potencia)
print("el módulo es",modulo)

##########################################################################################################
# variables dinámicas
dato=50
print(dato)
dato="Cambio"
print(dato)

'''
Esto tambien es un comentario
pero este puede ser multilínea
'''
##########################################################################################################
# Operadores
    #relacionales
'''
==      igual que
!=      distinto de
<       menor que
<=      menor o igual que
>       mayor que
>=      mayor o igual que
'''
comparacion = 50 == 100
distinto= 50!=100
menor=50<100
menor1=50<=100
mayor=50>100
mayor1=50>=100
print("50 es igual que 100?: ",comparacion)
print("50 es distinto de 100?: ",distinto)
print("50 es menor o igual que 100?: ",menor)
print("50 es menor que 100?: ",menor1)
print("50 es mayor que 100?: ",mayor)
print("50 es mayor o igual que 100?: ",mayor1)
##########################################################################################################
#operadores 
    #lógicos
'''
and     si se cumplen ambas condiciones
or      si se cumple alguna de las doscondiciones
not     negación a una condición

'''
a=30
b=50
c=10

opand=((a<b)and(c<b))
opor=((a>b)or(c<b))
opnot=not (((a>b)or(c<b)))

print('(a menor qué b ) y (c menor qué b)',opand)
print('(a mayor qué b ) o (c menor qué b)',opor)
print('Negamos el resulatdo de= (a menor qué b ) y (c menor qué b)',opnot)
##########################################################################################################
#operadores 
    #de adignación
'''
variable= variable +1
variavle +=1                suma
variavle -=1                resta
variavle *=1                multiplicación
variavle /=1                división
variavle **=1               potencia
variavle %=1                módulo 
'''
c=1
c=c+1
print('valor ',c)
c+=1
print('valor ',c)
c-=1
print('valor ',c)
c*=3
print('valor ',c)
c/=3
print('valor ',c)
c**=3
print('valor ',c)
c%=2
print('valor ',c)
##########################################################################################################
#   datos de salida
app="pyhton"
proyecto="nuevo"

print(f"La app en {app} se llamará {proyecto}")
###########################################################################################################
#   entrada de datos
## string
pedirDatos=input("Dame un nombre: ")
print("el nombre es ",pedirDatos)
## número
pedirNum=int(input("Dame un nombre: "))
print("el número es ",pedirNum+1)

## decimla
pedirdec=float(input("Dame un nombre: "))
print("el número es ",pedirdec+1)