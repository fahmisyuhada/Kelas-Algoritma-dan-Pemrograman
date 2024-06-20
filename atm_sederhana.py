import menu as mn 


saldo = 0




def proses_tarik_uang():
    global saldo
    print("ini adalah proes tarik uang")
    saldo = saldo - 100000
    cek_saldo()

def cek_saldo():
    print("Saldo anda : ", saldo)
    print("ini adalah menu untuk tampilkan saldo")

running = True

while(running):

    # pin = input("Masukkan PIN anda : ")
    pin = "123456"
    if(pin == "123456"):
        saldo = 1000000
        mn.menu()
        pilihan = int(input("Masukkan Menu : "))
        if pilihan == 4:
            running = False
            print("Terima kasih sudah menggunakan layanan ATM Bank Sederhana")
        elif pilihan == 1:
            cek_saldo()
        elif pilihan == 2:
            proses_tarik_uang()
    else:
        print("PIN ANDA SALAH, SILAHKAN MASUKKAN PIN YANG BENAR")    


