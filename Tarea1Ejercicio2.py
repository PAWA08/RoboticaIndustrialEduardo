a=int(input("inserta el primer valor"))
b=int(input("inserta el segundo valor"))
c=int(input("inserta el tercer valor"))
d=int(input("inserta el cuarto valor"))
e=int(input("inserta el quinto valor"))
f=int(input("inserta el sexto valor"))
tupla1=(a,b,c)
tupla2=(d,e,f)
ppunto=[]
for i in range(len(tupla1)):
	ppunto.insert(i,tupla1[i]*tupla2[i])
tuplappunto=tuple(ppunto)
print(tuplappunto)