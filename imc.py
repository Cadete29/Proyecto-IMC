personas = int(input("Ingrese la cantidad de personas: "))

#aqui vamos a verificar que el numero de personas sea mayor a cero
for _ in range (personas):
    #Aqui pediremos el nombre completo 
     nombre = input("Ingrese su nombre por favor: ")
     #Aqui pedimos la edad en años 
     edad = int (input("Ingrese su edad en años por favor: "))
     #aqui pedimos la altura en metros
     altura = float (input("Ingrese su altura en metros porfavor: "))
     #aqui podemos pedir el peso en kilogramos
     masa = float (input("Ingrese su masa en kilogramos por favor: "))
     
     IMC = masa / altura ** 2
     
     if edad < 18:
         print(f"{nombre}, eres menor de edad")
     else:
        print(f"{nombre}, eres mayor de edad")
    
print (f"{nombre}, su IMC es: {IMC}")

#Realizamos las clasificaciones de IMC 
if 0 <= IMC <= 15.99:
    print(f"{nombre}, usted tiene Delgadez severa")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")
elif 16.00 <= IMC <= 16.99:
    print (f"{nombre}, usted tiene Delgadez moderada")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")
elif 17.00 <= IMC <= 18.49:
    print (f"{nombre}, usted tiene Delgadez leve")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")
elif 18.50 <= IMC <= 25.00:
    print (f"{nombre}. usted tiene un IMC Normal")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")
elif 25.00 <= IMC <= 29.00:
    print (f"{nombre}, usted tiene Sobrepeso")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")
elif 30.00 <= IMC <= 34.99:
    print (f"{nombre}, usted tiene Obesidad leve")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")
elif 35.00 <= IMC <= 39.99:
    print (f"{nombre}, used tiene Obesidad media")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")
else:
    print(f"{nombre}, usted tiene una Obesidad morbida")
    print ("Consejos para lograr un IMC normal:")
    print ("-Mantenga una dieta balanceada y nutritiva")
    print ("mantenga un estilo de vida saludable y activa")
    print ("-Realize ejercicio fisico regularmente")