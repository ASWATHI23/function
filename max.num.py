def max(a,b,c):
    if (a>=b) and (a>=c):
        largest=a
    elif (b>=a) and (b>=c):
        largest=b
    else:
        largest=c
    return largest
sum=max(2,4,3)
print(sum)
