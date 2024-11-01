import random
import time
import json
import os

def load_language(filename):
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_folder, f'{filename}.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
language = load_language("eng")
def txt(key):
    return language.get(key,key)

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
            print_delay (f"{txt('your_cards')}"+ str(self.karty),0.005)
            karta = input(f"{txt('you_choose').format(len(self.karty))}")
            try:
                karta = int(karta)
                if karta==0:
                    print_delay(f"{txt('you_draw')}")
                    return 0
                karta -=1
                try:
                    print_delay(f"{txt('your_choice')}"+str(self.karty[int(karta)]))
                except IndexError:
                    print_delay(f"{txt('index_error')}")
            except ValueError:
                print_delay(f"{txt('value_error')}")
        return self.karty[karta]
    
    def auto_wybor(self,karta=1000):
        zakres = len(self.karty)
        print_delay (f"{txt('pc_cards')}"+ str(len(self.karty)),0.005)
        karta = int(zakres)

        x,y = stos_kart.karty[-1].split(' ')
        a,b = [' ',' ']
        while x != a and y != b:  
            karta += -1
            rzucona_karta=self.karty[karta]
            a,b = rzucona_karta.split(' ')
            if karta==0:
                print_delay(f"{txt('pc_draws')}")
                return 0
            else:
                pass
        print_delay(f"{txt('pc_choice')}"+str(self.karty[int(karta)]))
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

#MECHANIKI MENU
def menu():
    print_delay(f"{txt('menu')}")
    nawiguj = 0
    while nawiguj not in (1,2,3):
        try:
            nawiguj=int(input(f"{txt('menu_nav')}"))
        except ValueError:
            pass
    return nawiguj

def zasady():
    print_delay(f"{txt('rules')}")
    nawiguj = 0
    while nawiguj not in (1,2):
        try:
            nawiguj = int(input(f"{txt('menu_nav')}"))
        except ValueError:
            pass
    return nawiguj

def jezyk():
    print_delay(f"{txt('languages')}")
    nawiguj = 0
    global language
    while nawiguj not in (1,2):
        try:
            nawiguj = int(input(f"{txt('lan_nav')}"))
        except ValueError:
            pass
    if nawiguj==1:
        language=load_language('pl')
    elif nawiguj==2:
        language=load_language('eng')
    return language

def nawigacja():
    nawiguj = menu()
    if nawiguj==3:
        jezyk()
        nawigacja()
    elif nawiguj==2:
        nawiguj = zasady()
        if nawiguj==2:
            nawigacja()
        elif nawiguj==1:
            pass
    elif nawiguj==1:
        pass

#WYWOŁANIE MENU
nawigacja()
#ROZGRYWKA
    #PRYGOTOWANIE TALII
figury=txt('figures')
kolory=txt('colors')
talia_bazowa=[]
for figura in figury:
    for kolor in kolory:
        talia_bazowa.append(figura +' '+ kolor)

talia_uzyta = talia(talia_bazowa) 
 
    #ROZDANIE KART
gracz1 = reka([])
gracz2 = reka([])

for x in range(5):
    gracz1.dobierz(talia_uzyta.losowanie())
    gracz2.dobierz(talia_uzyta.losowanie())
    
stos_kart = stos([])
stos_kart.dodanie(talia_uzyta.losowanie())

    #ROZGRYWKA WŁAŚCIWA
def tura_gracza(rzucona_karta):
    if rzucona_karta!=0:
        x,y = stos_kart.karty[-1].split(' ')
        a,b = [' ',' ']
        if x != a and y != b: #SPRAWDZENIE CZY KARTA PASUJE DO TEJ NA STOSIE
            a,b = rzucona_karta.split(' ')
            if x != a and y != b:
                print_delay(f"{txt('wrong_card')}")
                tura_gracza(rzucona_karta = gracz1.wybor())
            else:
                gracz1.usun(rzucona_karta)
                stos_kart.dodanie(rzucona_karta)
    else:
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
    if talia_uzyta.policz()==0: #sprawdzanie czy talia jest niepusta 
        talia_uzyta = talia(stos_kart.karty)
        stos_kart=stos([talia_uzyta.karty[-1]])
        talia_uzyta.usun(talia_uzyta.karty[-1])
    
    print_delay (f"{txt('current_card')}" + stos_kart.karty[-1])
    tura_gracza(gracz1.wybor())
    if len(gracz1.karty)==0:
        print_delay (f"{txt('win_credits').format(str(tura))}",0.1)
        break
    tura_PC(gracz2.auto_wybor())
    if len(gracz2.karty)==0:
        print_delay (f"{txt('loose_credits').format(str(tura))}",0.1)
        break


