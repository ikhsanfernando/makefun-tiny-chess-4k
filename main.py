import json as a,os as z,urllib.request as c
T='pnbrqk';d=100,320,330,500,900,0;S='Pp';h='.';F='';r=None
l='w';I='b';Q='-';W='/';U='k';V='K';m=max;P=abs;R=range
s=-17,-15,-10,-6,6,10,15,17;j=-9,-8,-7,-1,1,7,8,9;_=-9,-7,7,9;X=-8,-1,1,8
def v(c,d):return 0<=d<64 and P(c%8-d%8)<3
def e(x):
 y=x.split();b=list(F.join(h*int(c)if c.isdigit()else c for r in y[0].split(W)[::-1]for c in r));e=y[2]if len(y)>2 else Q;f=ord(y[3][0])-97+8*(int(y[3][1])-1)if y[3:]and y[3]!=Q else r
 return b,y[1],e,f
def o(e):a,b,c=e;return f'{chr(97+a%8)}{a//8+1}{chr(97+b%8)}{b//8+1}{c or F}'
def u(e,l):u=z.environ['MAKEFUN_ENV_URL'].rstrip(W)+W+e.lstrip(W);return a.load(c.urlopen(c.Request(u,a.dumps(l).encode(),{'Content-Type':'application/json'})))
def w():
 while 1:
  z=u('/game',{})
  if z.get('status')=='done':return
  while z.get('status')=='your_move':
   a,d,g,f=e(z['fen']);m=C(a,d,g,f)
   if m is r:z=u('/resign',{'game':z['game']});break
   z=u('/move',{'game':z['game'],'move':o(m)})
def x(a):return sum((-1+2*q.isupper())*d[T.index(q.lower())]for q in a if q!=h)
def q(a,d):return x(a)*(-1+2*(d==l))
def J(a,n,u):
 z='pP'[u==l];w=8-16*(u==l)
 if any(v(n,n+w+x)and a[n+w+x]==z for x in(-1,1)):return 1
 if any(v(n,n+x)and a[n+x]=='nN'[u==l]for x in s):return 1
 if any(v(n,n+x)and a[n+x]=='kK'[u==l]for x in j):return 1
 for p in _+X:
  w=n+p
  while v(w-p,w)and a[w]==h:w+=p
  if v(w-p,w)and a[w].islower()==(u==I)and a[w].lower()in'q'+'br'[p in X]:return 1
 return 0
def n(a,e,f):c,b,o=e;return(d[T.index(a[b].lower())]if a[b]!=h else 100*(a[c]in S and b==f))+(d[T.index(o)]if o else 0)
def p(a,d,g,f):
 L=d==I;n=(T,'PNBRQK')[L];u=n+h;e=7-7*L;E=8-16*L;N=[];t=N.append
 for c,q in enumerate(a):
  if q==h or q.islower()!=L:continue
  M=q.lower()
  if M=='p':
   b=c+E
   if 0<=b<64 and a[b]==h:
    if b//8==e:
     for o in'qrbn':t((c,b,o))
    else:
     t((c,b,r));w=c+2*E
     if c//8==1+5*L and a[w]==h:t((c,w,r))
   for k in(-1,1):
    b=c+E+k
    if v(c,b)and(a[b]in n or b==f):
     if b//8==e:
      for o in'qrbn':t((c,b,o))
     else:t((c,b,r))
  elif M in'nk':
   for p in(s if M=='n'else j):
    b=c+p
    if v(c,b)and a[b]in u:t((c,b,r))
   if M==U and c in(4,60):
    C=c==4;z=('kq','KQ')[C];y='rR'[C];x='wb'[C]
    for i in R(2):
     m=1-2*i
     if z[i]in g and a[c+m*(3+(m<0))]==y and all(a[c+m*l]==h for l in R(1,3+(m<0)))and all(not J(a,c+m*l,x)for l in R(3)):t((c,c+2*m,r))
  else:
   for p in(_,X,_+X)['brq'.index(M)]:
    b=c+p
    while v(b-p,b)and a[b]in u:
     t((c,b,r))
     if a[b]!=h:break
     b+=p
 return N
def Y(a,d,g,f,e):
 c,b,o=e;s=list(a);D=s[c];C=d==l
 if D in S and P(b-c)in(7,9)and s[b]==h:s[b-(8 if C else-8)]=h
 s[b]=D;s[c]=h
 if o:s[b]=o.upper()if C else o
 if D in'Kk'and P(b-c)==2:m=1 if b>c else-1;s[c+m],s[c+3*m]=s[c+3*m],h
 B=g if g and g!=Q else F
 if D in'Kk':B=B.replace(D,F).replace('Q'if D==V else'q',F)
 for n in(c,b):B=B.replace({0:'Q',7:'K',56:'q',63:'k'}.get(n,F),F)
 return s,I if C else l,B or Q,(c+b)//2 if D in S and P(b-c)==16 else r
def t(a,d,g,f):e='kK'[d==l];u='wb'[d==l];return[m for m in p(a,d,g,f)if e in(x:=Y(a,d,g,f,m)[0])and not J(x,x.index(e),u)]
def D(a,d,g,f,j,A,k):
 k[0]+=1;H=q(a,d)
 if k[0]>6e4:return H
 if H>=A:return H
 j=m(j,H);i=[e for e in t(a,d,g,f)if a[e[1]]!=h or e[2]or a[e[0]]in S and e[1]==f];i.sort(key=lambda e:-n(a,e,f))
 for e in i:
  if k[0]>6e4:break
  K=Y(a,d,g,f,e);j=m(j,-D(*K[:4],-A,-j,k))
  if j>=A:break
 return j
def G(a,d,g,f,Z,j,A,k):
 k[0]+=1;H=q(a,d)
 if k[0]>6e4:return H
 if Z<1:return D(a,d,g,f,j,A,k)
 i=t(a,d,g,f)
 if not i:return-99999*J(a,a.index('kK'[d==l]),'wb'[d==l])
 i.sort(key=lambda e:-n(a,e,f));y=-1e6
 for e in i:
  if k[0]>6e4:break
  K=Y(a,d,g,f,e);y=m(y,-G(*K[:4],Z-1,-A,-j,k))
  if y>j:j=y
  if j>=A:break
 return y
def C(a,d,g,f):
 i=t(a,d,g,f)
 if not i:return r
 E=i[0];k=[0]
 for Z in R(1,5):
  b=-1e6;c=E;h=0;i.sort(key=lambda e:-n(a,e,f))
  if E in i:i.remove(E);i.insert(0,E)
  for e in i:
   if k[0]>6e4:h=1;break
   K=Y(a,d,g,f,e);O=-G(*K[:4],Z-1,-1e6,-b,k)
   if O>b:b=O;c=e
  if h:break
  E=c
 return E
if __name__=='__main__':w()
parse=e
legal=t
mv=Y
