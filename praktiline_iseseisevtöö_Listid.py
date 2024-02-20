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


#10
töötajad=["Aadu Suur", "Malle Kapsas", "Uudo Koba", "Tiit Kopikas", "Vahur Vana"]
vanused=[56, 42, 32, 22, 67]
palgad=[2500, 1500, 700, 550, 870] 
maksimaalne_palk=max(palgad) 
maksimaalne_palk_indeks=palgad.index(maksimaalne_palk) 
nimi_maksimaalne_palk=töötajad[maksimaalne_palk_indeks] 
keskmine_palk=sum(palgad)/len(palgad) 
for palk in palgad:
    keskmisest=palk>keskmine_palk
    keskmisest=sum 
vanus_keskmisest_vähem=[] 
vanus_keskmisest_rohkem=[] 
for i in range(len(töötajad)):
    if palgad [i]<=keskmine_palk:
        vanus_keskmisest_vähem.append(vanused[i]) 
    else:
        vanus_keskmisest_rohkem.append(vanused[i]) 
keskmisest_väiksem_palk=sum(vanus_keskmisest_vähem)/len(vanus_keskmisest_vähem) 
keskmisest_suurem_palk=sum(vanus_keskmisest_rohkem)/len(vanus_keskmisest_rohkem)
print("Kõige suurema palgaga töötaja on "+str(nimi_maksimaalne_palk), "ning tema palk on "+str(maksimaalne_palk)) 
print("Keskmine palk on "+str(keskmine_palk))
print("Keskmisest palgast rohkem teenib "+str(keskmisest), "töötajat") 
print("Keskmised vanused neile, kes teenivad keskmisest palgast vähem: "+str(keskmisest_väiksem_palk)) 
print("Keskmised vanused neile, kes teenivad keskmisest palgast rohkem: "+str(keskmisest_suurem_palk))


#11
tähestik=["a","b","c","d", "e", "f", "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
indeks = -1
for i in tähestik:
   indeks += 1
   tähestik[indeks] = i * (indeks + 1) 
print("Inglise tähestiku järjestus: "+str(tähestik)) 


#13. Arva sõna ära
from random import choice
sõnad = ["Apple", "Banaan", "Pirn", "Ploom", "Arbuus", "Melon", "Kõrvits", "Kirss", "Kiivi", "Mandariin","Aprikoos", "Viinamarja", "Maasikas", "Vaarikad", "Sidrun"]
sõna = choice(sõnad)
kuva = ["_"]*len(sõna)
arvasi_ära = []
püüdlused = 1
maksimaalsed_püüdlused = 10
print(" ".join(kuva))
while True:
    try:
        oletada = input("Sisesta tähestik: ").lower()
    except: 
        print("Vale andme tüüp.")
    if len(oletada)>1: 
        print("Palun sisestage ainult üks täht!")
    if oletada in arvasi_ära:
        print("Sa juba arvasid selle tähe ära!")
        continue
    if oletada in sõna.lower():
        print("Õige!")
        arvasi_ära.append(oletada)
        kuva = ' '
        for letter in sõna.lower():
            if letter in arvasi_ära:
                kuva += letter
            else:
                kuva += '_'
        print(kuva.capitalize())
    else:
        print("Vale!")
        print("Püüdluste arv: " +str(püüdlused), "/10")
        arvasi_ära.append(oletada)
        print(kuva)
    if '_' not in kuva:
        print("Sa arvasid sõna ära! Mõistatuslik sõna oli: " +str(sõna))
        print("Kasutatud püüdluste arv:" +str(püüdlused), "/10")
        break
    püüdlused += 1
    if püüdlused >=maksimaalsed_püüdlused:
        print("Sa ei arvanud sõna ära!Mõistatuslik sõna oli: " +str(sõna))
        print("Kasutatud püüdluste arv: " +str(püüdlused), "/10")
        break



