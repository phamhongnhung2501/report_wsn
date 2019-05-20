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
def nt(p):
	if(p<2):
		return 0
	for i in range(2,p-1):
		if(p%i == 0):
			return 0
	return 1

def in_nt(n,a):
        for i in range(0,n):
            if nt(a[i]):
                print(a[i]),
in_nt(n,a)

def NhapMangB():
	global b,m
	try:
	    m = int(input("Nhap so phan tu cua mang b: "))
	    if m <= 0:
	        exit()
	except:
	    print('So nhap khong hop le')
	    exit()
	b = []
	for i in range(0,m):
	    b.append(int(input('Nhap so thu %d: ' % (i+1))))
NhapMangB()
def GopMang():
	# global a,b,k
	try:
	    k = int(input("Nhap vi tri chen: "))
	    if k <= 0:   	
	        exit()
	except:
	    print('So nhap khong hop le')
	    exit()
	# a.extend(b)
	a.insert(k, b)
	print(a)
GopMang()
