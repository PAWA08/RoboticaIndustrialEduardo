#------Diccionario--------#
d={"i":"1","a":"4","e":"3","o":"0","u":"9","A":"4","E":"3","I":"1","O":"o","U":"9"}
name=[]
#------codigo------#
nombre=input("insertar nombre")
ln=len(nombre)
while i<ln:
	for k, v in d.items():
	if nombre[i]==k:
		name.append(v)
	
	