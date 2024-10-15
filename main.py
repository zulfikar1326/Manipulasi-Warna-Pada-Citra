# # # #pembuatan menu 1
import  cv2 as cv 
import numpy as np
import os
import time as tm 




def welcome(nameUser,delay=0.1):
    """Tulisan Welcome"""
    text = f"Selamat Datang {nameUser}"
    for karakter in text:
        print(karakter, end='', flush=True)
        tm.sleep(delay)

def opsiPilih():
    """Opsi Pilih"""
    for i in range(4):
        number = i+1
        if number == 1:
            print(f"{number} BGR ke Grayscale".upper())
        elif number  == 2:
            print(f"{number} BGR ke HSV".upper())
        elif number == 3:
            print(f"{number} BGR ke RGB".upper())
        elif number == 4:
            print(f"{number} Exit\n".upper())


def Konversicitrawarna(img,inputwarna):

    if inputwarna == '1':
        ubahBGR2GRAY = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return ubahBGR2GRAY
        
    elif inputwarna == '2':
        ubahBGR2HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        return ubahBGR2HSV
    
    elif inputwarna == '3':
        ubahBGR2RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return ubahBGR2RGB
    
    
def tampilkanFoto(img,name):
    cv.imshow(name,img)
    
    key = cv.waitKey(0)
    
    key = cv.waitKey(0) & 0xFF 
    if key == ord('x'):
        cv.destroyAllWindows()
        os.system('clear')
 
        
def main():
    inputName = input('Masukkan Nama Anda\t: ')
    inputImg = input('Masukkan Alamt Img\t :')
    
    alamat = f"./konversi warna citra/{inputImg}"
    img = cv.imread(alamat)
    
    
    os.system('clear')
    
    while True:
        welcome(inputName)
        print('\n')
        opsiPilih()
        
        menuPilih = input('Pilih menu (1,2,3) : ')
        print(menuPilih)
        
        if menuPilih == '1':
            print('=== BGR ke Grayscale ===')
            hasil = Konversicitrawarna(img, menuPilih)
            print(hasil)
            tampilkanFoto(hasil, inputName)

        elif menuPilih == '2':
            print('=== BGR ke HSV ===')
            hasil = Konversicitrawarna(img, menuPilih)
            tampilkanFoto(hasil, inputName)
            
        elif menuPilih == '3':
            print('=== BGR ke RGB ===')
            hasil = Konversicitrawarna(img, menuPilih)
            tampilkanFoto(hasil ,inputName)
        
        elif menuPilih == '4':
            exit(f'Terima Kasih Banyak {inputName}')
            
        else:
            print('Value Erorr')
            os.system('clear')
            
            
            

if __name__ == "__main__":
    main()