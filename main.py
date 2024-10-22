def inc(n,num):
    if n>num or n<1:
        return
    print(n)    
    inc(n-1,num)
    print(n)
n=int(input("Enter A Number: "))
inc(n,n)