def semana(numero):
    lista = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
    dia = lista[numero-1]
    return(dia)
semana(1)

def piramide (n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

piramide(15)

def compara_numeros(i,j):
    if i == j:
        print("Los numeros son iguales")
    elif i>j:
        print("El primer numero es mayor")
    else:
        print("El segundo numero es mayor")

x= input("dime un numero")
y=input("Dime otro numero")
compara_numeros(x,y)

def contar_letra(texto, letra):
    # Convertir ambos, texto y letra, a minúsculas para hacer la comparación insensible a mayúsculas/minúsculas
    texto = texto.lower()
    letra = letra.lower()
    
    # Contar la cantidad de veces que aparece la letra en el texto
    contador = texto.count(letra)
    
    return contador

texto = "Hola Mundo"
letra = "h"
print(contar_letra(texto, letra))

def contador_letras(cadena):
    # Crear un diccionario para almacenar el conteo de letras
    conteo = {}
    
    # Recorrer cada carácter en la cadena
    for letra in cadena:
        # Ignorar espacios y caracteres no alfabéticos
        if letra.isalpha():
            # Convertir la letra a minúscula para un conteo insensible a mayúsculas
            letra = letra.lower()
            # Incrementar el conteo de la letra en el diccionario
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
    
    return conteo

texto = "Hola pais de nombre pequeño"
resultado = contador_letras(texto)
print(resultado)

def añadir_eliminar(lista,comando,elemento=1):
    if comando == add:
        x = lista[elemento].add()
        print(x)
    else:
        x = lista[elemento].remove()
        print(x)

lista =[1,2,3,4,5,6,7,8,9,10]
elemento=4
añadir_eliminar(lista,"add",5)

def crear_frase(*palabras):
    return ' '.join(palabras)

frase = crear_frase("Hola", "mundo", "esto", "es", "una", "frase")
print(frase)

def fibonaci(x):
    fibonacci = x/(1-x-(x*2))
    print(fibonacci)
fibonaci(5)

def funciones (base, altura):
    area_1 = base * altura
    print(area_1)
    return area_1
def funcion (base,altura):
    area_2 =base * altura/2
    print(area_2)
    return area_2
def func (radio):
    area_3= 3.1416*(radio*2)
    print(area_3)
    return area_3

funciones(4,3)
funcion(5,6)
func(4)



