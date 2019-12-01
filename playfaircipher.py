#PROGRAM TO IMPLEMENT PLAYFAIR CIPHER
import numpy as np
import string
i=input("Enter the string for encryption using Playfair cypher\n")
lis=i
str=""
flag=0
if len(i) %2 ==0:
    for v in range(0,len(lis),2):
        if lis[v]!=lis[v+1]:
            s=lis[v]+lis[v+1]
            str=str+s
        else:
            flag=1
            s=lis[v]+"x"+lis[v+1]
            str=str+s
            t=""
            for k in range(v+2,len(lis)):
                t=t+lis[k]
            str=str+t+"z"
        if flag==1:
            break

else:
    for v in range(0,len(lis)-1,2):
        if lis[v]!=lis[v+1]:
            s=lis[v]+lis[v+1]
            str=str+s
        else:
            flag=1
            s=lis[v]+"x"+lis[v+1]
            str=str+s
            t=""
            for k in range(v+2,len(lis)):
                t=t+lis[k]
            str=str+t
        if flag==1:
            break
    if flag==0:
        str=str+lis[len(lis)-1]+"z"
        
pro=[]
for i in range(0,len(str),2):
    to=str[i]+str[i+1]
    pro.append(to)


k=input("Enter the key for encryption using Playfair cypher:\n")
key=list(k.lower())
new=[]
for j in key:
    if j not in new:
        new.append(j)

li=[]
for r in range(97,123):
    li.append(chr(r))

for a in li:
    if a!="j":
        if a not in new:
             new.append(a)

ip=[]       
for b in range(25):
    ip.append(new[b])

datamat=np.array(ip)
shape=(5,5)
datamat.shape=shape
print("\n")
print("The 5*5 Encryption Matrix is:\n")
print(datamat,"\n")

data=datamat.tolist()


ind=[]
def indices(val1,val2):
    ind=[]
    for y in range(5):
        for z in range(5):
            if data[y][z]==val1:
                temp1=[y,z]
                ind.extend(temp1)
                
    for y in range(5):
        for z in range(5):
            if data[y][z]==val2:
                temp2=[y,z]
                ind.extend(temp2)        
    return ind

def conditions(ind):
    
    if ind[0]==ind[2]:
        ind[1]=(ind[1]+1) %5
        ind[3]=(ind[3]+1) %5

    elif ind[1]==ind[3]:
        
        ind[0]=(ind[0]+1) %5
        ind[2]=(ind[2]+1) %5
    else:
        ind[1],ind[3]=ind[3],ind[1]
    return ind

encrypted=[]
for t in pro:
    fir=t[0]
    sec=t[1]
    value=indices(fir,sec)
    v=conditions(value)
    encrypted.append(value)

result=[]
for p in range(len(pro)):
    for q in range(4):
        result.append(encrypted[p][q])

output=""
for b in range(0,len(result),2):
    e=result[b]
    f=result[b+1]
    var=data[e][f]
    output=output+var
print("Encrypted Message is:\n")
print("\n"+output.upper())


#DECRYPTION
def dec(ind):
    
    if ind[0]==ind[2]:
        ind[1]=(ind[1]-1) %5
        ind[3]=(ind[3]-1) %5

    elif ind[1]==ind[3]:
        
        ind[0]=(ind[0]-1) %5
        ind[2]=(ind[2]-1) %5
    else:
        ind[1],ind[3]=ind[3],ind[1]
    return ind



original=[]
for p in range(len(encrypted)):
    t=encrypted[p]
    new=dec(t)
    original.append(new)

result=[]
for p in range(len(pro)):
    for q in range(4):
        result.append(original[p][q])

output=""
for b in range(0,len(result),2):
    e=result[b]
    f=result[b+1]
    var=data[e][f]
    output=output+var
print("\n"+"Decrypted  Message is:\n")
print(output)




           
































 


















