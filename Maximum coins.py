a,b=map(int,input("enter: ").split())
if(b==1):
    e=a*2
    for i in range(5):
        e=e+5
    f=e
    x=f*2
if(b==2):
    for i in range(5):
        a=a+5
    f=a
    x=f*2*2
if(b==3):
    for i in range(4):
        a+=5
    f=a*2*2
    x=f+5
if(b==4):
    for i in range(3):
        a+=5
    f=a*2*2
    x=f+10
if(b==5):
    for i in range(2):
        a+=5
    f=a*2*2
    x=f+15
if(b==6):
    a+=5
    f=a*2*2
    for i in range(4):
        f+=5
    x=f
if(b==7):
    a=a*2*2
    for i in range(5):
        a+=5
    x=a    
print(x)

        
    
    
