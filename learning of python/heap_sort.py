def heapfiy(list,i,n):
    j=2*i+1
    while j<n:
        if  j+1<n and list[j]<list[j+1]:
            j+=1
        if list[i]>list[j]:
            break
        list[i],list[j]=list[j],list[i]
        i=j
        j=2*i+1
def build_heap(list):
    for i in range(len(list)//2-1,-1,-1):
        heapfiy(list,i,len(list))
def heap_sort(list):
    l=len(list)
    build_heap(list)
    for i in range(l-1,0,-1):
        list[0],list[i]=list[i],list[0]
        heapfiy(list,0,i)
    return
a=[3,6,2,9,5]
heap_sort(a)
print(a)