X='q';W=range;V=any;P='Pp';O='pnbrqk';M='-';D='/';B=max;L=abs;K='k';J='K';I='';H='b';F=None;E='w';C='.'
a=-17,-15,-10,-6,6,10,15,17;d=-9,-8,-7,-1,1,7,8,9;Q=-9,-7,7,9;N=-8,-1,1,8;A=100,320,330,500,900,0
f={0:'Q',7:J,56:X,63:K}
import json as Y,os,urllib.request as Z
def G(a,b):return 0<=b<64 and L(a%8-b%8)<=2
def R(b,s,y):
	z='pP'[y==E];k=8-16*(y==E)
	if V(G(s,s+k+x)and b[s+k+x]==z for x in(-1,1)):return True
	if V(G(s,s+x)and b[s+x]=='nN'[y==E]for x in a):return True
	if V(G(s,s+x)and b[s+x]=='kK'[y==E]for x in d):return True
	for x in Q+N:
		t=s+x
		while G(t-x,t)and b[t]==C:t+=x
		if G(t-x,t)and b[t].islower()==(y==H)and b[t].lower()in X+'br'[x in N]:return True
	return False
def parse(x):
	f=x.split();b=list(I.join(C*int(c)if c.isdigit()else c for r in f[0].split(D)[::-1]for c in r));e=F
	if f[3:]and f[3]!=M:e=ord(f[3][0])-97+8*(int(f[3][1])-1)
	return b,f[1],f[2]if len(f)>2 else M,e
def i(b,s,c,e):
	T='qrbn';E=[];J=E.append;I=s==H;U='PNBRQK'if I else O;V=U+C
	for(A,M)in enumerate(b):
		if M==C or M.islower()!=I:continue
		L=M.lower()
		if L=='p':
			P=8-16*I;X=7-7*I;Y=A+P
			if 0<=Y<64 and b[Y]==C:
				if Y//8==X:E+=[(A,Y,C)for C in T]
				else:
					J((A,Y,F));Z=A+2*P
					if A//8==1+5*I and b[Y]==b[Z]==C:J((A,Z,F))
			for D in(-1,1):
				Y=A+P+D
				if G(A,Y)and(b[Y]in U or Y==e):
					if Y//8==X:E+=[(A,Y,C)for C in T]
					else:J((A,Y,F))
		elif L in'nk':
			E+=[(A,A+D,F)for D in(a if L=='n'else d)if G(A,A+D)and b[A+D]in V]
			if L==K and A in(4,60):
				S=A==4;Z=('kq','KQ')[S];f='rR'[S];g='wb'[S]
				for Y in W(2):
					D=1-2*Y;h=2+(D<0)
					if Z[Y]in c and b[A+D*(3+(D<0))]==f and all(b[A+D*B]==C for B in W(1,h+1))and all(not R(b,A+D*B,g)for B in W(3)):J((A,A+2*D,F))
		else:
			for D in(Q,N,Q+N)['brq'.index(L)]:
				Y=A+D
				while G(Y-D,Y)and b[Y]in V:
					J((A,Y,F))
					if b[Y]!=C:break
					Y+=D
	return E
def mv(b,s,c,e,m):
	B=list(b);A,D,K=m;G=B[A];N=s==E;R=16*N-8
	if G in P and L(D-A)in(7,9)and B[D]==C:B[D-R]=C
	B[D]=G;B[A]=C
	if K:B[D]=K.upper()if N else K
	if G in'Kk'and L(D-A)==2:O=2*(D>A)-1;B[A+O],B[A+3*O]=B[A+3*O],C
	H=c if c and c!=M else I
	if G in'Kk':H=H.replace(G,I).replace('Q'if G==J else X,I)
	for Q in(A,D):H=H.replace(f.get(Q,I),I)
	return B,'wb'[N],H or M,(A+D)//2 if G in P and L(D-A)==16 else F
def legal(b,s,c,e):
	K='kK'[s==E];D='wb'[s==E]
	return[m for m in i(b,s,c,e)if K in(B:=mv(b,s,c,e,m)[0])and not R(B,B.index(K),D)]
def c(b):return sum((-1+2*B.isupper())*A[O.index(B.lower())]for B in b if B!=C)
def S(b,s):return c(b)*(-1+2*(s==E))
def T(b,m,e):
	E,B,D=m;F=A[O.index(b[B].lower())]if b[B]!=C else 100*(b[E]in P and B==e);return F+(A[O.index(D)]if D else 0)
def g(b,s,c,e,a,z,n):
	n[0]+=1;A=S(b,s)
	if n[0]>6e4:return A
	if A>=z:return A
	a=B(a,A);D=[A for A in legal(b,s,c,e)if b[A[1]]!=C or A[2]or b[A[0]]in P and A[1]==e];D.sort(key=lambda h:-T(b,h,e))
	for E in D:
		if n[0]>6e4:break
		F=mv(b,s,c,e,E);A=B(A,-g(*F[:4],-z,-a,n));a=B(a,A)
		if a>=z:break
	return A
def h(b,s,c,e,d,a,z,n):
	n[0]+=1;A=S(b,s)
	if n[0]>6e4:return A
	if d<1:return g(b,s,c,e,a,z,n)
	C=legal(b,s,c,e)
	if not C:return-99999*R(b,b.index('kK'[s==E]),'wb'[s==E])
	C.sort(key=lambda h:-T(b,h,e));A=-1e6
	for D in C:
		if n[0]>6e4:break
		F=mv(b,s,c,e,D);A=B(A,-h(*F[:4],d-1,-z,-a,n))
		if A>a:a=A
		if a>=z:break
	return A
def b(b,s,c,e):
	A=legal(b,s,c,e)
	if not A:return
	B=A[0];D=[0]
	for I in W(1,5):
		C=-1e6;E=B;F=0;A.sort(key=lambda h:-T(b,h,e))
		if B in A:A.remove(B);A.insert(0,B)
		for G in A:
			if D[0]>6e4:F=1;break
			J=mv(b,s,c,e,G);H=-h(*J[:4],I-1,-1e6,-C,D)
			if H>C:C=H;E=G
		if F:break
		B=E
	return B
def e(m):A,B,C=m;return f'{chr(97+A%8)}{A//8+1}{chr(97+B%8)}{B//8+1}{C or I}'
def U(p,b):A=os.environ['MAKEFUN_ENV_URL'].rstrip(D)+D+p.lstrip(D);return Y.load(Z.urlopen(Z.Request(A,Y.dumps(b).encode(),{'Content-Type':'application/json'})))
def j():
	C='status';B='game'
	while 1:
		A=U('/game',{})
		if A.get(C)=='done':return
		while A.get(C)=='your_move':
			E,G,H,I=parse(A['fen']);D=b(E,G,H,I)
			if D is F:A=U('/resign',{B:A[B]});break
			A=U('/move',{B:A[B],'move':e(D)})
if __name__=='__main__':j()
