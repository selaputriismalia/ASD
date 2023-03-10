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