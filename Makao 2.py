import random
import time
import sys
def print_delay(text,delay=0.02):
    for char in text:
        print (char,end="",flush=True)
        time.sleep(delay)
    print('\n',end="")

class talia: #talia w grze
    def __init__(self, karty):
        self.karty = karty

    def wyswietl(self):
        print (self.karty)

    def losowanie(self): #losuje, zwraca i usuwa kartę z talii
        karta = random.choice(self.karty)
        self.karty.remove(karta)
        return karta

class reka:#karty na rece gracza
    def __init__(self, karty):
        self.karty = karty

    def dobierz(self, nowa_karta):
        self.karty.append(nowa_karta)

    def wybor(self,karta=1000):
        print_delay ("Twoje karty: "+ str(self.karty),0.01)
        #karta=1000           
        while karta not in range(len(self.karty)):
            karta = input("Wybierz kartę (1-" + str(len(self.karty))+") lub dobierz (0): ")
            karta = int(karta)
            if karta==0:
                print_delay("dobierasz kartę")
                return 0
            karta -=1
            print_delay('wybrales: '+str(self.karty[int(karta)]))
        return self.karty[karta]

    def usun(self,usun):
        self.karty.remove(usun)

    def wyswietl(self):
        print_delay (self.karty)

class stos: #stos zagranych kart 
    def __init__(self, karty):
        self.karty = karty

    def dodanie(self,nowa_karta):
        self.karty.append(nowa_karta)

    def tasowanie(self, karty, nowa_karta):
        karty=[]
        karty.append(nowa_karta)            

    def wyswietl(self):
        print(self.karty)


#ROZGRYWKA
    #PRYGOTOWANIE TALII

figury=['dwójka','trójka','czwórka','piątka','szóstka','siódemka','ósemka','dziewiątka','dziesiątka','walet','dama','król','as']
kolory=['pik','trefl','karo','kier']
talia_bazowa=[]
for figura in figury:
    for kolor in kolory:
        talia_bazowa.append(figura +' '+ kolor)

talia_uzyta = talia(talia_bazowa)

#nastepna_karta = talia_uzyta.losowanie()
#print(nastepna_karta)
#talia_uzyta.wyswietl()   
 
    #ROZDANIE KART
gracz1 = reka([])
gracz2 = reka([])

for x in range(5):
    gracz1.dobierz(talia_uzyta.losowanie())
    gracz2.dobierz(talia_uzyta.losowanie())
    
stos_kart = stos([])
stos_kart.dodanie(talia_uzyta.losowanie())
#print ("Karta na stole to: " + stos_kart.karty[-1])
#gracz1.wyswietl()
#gracz2.wyswietl()
#talia_uzyta.wyswietl()

    #ROZGRYWKA WŁAŚCIWA
tura=0
while len(gracz1.karty) > 0 or len(gracz2.karty) > 0:
    tura+=1 #WARUNKI ZAKOŃCZENIA GRY
    print_delay ('\ngramy dalej')
    print_delay ("Karta na stole to: " + stos_kart.karty[-1])
    rzucona_karta = gracz1.wybor()
    def rzucanie_karty(rzucona_karta):
        x,y = stos_kart.karty[-1].split(' ')
        a,b = [' ',' ']
        while x != a and y != b: #SPRAWDZENIE CZY KARTA PASUJE DO TEJ NA STOSIE
            a,b = rzucona_karta.split(' ')
            if x != a and y != b:
                print_delay("Nie możesz rzucić tej karty!")
                rzucona_karta = gracz1.wybor()
            else:
                pass
        gracz1.usun(rzucona_karta)
        #gracz1.wyswietl()
        stos_kart.dodanie(rzucona_karta)
        #stos_kart.wyswietl()
    if rzucona_karta!=0:
        rzucanie_karty(rzucona_karta)
    else:
        print_delay("dobieraniekarty.exe")
print_delay ("WYYGRAŁEŚ! Skonczyłeś grę w "+str(tura)+" turach",0.05)