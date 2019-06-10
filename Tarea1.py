tupla1=(4,24,40,17)
tupla2=(3,21,7,80)
suma=[]
for i in range(len(tupla1)):
	suma.insert(i,tupla1[i]+tupla2[i])
tuplasuma=tuple(suma)
print(tuplasuma)