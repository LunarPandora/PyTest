import cv as cv
import luas_persegi_panjang as lpp
import konverter_suhu as ks
import konverter_detik as kd
import luas_lingkaran as ll

from os import system

def clearWindow():
    system('cls')

repeat = True

print("""
Selamat datang!
Silahkan pilih program yang ingin anda jalankan.      
"""
)

while repeat:
    
    print("""
1. Tampilkan Curriculum Vitae
2. Hitung Luas Persegi Panjang
3. Konverter Celcius ke Reamur dan Fahrenheit
4. Konverter Detik
5. Hitung Luas Lingkaran
""")
    
    pilihan = input("Pilih operasi sesuai dengan nomor yang telah dicantumkan : ")
    if pilihan == "1":
        cv.info_cv()
    elif pilihan == "2":
        p = input("Masukkan panjang (p) : ")
        l = input("Masukkan lebar (l) : ")
        
        lpp.hitung_luas(p, l)
    elif pilihan == "3":
        c = input("Masukkan suhu celcius yang ingin dikonversi : ")
        
        ks.c_to_another(c)
    elif pilihan == "4":
        d = input("Masukkan jumlah detik yang ingin dikonversi : ")
        
        kd.konv_dtk(d)
    elif pilihan == "5":
        r = input("Masukkan jari-jari lingkaran yang ingin dihitung luasnya : ")
        
        ll.lingkaran(r)
    else:
        print("Harap memilih pilihan yang disediakan diatas dan cantumkan sesuai angka yang tertera.")

    replay_program = input('Apakah anda ingin mengulang program? (y/n):').lower()
      
    if replay_program == 'y':
        clearWindow()
        status_program = True
    elif replay_program == 'n':
        raise SystemExit()
    else:
        raise SystemExit()

    