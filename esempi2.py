
##############################TRIS###########################

import random

lista_player = []
lista = []
lista_computer = []

print("TRIS")

def greet():
    print(lista)

m0c = int(random.randint(0,8))
m01c = int(random.randint(0,8))


def giocatore(scelta0, scelta01):
    scelta0
    if scelta0 in lista:
        for b in lista:
            while scelta0 == b:
                scelta01
                if scelta01 != b:
                    lista.append(scelta01)
                    lista_player.append(scelta01)
    if scelta0 not in lista:
        lista.append(scelta0)
        lista_player.append(scelta0)
    greet()

def computer(choiche0, choiche01):
    choiche0
    if choiche0 in lista:
        for a in lista:
            while choiche0 == a:
                choiche01 = choiche0 = random.randint(0,4)
                if choiche01 != a:
                    print("Il computer scelto: " ,choiche01)
                    lista.append(choiche01)
                    lista_computer.append(choiche01)
    if choiche0 not in lista:
        print("Il computer ha scelto: ", choiche0)
        lista.append(choiche0)
        lista_computer.append(choiche01)
    greet()



print(giocatore((m0p == int(input("mossa 1: "))), (m01p == int(input("riprova: "))))) #mossa 1 giocatore - mossa 1
print(computer(m0c, m01c)) #mossa 1 computer - mossa 2
m1p = int(input("mossa 2: "))
print(giocatore(m1p, m11p)) #mossa 2 giocatore - mossa 3
print(computer(m1c, m11c)) #mossa 2 giocatore - mossa 4
m2p = int(input("mossa 3: "))
print(giocatore(m2p, m21p)) #mossa 3 giocatore - mossa 5
print(computer(m2c, m21c)) #mossa 3 computer - mossa 6
m3p = int(input("mossa 4: "))
print(giocatore(m3p, m31p)) #mossa 4 giocatore - mossa 7
print(computer(m3c, m31c)) #mossa 4 computer - mossa 8
m4p = int(input("mossa 5: "))
print(giocatore(m4p, m41p)) #mossa 5 giocatore - mossa 9
