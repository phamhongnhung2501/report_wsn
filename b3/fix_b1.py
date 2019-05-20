import math
#Nhap mang a
def NhapMangA():
	global a,n
	try:
	    n = int(input("Nhap so phan tu cua mang a: "))
	    if n <= 0:   	
	        exit()
	except:
	    print('So nhap khong hop le')
	    exit()
	a = []
	for i in range(0,n):
	    a.append(int(input('Nhap so thu %d: ' % (i+1))))
NhapMangA()
def nt(n):
	if(n<2):
		return 0
	for i in range(2,n-1):
		if(n%i == 0):
			return 0
	return 1
	for i in range(0,n):
		d = 0
	    if nt(a[i]):
	    	d += 1
	        print(a[i])
	    
nt()