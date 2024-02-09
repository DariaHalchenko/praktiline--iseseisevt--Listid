#1 Sõna/Lause
#from string import punctuation

#vokaali=["a","o","e","i","u","õ","ä","ö","ü","y"]
#konsonanti="t,w,q,r,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,"
#märkid=punctuation
#v=k=m=t=0
#tekst=input("Sisestage sõna või lause: ").lower()
#tekst_list=list(tekst)
#for sümbol in tekst_list:
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in märkid:
#        m+=1
#    elif sümbol==" ":
#        t+=1
#print("Vokaali: ",v) 
#print("Konsonanti:", k) 
#print("Kirjuvahemärgid: ",m) 
#print("Tühikud: ",t)

#2 Loetelu
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

vanus=[]
for i in range(5):
    aastat=input("Sisestage oma vanus: ").capitalize()
    vanus.append(aastat) 
vanus.sort() 
print("Vanuste loend: "+str(vanus)) 
max_age=max(vanus) 
min_age=min(vanus) 
summa_age=sum(vanus) 
average_age=sum(vanus)/len(vanus)
print(max_age)
print(min_age) 
print(summa_age) 
print(average_age)
