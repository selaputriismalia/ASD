# def magre_sort(arr) :
#     """ fungsih ini menerima sebyuah array dan mengembalikan array tersebut dalam keadaan terurut menggunakan
#     marge sort.
    
#     args : 
#         arr : sebuah array yang akan diurutkan. 
        
#     returns :
#         array dalam keadaan terurut"""
    
#     #Base case: jika array memiliki satu alamen atau kurang, kembalikan array tersebut
#     if len(arr) <=1:
#         return arr
    
#     #tentukan indeks
#     mid = len(arr) //2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = magre_sort(left)
#     right = magre_sort(right)

# def marge(left, right) :


#     result = []
#     i = 0
#     j = 0

#     while i <

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]

        

