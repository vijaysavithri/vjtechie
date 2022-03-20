def color_socks(n,ar):
    a={}
    for i in ar:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    count=0
    for i in a.values():
        count+=i//2
    print(count)
    print(a)


color_socks(9,[10,20,20,10,30,50,10,10,40])
