import csv
import os
import math
from time import time

os.chdir(r"D:\Python\Alpro2\UAS")
file = csv.reader(open("super.csv", 'r'))

baris = [row for row in file]

def clear():  #
    os.system('cls')

##################################################################################
def bubble_sort(data, kolom):
    n = len(data)

    for x in range (n - 1):
        for y in range(0+1, n-x-1):
            if data[y][kolom] > data[y+1][kolom]:
                data[y], data[y+1] = data[y+1], data[y]
    
    return data



def jump(data, find, kolom):
    global p_loncat
    n = len(data)
    p_loncat = math.sqrt(n)
    
    while data[int(p_loncat)][kolom] < find:
        p_loncat += math.sqrt(n)
        if p_loncat >= n:
            p_loncat = n-1
            break

    while data[int(p_loncat)][kolom] > find:
        p_loncat -=1
        if p_loncat < 0:
            break

    if data[int(p_loncat)][kolom] == find:
        print("Data found")
        return 1
    else :
        return 0

    # return int(p_loncat)

# ####################################################################################

while True:
    clear()
    print("""
1. Searching Data
2. Sorting Data
3.  Exit""")
    menu = input("Masukkan Pilihan : ")

    if menu == '1':
        select = int(input("pilih kolom yang dicari : "))
        print(f"Anda melakukan searching pada kolom {baris[0][select]} ")
        print("Sedang dilakukan Sorting...")
        bubble_sort(baris, select)
        print("Sorting Selesai")
        x = input("Masukkan data yang dicari : ")
        search = jump(baris, x, select)
        if search == 1:    
            print(f'data ditemukan di kolom {baris[0][select]} di baris ke - {int(p_loncat)} ')
            print(f'{baris[0]}')
            print(f'{baris[int(p_loncat)]}  ')
        else :
            print(f"Data {x} yang dicari tidak ditemukan ")

    elif menu == "2":
        select = int(input("pilih kolom yang di Sort : "))
        print(f"Anda melakukan sorting pada kolom {baris[0][select]} ")
        print("Sedang dilakukan Sorting...")
        start = time()
        terurut = [','.join(row)+'\n' for row in bubble_sort(baris, select)]
        end = time()
        print("Sorting Selesai")
        x = input("input nama file dengan ext .csv : ")
        with open(x, 'w+') as f:
            f.writelines(terurut)
        print(f"waktu yang dibutuhkan adalah {end-start:.2f} detik")
        # print()

    else:
        print("Terima kasih telah menggunakan program ini")
        break

    print("Apakah anda ingin lanjut (y/n) ? ")

    menu = input("Masukkan Pilihan : ")
    if menu == 'n':
        print("Terima kasih telah menggunakan program ini")
        break
    else:
        clear()

