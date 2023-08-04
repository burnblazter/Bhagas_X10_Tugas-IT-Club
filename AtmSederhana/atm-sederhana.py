#karena saya gabut jadi saya buat sekalian code pythonnya walaupun buat anda pasti ini terlalu simpel dan berntakan

#import random buat saldonya biar angkanya ga sama
import random

#bisa diganti jadi apapun yang penting angka
nomor_rekening = 10203040
pin_rekening = "000000"

#saldo random
saldo = random.randint(47000, 76000)

# define menu utama
def menu_utama():
    print("-----------------------------------------------------------------")
    print("\nSelamat datang di ATM sederhana buatan bhagas yang bahkan gatau buat apa :/\n")
    print("Anda pengen ngapain?")
    print("1. Cek uang")
    print("2. Tarik uang")
    print("3. Deposit uang") 
    print("4. Keluar")
    print("100. Hack atm") #cuma buat bercanda
    print("-----------------------------------------------------------------")

#define cek uang
def cek_uang():
    print("Uang anda di ATM Anda sisa: Rp ", saldo)

#define tarik uang
def tarik_uang(jumlah_tarik):
    global saldo
    if jumlah_tarik <= saldo:
        saldo -= jumlah_tarik
        print(f"Berhasil narik uang di atm anda tetapi tidak tau uangnya ketarik kemana yah? :D")
    else:
        print("Saldo tidak mencukupi hahahahhaha")

#define deposit uang
def deposit_uang(jumlah_deposit):
    global saldo
    saldo += jumlah_deposit
    print(f"Berhasil melakukan deposit sebesar Rp {jumlah_deposit}")

#menu utama
if __name__ == "__main__":
    print("Hai, silahkan login ke akun Anda")

    while True:
        input_nomor_rekening = input("Masukkan nomor akun: ")
        input_pin_rekening = input("Masukkan PIN: ")
    
        if input_nomor_rekening == str(nomor_rekening) and input_pin_rekening == pin_rekening:
            print("Berhasil login!")
            while True:
                menu_utama()
                pilihan = input("Pilih [1/2/3/4]: ")

                if pilihan == '1': #PILIHAN 1
                    cek_uang()
                elif pilihan == '2': #PILIHAN 2
                    jumlah_tarik = int(input("Berapa uang yang mau ditarik: "))
                    tarik_uang(jumlah_tarik)
                elif pilihan == '3': #PILIHAN 3
                    jumlah_deposit = int(input("Berapa uang yang mau di deposit: "))
                    deposit_uang(jumlah_deposit)
                elif pilihan == '4': #PILIHAN 4
                    print("Terima kasih telah menggunakan atm sederhana")
                    break
                  
                elif pilihan == '100': #PILIHAN 100
                  print("Selamat! Uang anda di atm telah di kosongkan karena anda mencoba ngehack di atm saya bwahahaha")
                  saldo = 0
                else:
                    print("Pilihan menu yang anda ketik ngawur!")
        else:
            print("Nomor rekening atau pin rekening salah, hayuu!.")
