def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = 1
            
            while j >= gap and arr[j - gap]> temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        
        gap //= 2
#Solicitar al usuario una lista de números 

numbers = input("ingrese una lista de números separados por espacios:").split()
numbers= [int(num) for num in numbers]

