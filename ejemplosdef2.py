def suma(a,b,c,d):
	sum=(a+b+c+d)
	return sum
suma=suma(3,6,12,40)
print(suma)
#-problema2-#
def cuadrado(a):
	cuadrado=(a**2)
	return cuadrado
square=cuadrado(3)
print(square)
#-problema3-#
l=[10,42,24,12,40]
def cuadrado2(v,p):
	cua=[]
	x=0
	r=len(v)
	while x<r:
		y=v[x]**2
		cua.append(y)
		x+=1
	return cua
print(cuadrado2(l,3))
#-problema4-#
def Nombres(**kwargs):
	for key in kwargs
