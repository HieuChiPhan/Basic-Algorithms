#a=3141592653589793238462643383279502884197169399375105820974944592
#b=2718281828459045235360287471352662497757247093699959574966967627
a=123456789
b=987654321
print('a*b=  ',a*b)
#print(len(a),len(b))

#def Karatsuba(a,b):
#    La=len(a)
#    Lb=len(b)
#    m=int(min(La,Lb)/2)
#    Bm=10**m
#    a1=int(a[0:La-m])
#    a2=int(a[La-m:La])
#    b1=int(b[0:La-m])
#    b2=int(b[La-m:La])
#    result=a1*b1*Bm**2+(a1*b2+a2*b1)*Bm+a2*b2
#    return result


def Karatsuba(a,b):

    if min (a,b)<100:
        return int(a*b)  
    print('Start')
    a=str(int(a))
    b=str(int(b))
#    print(a,b)

    La=len(a)
    Lb=len(b)
    m=int(min(La,Lb)/2)
    Bm=10**m
    a1=int(a[0:La-m])
    a2=int(a[La-m:La])
    b1=int(b[0:Lb-m])
#    print(m,b)
    b2=int(b[Lb-m:Lb])
    print(a,b)
#    print(a1,a2,b1,b2)


    
    z2=Karatsuba(a1,b1)
    z11=Karatsuba(a1,b2)
    z12=Karatsuba(a2,b1)
    z0=Karatsuba(a2,b2) 
#    print(z2,z11,z12,z0)
    result=z2*Bm**2+(z11+z12)*Bm+z0
    print(result)
    print('===========================')
    return result

print('result',Karatsuba(a,b))








