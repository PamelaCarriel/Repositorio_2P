def exchange_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(i + 1, n):
            if arr[1] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
#Ejmplo de uso
array= [64, 34, 25, 12, 22, 11, 90]
exchange_sort(array)
print("Array ordenado:")
print(array)
