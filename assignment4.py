def bubble(list_a):
    indexing_length=len(list_a)-1
    sorted=False
    while not sorted:
        sorted=True
        for i in range(0,indexing_length):
            if list_a[i]>list_a[i+1]:
                sorted=False
                list_a[i],list_a[i+1]=list_a[i+1],list_a[i]
    return(list_a)
print(bubble([2,3,1,8,5,6]))            

#selection.sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_value = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_value]:
                min_value = j
        arr[i], arr[min_value] = arr[min_value], arr[i]
    return arr

print(selection_sort([2, 3, 5, 1, 6]))
