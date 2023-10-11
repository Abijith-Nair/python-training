def cal(lim,num,temp):
    print("")
    if(temp>0):
        ch1=str(input("Enter new list of numbers? (y/n): "))
        print("")
        if(ch1=='y'):
            inp()
    ch=str(input("Enter operation(+ - / * ^ %) or (x):"))
    if(ch=='+'):
        add(num,lim)
    elif(ch=='-'):
        sub(num,lim)
    elif(ch=='/'):
        div(num,lim)
    elif(ch=='*'):
        mult(num,lim)
    elif(ch=='^'):
        exp(num,lim)
    elif(ch=='%'):
        mod(num,lim)
    elif(ch=='x'):
        exit

def inp():
    temp=0
    num=[]
    num.clear()
    lim=int(input("Enter limit of numbers: "))
    print('')
    for i in range (0,lim,1):
        x=int(input("Enter value: "))
        num.append(x)
    cal(lim,num,temp)

def add(x,l):
    n=[]
    for i in range(0,l,1):
        n.append(x[i])
    print("")
    tot=0;
    for i in range(0,l,1):
        tot=tot+x[i]
    print("Sum =",tot)
    cal(l,n,1)

def sub(x,l):
    n=[]
    for i in range(0,l,1):
        n.append(x[i])
    print("")
    tot=x[0];
    for i in range(1,l,1):
        tot=x[i]-tot
    print("Difference =",tot)
    cal(l,n,1)

def div(x,l):
    n=[]
    for i in range(0,l,1):
        n.append(x[i])
    print("")
    tot=[]
    for i in range(0,l-1,1):
        tot.append(x[i]/x[i+1])
        print("Quotient for given numbers [(x,y)...] format = [",tot[i],"]")
    cal(l,n,1)
    
def mult(x,l):
    n=[]
    for i in range(0,l,1):
        n.append(x[i])
    print("")
    tot=x[0];
    for i in range(1,l,1):
        tot*=x[i]
    print("Product =",tot)
    cal(l,n,1)

def exp(x,l):
    n=[]
    for i in range(0,l,1):
        n.append(x[i])
    print("")
    tot=[];
    power=int(input("Enter power value: "))
    for i in range(0,l,1):
        tot.append(x[i]**power)
        print("Exponential value for given numbers and given power value = [",tot[i],"]")
    cal(l,n,1)

def mod(x,l):
    n=[]
    for i in range(0,l,1):
        n.append(x[i])
    print("")
    tot=[];
    for i in range(0,l-1,1):
        tot.append(x[i]%x[i+1])
        print("Floor value for given numbers [(x,y)...] format = [",tot[i],"]")
    cal(l,n,1)
    
inp()
    

