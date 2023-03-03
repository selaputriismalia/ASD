def merge_sort(arr):
    """
    Fungsi ini menerima sebuah array dan mengembalikan array tersebut dalam
    keadaan terurut menggunakan Merge Sort.
    
    Args:
        arr: Sebuah array yang akan diurutkan.
    
    Returns:
        Array dalam keadaan terurut.
    """
    # Base case: jika array memiliki satu elemen atau kurang, kembalikan array tersebut
    if len(arr) <= 1:
        return arr
    
    # Tentukan indeks tengah array dan pisahkan array menjadi dua bagian
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Urutkan bagian kiri dan kanan secara rekursif
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Gabungkan bagian kiri dan kanan yang sudah terurut menggunakan fungsi merge
    return merge(left, right)

def merge(left, right):
    """
    Fungsi ini menerima dua array yang sudah terurut dan mengembalikan
    gabungan kedua array tersebut dalam keadaan terurut.
    
    Args:
        left: Sebuah array yang sudah terurut.
        right: Sebuah array yang sudah terurut.
    
    Returns:
        Array dalam keadaan terurut yang merupakan gabungan dari left dan right.
    """
    result = []  # Inisialisasi array kosong untuk menyimpan hasil penggabungan
    i = 0  # Indeks untuk array left
    j = 0  # Indeks untuk array right
    
    # Selama kedua array memiliki elemen yang belum digabungkan
    while i < len(left) and j < len(right):
        # Jika elemen pertama left lebih kecil daripada elemen pertama right
        if left[i] < right[j]:
            result.append(left[i])  # Tambahkan elemen pertama left ke hasil penggabungan
            i += 1  # Pindahkan indeks i ke elemen berikutnya di left
        else:
            result.append(right[j])  # Tambahkan elemen pertama right ke hasil penggabungan
            j += 1  # Pindahkan indeks j ke elemen berikutnya di right
    
    # Jika masih ada elemen yang tersisa di left, tambahkan semua elemen tersebut ke hasil penggabungan
    result += left[i:]
    # Jika masih ada elemen yang tersisa di right, tambahkan semua elemen tersebut ke hasil penggabungan
    result += right[j:]
    
    return result

arr = [10, 1, 2, 9, 3, 7]
print("Array Belum Terurut")
print(arr)

print()

result = merge_sort(arr)
print("Array Sudah Terurut")
print(result)