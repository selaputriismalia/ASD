fibonacci adalah suatu deret bilangan yang mana tiap angkanya adalah hasil penjumlahan dari dua angka sebelumnya.

Dan dua anggota pertama dari deret fibonacci selalu 0 dan 1.

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,

Deret Fibonacci adalah deret bilangan dimana setiap angka yang dihasilkan adalah 
jumlah dari dua angka sebelumnya. Misalnya,
 deret Fibonacci dimulai dengan 0, 1, dan 1, kemudian diikuti dengan 2, 3, 5, 8, 13, dan seterusnya.


Fibonacci adalah sebuah deret bilangan yang mana setiap anggotanya adalah hasil penjumlahan dari 2 bilangan sebelumnya.

Bilangan fibonacci selalu diawali oleh 2 angka, yaitu 0 dan 1.

Dan mulai bilangan ke-3, barulah setiap anggota deret fibonacci dikalkulasikan berdasarkan penjumlahan dua angka sebelumnya.

Sehingga nilai dari bilangan:

Ke-3 adalah hasil dari 0 + 1 = 1
Ke-4 adalah hasil dari 1 + 1 = 2
Ke-5 adalah hasil dari 2 + 1 = 3
Ke-6 adalah hasil dari 3 + 2 = 5
Ke-7 adalah hasil dari 5 + 3 = 8
dan seterusnya

Mengambil 2 angka sebelumnya lalu menyimpannya pada 2 variabel (yaitu angka1 dan angka2).
Membuat variabel baru dengan nama angkaSelanjutnya dengan nilai hasil penjumlahan dari angka1 dan angka2.
Hasil penjumlahan tersebut kita masukkan ke dalam list agar bisa digunakan untuk menentukan angka selanjutnya lagi.


jump
Jump Search (pencarian lompat) adalah algoritma pencarian dengan masukan berupa data/list (array) yang sudah terurut, 
dengan “melompati” beberapa elemen data sampai menemukan tepat sama dengan atau lebih dari elemen data yang dicari. 
Banyak elemen data yang dilompati tetap (konstan). Jika pada lompatan tertentu, pencarian tiba pada elemen data yang bernilai lebih dari yang dicari, maka mundur sebanyak 1 lompatan, dan kemudian mencari data satu per satu dengan pencarian linier.

Misalkan:

data disimpan dalam array berukuran  yaitu ,
elemen yang dicari adalah , dan
banyak elemen yang dilompati adalah ,
dengan 0 < m < n.

Dalam hal ini, diasumsikan indeks awal array adalah 0 



linier

Linear Search merupakan sebuah teknik pencarian data dengan menelusuri semua data satu per satu. 
Apabila ditemukan kecocokan data maka program akan mengembalikan output, jika tidak pencarian akan terus berlanjut hingga akhir dari array tersebut.



# ASD
POST TES 2

import math
def fibonacci_search(arr, x):
    fib1 = 0
    fib2 = 1
    fib3 = fib1 + fib2
    while fib3 < len(arr):
        fib1 = fib2
        fib2 = fib3
        fib3 = fib1 + fib2
    offset = -1
    while fib3 > 1:
        i = min(offset + fib1, len(arr) - 1)
        if isinstance(arr[i], list):
            sublist_index = fibonacci_search(arr[i], x)
            if sublist_index != -1:
                return [i, sublist_index]
            else:
                fib3 = fib1
                fib2 = fib2 - fib1
                fib1 = fib3 - fib2
                offset = i
        elif arr[i] < x:
            fib3 = fib2
            fib2 = fib1
            fib1 = fib3 - fib2
            offset = i
        elif arr[i] > x:
            fib3 = fib1
            fib2 = fib2 - fib1
            fib1 = fib3 - fib2
        else:
            return i
    if fib2 and arr[offset + 1] == x:
        return offset + 1
    else:
        return -1


var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

def jumpSearch(var, x):

    n = len(var)
    step = int(math.sqrt(n))
    prev = 0
    while compare(var[min(step, n) - 1], x) < 0:
        prev = step
        step += int(math.sqrt(n))
        if prev >=n:
            return -1
    while compare(var[prev], x) < 0:
        prev += 1
        if prev == min(step, n):
            return -1
    if compare(var[prev], x) == 0:
        return prev
    return -1


def compare(a, b):
    if isinstance(a, list):
        for elem in a:
            if compare(elem, b) == 0:
                return 0
        return -1
    else:
        return 1 if a > b else (-1 if a < b else 0)


def linear_search(arr,x):
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            SL_index = linear_search(arr[i],x)
            if SL_index != -1:
                return [i, SL_index]
        elif arr[i] == x:
            return i
    return -1


def tampilan():
    print("===========================          ===========================")
    print("|    Data yang tersedia   |          |   Metode yang digunakan |")
    print("|=========================|          |=========================|")
    print("|    Arsel                |          | 1. Fibbonaci            |")
    print("|    Avivah               |          | 2. Jump                 |")
    print("|    Daiva                |          | 3. Linier               |")
    print("|    Wahyu                |          ===========================")
    print("|    Wibi                 |")
    print("===========================")


    cari = input("Masukkan nama yang ingin dicari: ")
    pilihan = input("Masukkan Metode yang akan digunakan: " )
    print("")

    if pilihan == ("1") :
        var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
        index = fibonacci_search(var, cari)
        if index != -1:
            if isinstance(index, list):
                print("")
                print(f"{cari} berada di index {index[0]} kolom {index[1]}")
                print("")
                    
            else:
                print("")
                print(f"{cari} berada di index {index}")
                print("")
                ulang1 = input("Apakah Ingin mengulang? : ")
                if ulang1.lower() == "y" :
                    tampilan()
                elif ulang1.lower() == "n":
                    print("BYE!!!")
                    exit()
        else:
            print(f"{cari} tidak ditemukan pada list")
            print("")
            ulang2 = input("Apakah Ingin mengulang? : ")
            if ulang2.lower() == "y" :
                tampilan()
            elif ulang2.lower() == "n":
                print("BYE!!!")
                exit()


    elif pilihan == "2" :
        var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
        result = jumpSearch(var, cari)
        if result != -1:
            if isinstance(var[result], list):
                print("")
                print(f"{cari} ditemukan di index {result}, kolom ke-{var[result].index(cari)}")
                print("")

            else:
                print(f"{cari} ditemukan di index {result}")
                print("")
                ULG1 = input("Apakah ingin mengulang : ")
                if ULG1.lower().lower() == "y" :
                    tampilan()
                elif ULG1.lower().lower() == "n":
                    print("BYE!!!")
                    exit()
        else:
            print(f"{cari} tidak ditemukan dalam list")
            print("")
            ULG2 = input("Apakah ingin mengulang : ")
            if ULG2.lower().lower() == "y" :
                tampilan()
            elif ULG2.lower().lower() == "n":
                print("BYE!!!")
                exit()
    elif pilihan == "3" :
        var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
        result = jumpSearch(var, cari)
        if result != -1:
            if isinstance(var[result], list):
                print("")
                print(f"{cari} ditemukan di index {result}, kolom ke-{var[result].index(cari)}")
                print("")

            else:
                print(f"{cari} ditemukan di index {result}")
                print("")
                ULG3 = input("Apakah ingin mengulang : ")
                if ULG3.lower().lower() == "y" :
                    tampilan()
                elif ULG3.lower().lower() == "n":
                    print("BYE!!!")
                    exit()
        else:
            print(f"{cari} tidak ditemukan dalam list")
            print("")
            ULG4 = input("Apakah ingin mengulang : ")
            if ULG4.lower().lower() == "y" :
                tampilan()
            elif ULG4.lower().lower() == "n":
                print("BYE!!!")
                exit()

tampilan()

