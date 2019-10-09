import math
z=16
class signAlgo :
    def __init__(self,a,b,c,d):
        self.p=a
        self.alpha=b
        self.beta=int(pow(self.alpha,z)%self.p)
        self.m=c
        self.k=d
        self.r=self.createR()
        self.s=self.createS()
        print "The Signed Message Triplet generated is : ("+str(self.m)+","+str(self.r)+","+str(self.s)+")"
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
    def createR(self):
        a=int((self.alpha**self.k)%self.p)
        return a
    def createS(self):
        a=(self.invK()*(self.m-z*self.r))%(self.p-1)
        return a
    
class verify:	
	def __init__(self,a,b,c,d,e,f):
		self.p=a
		self.alpha=b
		self.beta=c
		self.m=d
		self.r=e
		self.s=f
	def v1(self,b,c,d):
		a=int(((b**c)*(c**d))%self.p)
		return a
	def v2(self,b,c):
		a=int((b**c)%self.p)
		return a
	def verified(self):
		if(self.v1(self.beta,self.r,self.s)==self.v2(self.alpha,self.m)):
			print("Signature verified using ElGamal.")
			print("The value of v1 mod p: "+str(self.v1(self.beta,self.r,self.s)))
			print("The value of v2 mod p: "+str(self.v2(self.alpha,self.m)))
		else:
			print("Signature missmatch")
			print("The value of v1 mod p: "+str(self.v1(self.beta,self.r,self.s)))
			print("The value of v2 mod p: "+str(self.v2(self.alpha,self.m)))
                                                            
p=input("Enter the value of p : ")
alpha=input("Enter the value of alpha : ")
m=input("Enter the value of m : ")
k=input("Enter the value of k : ")
sign=signAlgo(p,alpha,m,k)
print
print "Verification of Elgamal Signature"
v=verify(sign.p,sign.alpha,sign.beta,sign.m,sign.r,sign.s)
v.verified()
