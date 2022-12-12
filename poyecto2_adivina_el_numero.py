import random

banner = "=" *40

def adivina_el_numero(x):

    print("\b")
    print(banner)
    print("bienvenido (a) al juego")
    print(banner)
    print("\b")
    print("tu meta es adivinar el numero generado por la computadora")

    numero_aleatorio = random.randint(1,x) # numero aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        # el usuario ingresa un numero
        prediccion = int(input(f"adivina un mumero entre 1 y el {x} : ")) # f-string
        if prediccion < numero_aleatorio:
            print("intenta otra vez el numero es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("intenta nuevamente el numero es muy grande.")
    print("\b")        
    print(f"FELICIDADES ADIVINASTE EL NUMERO {numero_aleatorio} CORRECTAMENTE")
    print("\b")

adivina_el_numero(10)
    

