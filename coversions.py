#binary to decimal conversion#

##S=1001
##dec=0
##i=0
##while S:
##    r=S%10
##    dec=dec+r*(2**i)
##    S=S//10
##    i+=1
##print(dec)   



## conversion from decimal to binary##

##n= int(input())
##l=[]
##while n:
##    
##    R=n%2
##    n=n//2
##    l.append(R)
##    if n==0 or n==1:
##        l.append(n)
##        break
##print(l)
##l.reverse()
##print(l)
##for i in l:
##    print(i,end=" ")

####conversion from decimal to octal####

#n= int(input())
##def dec_to_oct(n):
##    l=[]
##    while n:
##        R=n%8
##        n=n//8
##        l.append(R)
##        if n==1:
##            l.append(n)
##            break
##        if n==0:
##            break
##    l.reverse()
##    for i in l:
##        print(i,end=" ")
##
##dec_to_oct(n)

####conversion from octal to decimal####
##n= int(input())
##def oct_to_dec(n):
##    dec=0
##    i=0
##    while n:
##        r=n%10
##        dec=dec+r*(8**i)
##        n=n//10
##        i+=1
##    return dec
##print(oct_to_dec(n))
##




###conversion from hexadecimal to decimal###
n= input()
n1=n[::-1]
print(n1)
base=0
dec=0
l1=['A','B','C','D','E','F']
l2=['0','1','2','3','4','5','6','7','8','9']
for i in n1:
    if i in l2:
        dec+=int(i)*(16**base)
        print(dec)
        base+=1
    if i in l1:
        dec+=(ord(i)-55)*(16**base)
        print(dec)
        base+=1
print(dec)       
    
    















