from math import pow
z=16
class signAlgo :
    def __init__(self,a,b,c,d):
        self.p=a
        self.alpha=b
        self.beta=(pow(alpha,z)%self.p
        self.m=c
        self.k=d
        self.r=self.createR(self.alpha,self.k)
        self.s=self.createS()
    def gcd(self,a,b):
        if a<b:
            return gcd(self,b,a)
        elif a%b==0:
            return b
        else:
            return gcd(b,a%b)
    def createK(self):
        a=2*(self.p-1)
        while (gcd(a,self.p-1)!=1):
            a=math.random()*(p-1)
        return a
    def invK(self):
        for x in range(1,self.p-1):
            if ((self.k*x)%(self.p-1)==1):
                return x
        return 1
    def createR(self,b,c):
        a=math.pow(b,c)
        if (a<math.pow(2,36)-1):
            return a%self.p
        else:
            return (self.createR(b,c/2)*self.createR(b,c-c/2))%self.p
    def createS(self):
        a=(self.invK()*(self.m-z*self.r))%(self.p-1)
        if (a>=0):
            return a
        else:
            return (a+self.p-1)
class verify:	
	def __init__(self,a,b,c,d,e,f):
		self.p=a
		self.alpha=b
		self.beta=c
		self.m=d
		self.r=e
		self.s=f
	def v1(self,b,c,d,e):
		a=int(((math.pow(b,c))*(math.pow(d,e))))
		if(a<math.pow(2,36)-1):
			return a%self.p
		else:
			return (self.v1(b,c/2,d,e/2)*self.v1(b,c-c/2,d,e-e/2))%self.p
	def v2(self,b,c):
		a=(math.pow(b,c))
		if(a<math.pow(2,36)-1):
			return a%self.p
		else:
			return (self.v2(b,c/2)*self.v2(b,c-c/2))%self.p
	def verified(self):
		if(self.v1(self.beta,self.r,self.r,self.s)==self.v2(self.alpha,self.m)):
			print("Signature verified using ElGamal.")
			print("The value of v1 mod p: ",self.v1(self.beta,self.r,self.r,self.s))
			print("The value of v2 mod p: ",self.v2(self.alpha,self.m))
		else:
			print("Signature missmatch")
			print("The value of v1 mod p: ",self.v1(self.beta,self.r,self.r,self.s))
			print("The value of v2 mod p: ",self.v2(self.alpha,self.m))
		print self.p, self.alpha, self.beta, self.m, self.r, self.s
		print 

p=input("Enter the value of p : ")
alpha=input("Enter the value of alpha : ")
m=input("Enter the value of m : ")
k=input("Enter the value of k : ")
sign=signAlgo(p,alpha,m,k)
v=verify(sign.p,sign.alpha,sign.beta,sign.m,sign.r,sign.s)
print sign.invK()
v.verified()
