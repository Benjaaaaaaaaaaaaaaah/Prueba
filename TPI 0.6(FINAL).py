import random

def jugar():
    on = int(input(f"""
                    0)No quiero jugar
                    1)Quiero jugar
                   """))
    if on != 1 and on != 0:
        print("El número seleccionado no se encuentra, elije otra vez")
        return jugar()
    if on == 1 or on == 0:
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
            print(f"Cual es el resultado de la resta {A} {signo1} {B}")
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

def multi():
    A,B = random.randint(1,10), random.randint(1,10)
    multiresp1 = A*B
    vidas = 3
    rspt = "no"
    while rspt != multiresp1:
        print(f"Cual es el resultado de está multiplicación: {A} x {B}")
        rspt = int(input())
        if multiresp1 == rspt:
            return print("Es Correcto :D")
        else:
            vidas -= 1
            print("Es incorrecto :C")
            print(f"Te quedan {vidas} intentos")
        if vidas == 0:
            return print("perdiste")
        
def divi():
    A,B = random.randint(1,90), random.randint(1,10)
    while A % B != 0:
        A,B = random.randint(1,90), random.randint(1,10)
    if A < B:
        A,B = B,A
    div = A / B
    rspt = "no"
    while div != rspt:
        print(f"Cual es el resultado de esta division {A} / {B}")
        rspt = int(input())
        if div == rspt:
            return print("Es Correcto :D")
        else:
            print("Es Incorrecto :C")

def ingles():
    color = ["rojo","verde","amarillo","azul","blanco","negro","rosa"]
    color_ingles = ["red","green","yellow","blue","white","black","pink"]
    color_desfM = random.choice(color)
    color_desfO = color_ingles[color.index(color_desfM)]
    color_elegido = []
    rmdele = random.randint(1,2)
    while color_elegido != color_ingles:
        print(f"¿Como se dice este color en ingles {color_desfM}? ")
        if rmdele == 1:
            print(f"""
                1){color_desfO}
                2){random.choice(color_ingles)}
                """)
            color_elegido = int(input("Elige la opción: "))
            if color_elegido == 1:
                print("Es Correcto :D")
                color_elegido = color_ingles
            elif color_elegido == 2:
                print("Es Incorrecto :C")
                color_elegido = color_ingles
            else:
                print("el número seleccionado no esta en las opcciónes")
        else:
            print(f"""
                1){random.choice(color_ingles)}
                2){color_desfO}
                """)
            color_elegido = int(input("Elige la opción: "))
            if color_elegido == 2:
                print("Es Correcto :D")
                color_elegido = color_ingles
            elif color_elegido == 1:
                print("Es Incorrecto :C")
                color_elegido = color_ingles
            else:
                print("el número seleccionado no esta en las opcciónes")
    


jugar1 = 1
while jugar1 == 1:
    print ("Vamos a jugar un juego")
    print ("""Las opciones son: 
                        1)Sumas y Restas 
                        2)Ahorcado 
                        3)Adivina el número 
                        4)Multiplicación
                        5)División
                        6)Colores en Ingles""")
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
    elif juego == 4:
        print("Bienvenido al juego de multipicacion")
        multi()   
    elif juego == 5:
        print("Bienvenido al juego de división")
        divi()
    elif juego == 6:
        print("Bienvenido al juego de Ingles")
        ingles()
    else:
        print ("Gracias por jugar :D")
    jugar1=jugar()