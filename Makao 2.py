import random
import time

def print_delay(text,delay=0.01):
    for char in text:
        print (char,end="",flush=True)
        time.sleep(delay)
    print('\n',end="")

class talia: #talia w grze
    def __init__(self, karty):
        self.karty = karty

    def wyswietl(self):
        print (self.karty)

    def policz(self):
        #print (len(self.karty))
        return(len(self.karty))

    def losowanie(self): #losuje, zwraca i usuwa kartę z talii
        karta = random.choice(self.karty)
        self.karty.remove(karta)
        return karta
    
    def usun(self,karta):
        self.karty.remove(karta)

class reka:#karty na rece gracza
    def __init__(self, karty):
        self.karty = karty

    def dobierz(self, nowa_karta):
        self.karty.append(nowa_karta)

    def wybor(self,karta=1000):           
        while karta not in range(len(self.karty)):
            print_delay ("Twoje karty: "+ str(self.karty),0.005)
            karta = input("Wybierz kartę (1-" + str(len(self.karty))+") lub dobierz (0): ")
            try:
                karta = int(karta)
                #print ("id "+str(karta))
                if karta==0:
                    print_delay("dobierasz kartę")
                    return 0
                karta -=1
                try:
                    print_delay('wybrales: '+str(self.karty[int(karta)]))
                except IndexError:
                    print_delay("\nNie masz tylu kart")
            except ValueError:
                print_delay("\nWpisz cyfrę")
        return self.karty[karta]
    
    def auto_wybor(self,karta=1000):
        zakres = len(self.karty)
        #print(zakres)
        print_delay ("Karty PC: "+ str(len(self.karty)),0.005)#+ str(self.karty)
        karta = int(zakres)

        x,y = stos_kart.karty[-1].split(' ')
        a,b = [' ',' ']
        while x != a and y != b:  
            karta += -1
            #print("test karty"+str(karta))
            #print(karta)
            rzucona_karta=self.karty[karta]
            a,b = rzucona_karta.split(' ')
            #print(a+b)
            if karta==0:
                print_delay("PC dobiera kartę")
                return 0
            else:
                pass
        print_delay('PC wybrał: '+str(self.karty[int(karta)]))
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
def rzucanie_karty(rzucona_karta):
    if rzucona_karta!=0:
        x,y = stos_kart.karty[-1].split(' ')
        a,b = [' ',' ']
        if x != a and y != b: #SPRAWDZENIE CZY KARTA PASUJE DO TEJ NA STOSIE
            a,b = rzucona_karta.split(' ')
            if x != a and y != b:
                print_delay("\nNie możesz rzucić tej karty!")
                rzucanie_karty(rzucona_karta = gracz1.wybor())
            else:
                gracz1.usun(rzucona_karta)
                #gracz1.wyswietl()
                stos_kart.dodanie(rzucona_karta)
                #stos_kart.wyswietl()
    else:
        print_delay("dobieraniekarty.exe")
        gracz1.dobierz(talia_uzyta.losowanie())

def tura_PC(rzucona_karta):
    if rzucona_karta!=0:
        gracz2.usun(rzucona_karta)
        stos_kart.dodanie(rzucona_karta)
    else:
        gracz2.dobierz(talia_uzyta.losowanie())


tura=0
while len(gracz1.karty) > 0 and len(gracz2.karty) > 0: #WARUNKI ZAKOŃCZENIA GRY
    tura+=1 
    #print(talia_uzyta.policz())
    if talia_uzyta.policz()==0: #sprawdzanie czy talia jest niepusta 
        #print (stos_kart.karty)
        talia_uzyta = talia(stos_kart.karty)
        stos_kart=stos([talia_uzyta.karty[-1]])
        talia_uzyta.usun(talia_uzyta.karty[-1])
        #print (talia_uzyta.karty)
    
    print_delay ('\ngramy dalej')
    print_delay ("Karta na stole to: " + stos_kart.karty[-1])
    rzucanie_karty(gracz1.wybor())
    if len(gracz1.karty)==0:
        print_delay ("\n------WYYGRAŁEŚ!------\nSkonczyłeś grę w "+str(tura)+" turach\n------GRATULACJE------",0.1)
        break
    tura_PC(gracz2.auto_wybor())
    if len(gracz2.karty)==0:
        print_delay ("\n------PC WYGRAŁ------\nSkonczyłeś grę w "+str(tura)+" turach\n-------------------",0.1)
        break


