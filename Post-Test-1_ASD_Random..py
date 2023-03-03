import random
arr = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(arr)



def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 
        print(f"Pivot : {pivot}")
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)
    

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
def merge(left, right):
    result = [] 
    i = 0  
    j = 0  
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])  
            i += 1 
        else:
            result.append(right[j])  
            j += 1  
    result += left[i:]
    result += right[j:]
    return result
    

def shellShort(arr):
    gap = (len(arr)//2)
    a=0

    while gap > 0 :
        for i in range(gap,len(arr)):
            value = arr[i]
            j = i

            while j >= gap and arr[j-gap] > value:
                arr[j] = arr[j-gap]
                j-=gap

            arr[j] = value
            print(arr)
        print("Iterasi ke",a,": ",arr,"dengan gap ",gap )
        a+=1

        gap //= 2

    return arr

def memilih():
    print("===================")
    print("| SILAHKAN PILIH  |")
    print("| 1. Quick Sort   |")
    print("| 2. Marge Sort   |")
    print("| 3. Sell Sort    |")
    print("===================")
    usermemilih = input("Ingin Memilih Nomor berapa : ")
    if usermemilih == "1" :
        print(quickSort(arr))
        kembli = input("Apakah ingin kembali? : ")
        if kembli ==  "y" :
            memilih()
    elif usermemilih == "2" :
        merge_sort(arr)
        print("Array Belum Terurut")
        print(arr)
        result = merge_sort(arr)
        print("Array Sudah Terurut")
        print(result)
        kembli1 = input("Apakah ingin kembali? : ")
        if kembli1 ==  "y" :
            memilih()
    elif usermemilih == "3" :
        shellShort(arr)
        print("Sebelum di-sort :",arr)
        print("Setelah di-sort :",shellShort(arr))
        kembli2 = input("Apakah ingin kembali? : ")
        if kembli2 ==  "y" :
            memilih()




# masukan()
memilih()