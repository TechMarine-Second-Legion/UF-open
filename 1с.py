#09.06.2021 ХО

def sign(num):
    return -1 if num < 0 else 1

def gcd(a,b):
	if b==0: return a
	else: return gcd(b, a%b)

# https://intuit.ru/studies/courses/691/547/lecture/12389?page=2
def uE(a,b):
	#a, b = max(a,b), min(a,b)

	U = (a,1,0)
	V = (b, 0, 1)

	while V[0]!=0:
		q = U[0] // V[0]
		t = (U[0] % V[0], U[1] - q* V[1], U[2] - q* V[2])
		U, V= V, t
	
	return U



def solver(a,b,c):
	#a, b = max(a,b), min(a,b)
	print(f"Исходное уравнение: {a}x + {b}y = {c}", end = '\n\n')
	
	solv = uE(a,b)
	#print(solv)
	if c % solv[0]==0:
		
		x = solv[1]*c/solv[0]
		y = solv[2]*c/solv[0]
		#print(int(x),int(y))
		print(f"Уравнение разрешимо, например: х = {x}, y = {y}")
		print(f"Проверка {a} * {x} {str(dict([[1,'+'],[-1, '-']])[sign(y*b)])} {b} * {y} == {c}",f"({a*x+b*y==c})")
	else:
		print("Уравнение корней не имеет")
		print(solv)

# Ax+By = C, 
# На вход A, B, C
solver(*map(int, input("Введите коэфиценты диофантового уравнения(A, B, C) через пробел: ").split()))

#solver(23,64,31)


