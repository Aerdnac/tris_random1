import random

print("TRIS")

lista_player = []
lista = []
lista_computer = []

def greet():
    print(lista)
#m0p vuol dire mossa (m) numero 0 del giocatore = player (p)
m0p = int(input("mossa 1: "))
lista_player.append(m0p)
lista.append(m0p)

if 0 <= m0p <= 8:
    m0c = int(random.randint(0,8))
    if m0c in lista:
        m01c = int(random.randint(0,8)) 
        lista.append(m01c)
        lista_computer.append(m01c)
        print("Il computer ha scelto: ", m01c)
    else:
        print("il computer ha scelto: ", m0c)
        lista.append(m0c)
        lista_computer.append(m0c)
    greet()

    m1p = int(input("mossa 2: "))
    if m1p in lista:
        m01p = int(input("Questo numero è stato già selezionato, scegline uno diverso. Numero: "))
        lista.append(m01p)
        lista_player.append(m01p)
         
    if  m1p > 8 or m1p < 0:
        m01p = int(input("Questo numero non è tra 0 e 8, scegli altro"))
        lista.append(m01p)
        lista_player.append(m01p)
    else:
        lista.append(m1p)
        lista_player.append(m1p)
    
    m1c = int(random.randint(0,8))
    if m1c in lista:
        for x in lista:
            while x not in lista:
                m11c = int(random.randint(0,8))
                lista.append(m11c)
                lista_computer.append(m11c)
        print("Il computer ha scelto", m11c)
    else:
        lista.append(m1c)
        lista_computer.append(m1c)
        print("Il computer ha scelto", m1c)
    greet()


