#1.  Sõna/Lause
from string import punctuation
vokaali=["a","o","e","i","u","õ","ä","ö","ü","y"]
konsonanti="t,w,q,r,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,"
märkid=punctuation
v=k=m=t=0
tekst=input("Sisestage sõna või lause: ").lower()
tekst_list=list(tekst)
for sümbol in tekst_list:
    if sümbol in vokaali:
        v+=1
    elif sümbol in konsonanti:
        k+=1
    elif sümbol in märkid:
        m+=1
    elif sümbol==" ":
        t+=1
print("Vokaali: ",v) 
print("Konsonanti:", k) 
print("Kirjuvahemärgid: ",m) 
print("Tühikud: ",t)

#2.  Loetelu
nimed=[] 
for i in range(5):
    nimi=input("Sisesta nime: ").capitalize()
    nimed.append(nimi)
nimed.sort()
print("Nimed tähestikulises järjekorras: "+str(nimed))
print("Viimati lisatud nimi: "+str(nimed[-1]))
index=int(input("Sisestage nimi, mida soovite kustutada: ")) 
new_nimi=input("Sisesta nimi: ")
nimed[index]=new_nimi 
print("Nimede loetelu: "+str(nimed)) 
uued_nimed=[] 
for nimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
print("Loetelu ilma identsete nimedeta: ",uued_nimed)

vanused=[]
for i in range(5):
    vanus=int(input("Sisestage oma vanus: "))
    vanused.append(vanus) 
vanused.sort() 
print("Vanuste loend: "+str(vanused)) 
maksimum=max(vanused) 
minimum=min(vanused) 
summa=sum(vanused) 
keskmine=summa/len(vanused)
print("Maksimum: "+str(maksimum), "Minimum: "+str(minimum), "Summa: "+str(summa), "Keskmine: "+str(keskmine))
for i in range(5):
    print(nimed[i], "on" , vanused[i], "aastat vana")


#3. Tärnid
from random import *
arvud=[] 
N=int(input("Mitu rida joonistame? ")) 
S=input("Sisesta sümbol: ") 
#loendi täitmine
for p in range (N):
    arvud.append(randint(1,100))
#diagrammi loomine
for p in range(N):
    print(arvud[p]*S) 


#4. Postiindex
Indeksid=["Tallinn", "Narva, Narva-Jõesuu", "Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn",
          "Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "Pärnumaa",
          "Läänemaa, Hiiumaa, Saaremaa"] 
while True:
    while True:
        try:
            indeks=int(input("Sisesta viienubriline indeks: ")) 
            #10000,15478,98854
            #if 10000<=indeks<=99999
            indeks_elemendide_arv=len(str(indeks)) 
            if indeks_elemendide_arv==5:
                print("5 numbriline indeks:  ") 
                break
            else:
                print("On vaja 5 numbriline arv (indeks)") 
        except:
            print("Vale andmetüüp!")
        arv1=indeks//10000
        print(arv1)       
        symbolid=list(str(indeks)) 
        print(f"Sa elad piirkonnas {Indeksid[int(symbolid[0])-1]}") 


#5. Vahetus
from random import *
from string import *
nimekirja=[] 
N=randint(2,35) 
for i in range(N):
    nimekirja.append(choice(ascii_uppercase)) 
print(nimekirja) 
kogus=int(input("Mitu elemendi vahetame oma vahel: "))
if len(nimekirja)//2>=kogus:
    for i in range(kogus):
        a=nimekirja[i] 
        nimekirja[i]=nimekirja[len(nimekirja)-i-1] 
        nimekirja[len(nimekirja)-1-i]=a 
print(nimekirja)

#6. Бесполезные числа
from random import *
nimekirja1=[]
nimekirja=[] 
N=int(input("Sisestage numbrite pikkus: "))
for i in range(N):
    arv=randint(10,100)
    nimekirja1.append(arv)
    nimekirja.append(arv)
maksimum=nimekirja[0]
for arv in nimekirja:
    if arv>maksimum:
        maksimum=arv
        useless_number=maksimum/len(nimekirja) 
for i in range(len(nimekirja)):
    if nimekirja[i]==maksimum:
        nimekirja[i]=useless_number
print("Esialgne nimekiri: "+str(nimekirja1))
print("Muudetud numbriga loend: "+str(nimekirja)) 

#6.1
from random import *
nimekirja=[] 
N=int(input("Sisestage numbrite pikkus: "))
for i in range(N):
    arv=randint(10,100)
    nimekirja.append(arv)
maksimum=max(nimekirja)
nimekirja[nimekirja.index(maksimum)]=maksimum/len(nimekirja) 
print("Muudetud numbriga loend: "+str(nimekirja))  

#самостоятельная работа

#7.Sorteerimine
nimekirja=[] 
try:
    N=int(input("Sisestage numbrite arv: ")) #
    for i in range(N): 
        try:
            arv=abs(int(input(f"Sisestage number {i+1}:")))
            nimekirja.append(arv)  
        except ValueError:
                print("Viga") 
    nimekirja.sort() 
    print("Nimekiri on sorteeritud: "+str(nimekirja)) 
    nimekirja.reverse() 
    print("Sortimisloendi järjekord: "+str(nimekirja)) 
except ValueError:
    ("Viga")


#12
from random import *
nimekirja=[] 
nimekirja1=[]
for i in range(10):
    arv=randint(1,100)
    nimekirja.append(arv)
    nimekirja1.append(arv)
min_index=nimekirja.index(min(nimekirja))   
max_index=nimekirja.index(max(nimekirja))
for i in range(len(nimekirja)):
        nimekirja[min_index]=0
        nimekirja[max_index]=100
print("Esialgne nimekiri: "+str(nimekirja1))
print("Loend, mis asendas selle loendi miinimum ja maksimumelemendid: "+str(nimekirja)) 


#9. Nimi kontroll 
from string import punctuation
vokaali=["a","o","e","i","u","õ","ä","ö","ü","y"]
konsonanti="t,w,q,r,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,"
while True:
     nimi = input("Sisesta oma nimi: ").capitalize()
     if nimi.isalpha():   #isalpha() возвращает True в том случае, если все символы в строке являются буквами
         break
     else:
         print("Nimi peab sisaldama ainult tähti!")
print("Tere, {}!".format(nimi)) 
nimi_pikkus=len(nimi)
v=k=0 
for sümbol in nimi:
    if sümbol.lower() in vokaali:
        v+=1
    elif sümbol.lower() in konsonanti:
        k+=1
print("Tähtede arv nimes:", nimi_pikkus)
print("Täishäälikute arv:", v)
print("Konsonantide arv:", k)
unique_letters = sorted(set(nimi.lower()))   #сортирует элементы данного списка в определенном порядке возрастания или убывания.
print("Nimetage tähed tähestiku järjekorras:", ", ".join(unique_letters)) 


#8. Võrdsepikkusega elemendid
nimekirja = [['крот', 'белка', 'выхухоль'], 
             ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], 
             ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']]
suur = 0
indeks = 0
for i in range(len(nimekirja)):
   suur = 0
   for j in nimekirja[i]:
       suur = len(j)
       for x in nimekirja[i]:
           if len(x) < suur:
               indeks = nimekirja[i].index(x)
               tagastab_koguse = suur - len(x)
               nimekirja[i][indeks] += "_" * tagastab_koguse
print(nimekirja) 


