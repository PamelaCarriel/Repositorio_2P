def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    
    pivot = arr[len(arr // 2)]
    left = [x for x in arr if x < pivot]
    middle = [ x for x i n arr if x == pivot]
    rigth = [x for ]