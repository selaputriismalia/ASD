import os
os.system('clear')

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 

        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot]

        greater = [x for x in arr[1:] if x > pivot]
    
        return quickSort(less) + [pivot] + quickSort(greater)
    
arr = [11, 9, 0, 2, 4, 5]

result = quickSort(arr)

print(result)