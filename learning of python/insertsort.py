def insertsort(list):
    j=1
    while j<len(list):
        key=list[j]
        i=j-1
        while i>=0:
            if key>list[i]:
                list[i+1]=list[i]
                list[i]=key
            i-=1
        j+=1
    return
a=[3,6,2,9,9,8,5]
insertsort(a)
print(a)