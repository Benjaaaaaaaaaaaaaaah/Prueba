import random
A = random.randrange(0,50)
B = random.randrange(0,50)
suma = (A + B)
colores = ("amarillo","azul","rojo","blanco","negro","gris","beige","verde","bordo","violeta","celeste","plateado","naranja","marrón","fucsia","rosa")
pjdisney = ("mickey","minnie","pato donald","goofy","daisy","pluto")
utiles = ("mochila","cartuchera","lapices","lapiceras","cuadernos","goma de borrar","resaltador")
todos = (colores+pjdisney+utiles)
secreta = random.choice(todos)
cadena = "-" * len(secreta)
intentos = 0
signo = ("+","-")
signo1 = random.choice(signo)
print ("Vamos a jugar un juego")
print ("Las opciones son: 1)Sumas y Restas 2)Ahorcado")
juego = int(input("Seleccione un juego: "))
if juego == 1:
    print ("Bienvenido al juego de sumar y restar")
    if signo1 == ("+"):
        suma = (A + B)
        print ("Cual es el resultado de la suma",(A),"+",(B))
        rtdo = int(input("El resultado es: "))
        if rtdo == suma:
            print ("El resultado es correcto :D")
        while rtdo != suma:
            print ("El resultado es incorrecto, intenta de nuevo")
            rtdo = int(input("El nuevo resultado es: "))
            if rtdo == suma:
                print ("El resultado es correcto :D")
                break
    else:
        if A > B:
            resta = (A - B)
            print ("Cual es el resultado de la resta",(A),"-",(B))
            rtdo = int(input("El resultado es: "))
            if rtdo == resta:
                print ("El resultado es correcto :D")
            while rtdo != resta:
                print ("El resultado es incorrecto, intenta de nuevo") 
                rtdo = int(input("El nuevo resltado es: "))
                if rtdo == resta:
                    print ("El resultado es correcto :D")
                    break
        else:
            resta = (B - A)
            print ("Cual es el resultado de la resta",(B),"-",(A))
            rtdo = int(input("El resultado es: "))
            if rtdo == resta:
                print ("El resultado es correcto :D")
            while rtdo != resta:
                print ("El resultado es incorrecto, intenta de nuevo") 
                rtdo = int(input("El nuevo resltado es: "))
                if rtdo == resta:
                    print ("El resultado es correcto :D")
                    break    
else: 
    print ("Bienvenidos al juego del ahorcado!")
    while True:
        print (cadena)
        letras = input("Ingrese una letra: ")
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
                print ("Perdiste =( la palabra era:",(secreta))
                break       
        if cadena == secreta:
                print ("Ganaste! la palabra era:",(secreta))
                break
