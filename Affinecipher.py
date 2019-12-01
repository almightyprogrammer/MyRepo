#PROGRAM TO IMPLEMENT AFFINE CIPHER
import math
ip=int(input("Enter the key for encryption using Affine cypher\n"))
add=2
print(" The Additive key for Affine cypher is \n",add)

while ip<=0:
	print("Enter a different value for key\n")
	ip=int(input())
k=math.gcd(ip,26)
#print(k)
if k==1:
	r1=26
	r2=ip
	t1=0
	t2=1
	while r2>0:
		q=r1//r2
		r=r1-q*r2
		r1=r2
		r2=r
		t=t1-q*t2
		t1=t2
		t2=t
	if r1==1:
		inverse=t1
		
mulinverse=26+inverse
print("Multiplicative Inverse is:",mulinverse)

s=input("Enter the plaintext\n")
st=s.lower()
print("Your message is:\n")
print(s)
new=[]
for i in st:
	k=ord(i)-97
	new.append(k)

encodedindices=[]
for j in new:
	p=(j*ip+add) % 26
	encodedindices.append(p)

encoded=""
for x in encodedindices:
	x=x+97
	g=chr(x)
	encoded=encoded+g
print("Encrypted message is:")
print(encoded.upper())


decodedindices=[]
#print("The Decryption side is \n")
for n in encodedindices:
	b=((n-2)*mulinverse) % 26
	decodedindices.append(b)

decrpt=""
for f in decodedindices:
	v=f+97
	p=chr(v)
	decrpt=decrpt+p
print("Decrypted message is:\n")
print(decrpt)

	


