print("-------------------")
while True:
    mat=input("sua nota de matemática: "  )
    if float(mat)>=0 and mat.isnumeric():
        break
    else:
        print("valor inválido!!")
        continue
        

while True:
    matconf=input("confirme sua nota (Y) ou Altere ela (M): ")

    if matconf =="Y" or matconf == "y" :
        matconf=input("confirme sua nota:  ")

        if matconf==mat:
            print("Sua nota é: "+ str(matconf))
            break
        elif matconf != mat:
            print ("Esta nota não foi a mesma selecionada inicialmente!")
            continue
    elif matconf == "m" or matconf=="M" :
        mat=input("Qual é o valor novo da nota?: " )
        print("Sua nota atual é:  " + str(mat) )
        break

print("-------------------")


hum=input("sua nota de humanas:"  )
print("confirme sua nota : " + str(hum))
print("-------------------")


nat=input("sua nota de natureza: ")

print("confirme sua nota : " + str(nat))

print("-------------------")


print ("sua nota de linguagens:")
ling=input()
print(ling)
print("-------------------")


print ("sua nota na redação:")
red=input()
print(red)
print("-------------------")

print ("o peso em matemática")
pm=input()
print(pm)
print("-------------------")

print ("o peso em humanas")
ph=input()
print(ph)
print("-------------------")

print ("o peso em natureza")
pn=input()
print(pn)
print("-------------------")

print ("o peso em linguagens")
pl=input()
print(pl)
print("-------------------")

print ("o peso em redação")
pred=input()
print(pred)
print("-------------------")
ptotal=float(pm)+float(ph)+float(pn)+float(pl)+float(pred)

print("sua média no sisu é :")
print(((float(mat)*float(pm))+(float(hum)*float(ph))+(float(nat)*float(pn))+(float(ling)*float(pl))+(float(red)*float(pred)))/ptotal)
print("O cálculo foi realizado através da seguinte média ponderada: ")
print(str(float(mat)) + " * " + str(float(pm)) + "+" + str(float(hum)) + "*" + str(float(ph))+"+"+ str(float(nat))+ "*" + str(float(pn)) + "+" + str(float(ling)) + "*" + str(float(pl)) + "+" + str(float(red)) + "*" + str(float(pred))+ "/" + str(ptotal))