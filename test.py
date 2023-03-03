import random
arr = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(arr)
# user1 = input("Silahkan masukan angka ke-1 : ")
# arr.append(user1)
# user2 = input("Silahkan masukan angka ke-2 : ")
# arr.append(user2)
# user3 = input("Silahkan masukan angka ke-3 : ")
# arr.append(user3)
# user4 = input("Silahkan masukan angka ke-4 : ")
# arr.append(user4)
# user5 = input("Silahkan masukan angka ke-5 : ")
# arr.append(user5)
# user6 = input("Silahkan masukan angka ke-6 : ")
# arr.append(user6)
# user7 = input("Silahkan masukan angka ke-7 : ")
# arr.append(user7)
# user8 = input("Silahkan masukan angka ke-8 : ")
# arr.append(user8)
# user9 = input("Silahkan masukan angka ke-9 : ")
# arr.append(user9)
# user10 = input("Silahkan masukan angka ke-10 : ")
# arr.append(user10)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 

        print(f"Pivot : {pivot}")
        
        less = [x for x in arr[1:] if x <= pivot]

        greater = [x for x in arr[1:] if x > pivot]
    
        return quickSort(less) + [pivot] + quickSort(greater)

result = quickSort(arr)
print(arr)
print(result)