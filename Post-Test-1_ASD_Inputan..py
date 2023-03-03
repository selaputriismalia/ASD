arr = []

def masukan():
    user1 = int(input("Silahkan masukan angka ke-1 : "))
    arr.append(user1)
    user2 = int(input("Silahkan masukan angka ke-2 : "))
    arr.append(user2)
    user3 = int(input("Silahkan masukan angka ke-3 : "))
    arr.append(user3)
    user4 = int(input("Silahkan masukan angka ke-4 : "))
    arr.append(user4)
    user5 = int(input("Silahkan masukan angka ke-5 : "))
    arr.append(user5)
    user6 = int(input("Silahkan masukan angka ke-6 : "))
    arr.append(user6)
    user7 = int(input("Silahkan masukan angka ke-7 : "))
    arr.append(user7)
    user8 = int(input("Silahkan masukan angka ke-8 : "))
    arr.append(user8)
    user9 = int(input("Silahkan masukan angka ke-9 : "))
    arr.append(user9)
    user10 = int(input("Silahkan masukan angka ke-10 : "))
    arr.append(user10)



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


masukan()
memilih()