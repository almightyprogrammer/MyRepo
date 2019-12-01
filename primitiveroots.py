#PROGRAM TO FIND PRIMITIVE ROOTS OF <zp*,*>
def check(n): 
    count=0
    if n==1:
        print("Enter a valid number!")
    else:
        for i in range(2,n):
            if n % i==0:
                count+=1
        if count!=0:
            print("Enter a valid number!")
        else:
            return 1
n=int(input(" ***Enter a number to find the primitive roots of <zp*,*> *** \n"))
ip=n
k=check(n)
if k==1:
    r=[]
    for n in range(1,n):
        r.append(n)
    
    x=[]
    for m in range(0,n-1):
        x.append(m)
    

    roots=[]
    
    flag=0

    for ele in r:
        temporary=[]
        
        for val in x:

            p=(ele**val) %ip
            
            temporary.append(p)
    
        
       
        l=len(temporary)
        count=0
        d=[]
      
        for v1 in temporary:
            if v1 in d:
                count+=1
            else:
                d.append(v1)
        if count==0:
            count2=0
            for c in temporary:
                if c in r:
                    count2+=1
            if count2==len(temporary):
                roots.append(ele)
            else:
                flag=1
        else:
            flag=1

        if flag==1:
            continue
            
    print("\n ***The primitive roots are as follows***")
    print(roots)





            

            

                

             






