import time,os

Ras_Kucing  = ["Persia","Anggora","Mixdom","Himalaya"]

def cl():
        os.system('cls')
        time.sleep(1)

def tampilan():
    print("=======================")
    print("| Daftar Kucing       |")
    print("=======================")
    print("| 1. Persia           |")
    print("| 2. Anggora          |")
    print("| 3. Mixdom           |")
    print("| 2. Himalaya         |")
    print("=======================")


def menu():
    print("==================================")
    print("| Ingin melakukan apa?           |")
    print("|================================|")
    print("| 1. Menambahkan                 |")
    print("| 2. akses                       |")
    print("| 3. total data                  |")
    print("| 4. menghapus                   |")
    print("| 5. mengubah                    |")
    print("| 6. Mengurutkan sesuai Alfabert |")
    print("==================================")
    create = input("Silahkan Input Nomor Berapa : ")
    if create == '1':
        print("")
        adminMemilih1 = input("Masukan Nama Kucing : ")
        print("")
        Ras_Kucing.append(adminMemilih1)
        for x in Ras_Kucing:
            print(x)
            print("")
        kembali = input("Apakah ingin kembali ke menu awal? Y/N :")
        if kembali == "Y" :
            cl()
            menu()
        elif kembali == "N" :
            exit()
    elif create == "2" :
        print("")
        for x in Ras_Kucing:
            print(x)
            print("")
        akses = input("Ingin mengaksesnya satu-satu? Y/N :")
        if akses == "Y" :
            akses2 = input ("Silahkan Masukan index nya : ")
            if akses2 == "0" :
                a = Ras_Kucing[0]
                print("")
                print(a)
                kembali2 = input("Apakah ingin kembali ke menu awal? Y/N :")
                if kembali2 == "Y" :
                    menu()
                elif kembali2 == "N" :
                    exit()
            elif akses2 == "1" :
                b = Ras_Kucing[1]
                print("")
                print(b)
                print("")
                kembali2b = input("Apakah ingin kembali ke menu awal? Y/N :")
                if kembali2b == "Y" :
                    menu()
                elif kembali2b == "N" :
                    exit()
            elif akses2 == "2" :
                c = Ras_Kucing[2]
                print("")
                print(c)
                print("")
                kembali2c = input("Apakah ingin kembali ke menu awal? Y/N : ")
                if kembali2c == "Y" :
                    menu()
                elif kembali2c == "N" :
                    exit()
            elif akses2 == "3" :
                d = Ras_Kucing[3]
                print("")
                print(d)
                print("")
                kembali2d = input("Apakah ingin kembali ke menu awal? Y/N :")
                if kembali2d == "Y" :
                    menu()
                elif kembali2d == "N" :
                    exit()
    elif create == '3':
        total = len(Ras_Kucing)
        print(total)
    elif create == '4':
        print("")
        for d in Ras_Kucing:
            print(d)
        print("")
        menghapus = int(input("Masukkan index yang ingin di hapus : "))
        print("")
        Ras_Kucing.pop(menghapus)
        for y in Ras_Kucing:
            print(y)
    elif create == "5" :
        print("")
        for x in Ras_Kucing:
            print(x)
        print("")
        mengubah = int(input("Silahkan masukkan index yang ingin di ubah : "))
        namaubah = input("silahkan masukan nama kucing yang baru : ")
        Ras_Kucing[mengubah] = namaubah
        print("")
        for p in Ras_Kucing:
            print(p)
    elif create == "6" :
        print("")
        Ras_Kucing.sort()
        for w in Ras_Kucing :
            print(w)

tampilan()
menu()