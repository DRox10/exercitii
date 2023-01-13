'''
import _thread, time

def functie(i):
    id_thread = _thread.get_ident()
    print(f"Hello din functie de la threadul numarul {i} din threadul {id_thread}")

for i in range(10):
    _thread.start_new_thread(functie, (i,))
    time.sleep(0.01)

time.sleep(1)
'''
'''
from os import fdatasync
import threading

#Varianta 1
def functie(x):
    print(f"Hello din functie, varianta 1: x = {x}")

t1 = threading.Thread(target = functie, args=(4,))
t1.start()


#Varianta 2
t2 = threading.Thread(target = lambda a,b: print(f"Varianta 2: a+b = {a+b}"), args = (4,5))
t2.start()


#Varianta 3
def func(a,b):
    print(f"Varianta 3: a+b= {a+b}")
t3 = threading.Thread(target = func, args = (4,5))
t3.start()

#####################################

class CustomThread(threading.Thread):
    def __init__(self, numar):
        super().__init__()
        self.numar = numar 
    def run(self):
        print(f"Hello din Custom Thread numar = {self.numar}")

for i in range(10):
    t = CustomThread(i)
    t.start()

'''

#--------------------EXERCITIUL CU MELCUL-------------------------
'''
import time, random, threading, os



class Melc(threading.Thread):
    FINISH = 20
    POZITIE = {

    }
    lock = threading.Lock()
   
    def __init__(self, numar):
        super().__init__()
        self.numar = numar 
        self.nume = f"M{self.numar}"
        Melc.POZITIE[self.nume] = 0

    def r(self):
        return random.randint(1,3)

    @staticmethod
    def printMelci():
        os.system('cls')
        for melc in Melc.POZITIE.keys():
            print(f"{melc}".rjust(Melc.POZITIE[melc]).ljust(Melc.FINISH)+"|")


    def run(self):
        self.initial = len(self.nume)
        while self.initial < self.FINISH:
            with Melc.lock:
                self.initial = Melc.POZITIE[self.nume]
                self.initial += self.r()
                Melc.POZITIE[self.nume] = self.initial
                Melc.printMelci()
            time.sleep(self.r())
        else:
            print(f"Melcul {self.nume} a terminat!!")

melci = [ Melc(i+1).start() for i in range(3)]
print(melci)

'''
#-------------------------TEMA---------------------------------------
# Creati u program care porneste 5 fire. 
# Fiecare fir alege un nr intamplator de la 1-10.
# Dupa ce termina toate firele, se aduna toate valorile generate.

import threading
import random
import time
import os

'''
class Fire(threading.Thread):
    def __init__(self, nume):
        super().__init__()
        self.nume = nume

    def r(self):
        return random.randit(1,10)
        print(f"{self.nume} a ales nr ")

Fir1 = Fire
'''
#-----------------------Varianta 1

suma = 0
lock = threading.Lock()

#Generare nr random
def generareNr(l):
    nr = random.randint(1,10)
    print(f"Numarul generat este {nr}")
    with l:
        global suma
        suma += nr

#crearea firelor:
for i in range(5):
    t = threading.Thread(target=generareNr, args=(lock,))
    t.start()

time.sleep(1)
print(suma)

#----------------------Varianta 2

class GenerareNumar(threading.Thread):
    suma = 0
    lock = threading.Lock()
    def run(self):
        nr = random.randint(1, 10)
        print(f"Numarul generat este {nr}")
        with GenerareNumar.lock:
            GenerareNumar.suma += nr

for i in range(5):
    t = GenerareNumar()
    t.start()

time.sleep(1)
print(GenerareNumar.suma)
