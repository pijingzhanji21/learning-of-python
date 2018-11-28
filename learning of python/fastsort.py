def fastsort(list,low,high):
    first = low
    last = high
    if low>=high:
        return
    key=list[first]
    while last>first:
        while last>first and list[last]>key:
            last-=1
        list[first]=list[last]
        while last>first and list[first]<=key:
            first+=1
        list[last]=list[first]
    list[first]=key
    fastsort(list,low,first-1)
    fastsort(list,first+1,high)
a=[3,6,2,9,5]
fastsort(a,0,len(a)-1)
print(a)
