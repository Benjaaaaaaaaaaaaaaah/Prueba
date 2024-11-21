import random

def jugar():
    on = int(input(f"""
                    0)No quiero jugar
                    1)Quiero jugar
                   """))
    return on

def j_suma():
    A,B = random.randint(0,50),random.randint(0,50)
    if B > A:
        A,B = B,A
    signo = ("+","-")
    signo1 = random.choice(signo)
    suma = "y"
    rspt = "x"
    if signo1 == "-":
        while suma != rspt:
            suma = A - B
            print(f"Cual es el resultado de la suma {A} {signo1} {B}")
            rspt = int(input("¿Cual es el resultado? \n"))
            if rspt == suma:
                return print("Ganaste :D")
            else:
                print("Es Incorrecto :C")
    if signo1 == "+":
        while suma != rspt:
            suma = A + B
            print(f"Cual es el resultado de la suma {A} {signo1} {B}")
            rspt = int(input("¿Cual es el resultado? \n"))
            if rspt == suma:
                    return print("Ganaste :D")
            else:
                print("Es Incorrecto :C")
        
def adv_num():
    A,B = random.randint(0,50),random.randint(0,50)
    if B > A:
        A,B = B,A
    signo = ("+","-")
    signo1 = random.choice(signo)
    suma = "y"
    rspt = "x"
    if signo1 == "+":
        while suma != rspt:
            suma = A + B
            print(f"Que numero falta para completar la operacion:\n{A} + ? = {suma}")
            rspt = int(input())
            if rspt == B:
                return print("Ganaste :D")
            else: 
                print("El numero es incorrecto :C")
    elif signo1 == "-":
        while suma != rspt:
            suma = A - B
            print(f"Que numero falta para completar la operacion:\n{A} - ? = {suma}")
            rspt = int(input())
            if rspt == B:
                return print("Ganaste :D")
            else: 
                print("El numero es incorrecto :C")
                
def ahorcado():
    colores = ("amarillo","azul","rojo","blanco","negro","gris","beige","verde","bordo","violeta","celeste","plateado","naranja","marrón","fucsia","rosa")
    pjdisney = ("mickey","minnie","pato donald","goofy","daisy","pluto")
    utiles = ("mochila","cartuchera","lapices","lapiceras","cuadernos","goma de borrar","resaltador")
    todos = (colores+pjdisney+utiles)
    secreta = random.choice(todos)
    cadena = "-" * len(secreta)
    intentos = 0
    while cadena != secreta:
            print (cadena)
            letras = input("Ingrese una letra: ")
            if letras == secreta:
                print(f"La palabra era {secreta}")
                return print("Ganaste :D")
            if letras in secreta:
                for i in range(len(secreta)):
                    if secreta[i] == letras:
                        cadena = cadena[:i] + letras + cadena[i+1:]
            else:
                intentos += 1
                if intentos == 1:
                    print ("O")
                elif intentos == 2:
                    print (" O")
                    print ("/")
                elif intentos == 3:
                    print (" O")
                    print ("/|")
                elif intentos == 4:
                    print (" O")
                    print ("/|\\")
                elif intentos == 5:
                    print (" O")
                    print ("/|\\")
                    print ("/")
                elif intentos == 6:
                    print (" O")
                    print ("/|\\")
                    print ("/ \\")
                    return print ("Perdiste =( la palabra era:",(secreta))           
            if cadena == secreta:
                return print ("Ganaste! la palabra era:",(secreta))
        


jugar1 = 1
while jugar1 == 1:
    print ("Vamos a jugar un juego")
    print ("Las opciones son: 1)Sumas y Restas 2)Ahorcado 3)Adivina el numero")
    juego = int(input("Seleccione un juego: "))
    if juego == 1:
        print("Bienvenido al juego de sumas")
        j_suma()
    elif juego == 2: 
        print ("Bienvenidos al juego del ahorcado!")
        ahorcado()
    elif juego == 3:
        print ("Bienvenido al juego de adivinar el numero")
        adv_num()             
    jugar1=jugar()
else:
    print ("Gracias por jugar :D")