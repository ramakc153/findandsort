import csv
import os
import math
from time import time

os.chdir(r"D:\Python\Alpro2\UAS")
file = csv.reader(open("super.csv", 'r'))

baris = [row for row in file]

##################################################################################
def bubble_sort(arr, kolom):
    n = len(arr)

    for x in range (n - 1):
        for y in range(0+1, n-x-1):
            if arr[y][kolom] > arr[y+1][kolom]:
                arr[y], arr[y+1] = arr[y+1], arr[y]
    
    return arr

# terurut = [','.join(row)+'\n' for row in bubble_sort(baris)]

# with open("1.csv", 'w+') as f:
#     f.writelines(terurut)

def jump(arr, find, kolom):
    global p_loncat
    n = len(arr)
    p_loncat = math.sqrt(n)
    
    while arr[int(p_loncat)][kolom] < find:
        p_loncat += math.sqrt(n)
        if p_loncat >= n:
            p_loncat = n-1
            break

    while arr[int(p_loncat)][kolom] > find:
        p_loncat -=1
        if p_loncat < 0:
            break

    if arr[int(p_loncat)][kolom] == find:
        print("Data found")
    else :
        print("data not found")

    return int(p_loncat)

# ####################################################################################

while True:
    menu = input("Masukkan Pilihan : ")

    if menu == '1':
        select = int(input("pilih kolom yang dicari : "))
        bubble_sort(baris, select)
        x = input("Masukkan data yang dicari : ")
        jump(baris, x, select)
        print(f'data ditemukan di kolom {baris[0][select]} di baris ke - {int(p_loncat)} ')

    elif menu == "2":
        select = int(input("pilih kolom yang di Sort : "))
        start = time()
        terurut = [','.join(row)+'\n' for row in bubble_sort(baris, select)]
        end = time()
        x = input("input nama file dengan ext .csv : ")
        with open(x, 'w+') as f:
            f.writelines(terurut)
        print(f"waktu yang dibutuhkan adalah {end-start:.2f}")
        # print()

    elif menu == '3':
        print("Terima kasih telah menggunakan program ini")
        break
