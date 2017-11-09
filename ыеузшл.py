def modify_list(l):
    n=len(l)
    i=0
    while i < n:
        print(i)
        if l[i]%2==1:
            l.pop(i)
            n=n-1
            continue
        else:
            l[i]=l[i]//2
            i+=1
    return l

l = [1,2,3,4,5,6]

print(modify_list(l))