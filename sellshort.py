def shellShort(data):
    gap = (len(data)//2)
    a=0

    while gap > 0 :
        for i in range(gap,len(data)):
            value = data[i]
            j = i

            while j >= gap and data[j-gap] > value:
                data[j] = data[j-gap]
                j-=gap

            data[j] = value
            print(data)
        print("Iterasi ke",a,": ",data,"dengan gap ",gap )
        a+=1

        gap //= 2

    return data

sampel=[-2,14,37,11,1,-99,6]

print("Sebelum di-sort :",sampel)
print("Setelah di-sort :",shellShort(sampel))