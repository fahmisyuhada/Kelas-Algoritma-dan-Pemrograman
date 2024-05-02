
saldo = 0

def menu():
    print("="*40)
    print("=== Selamat Datang di ATM Sederhana ====")
    print("="*40)

    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Setor Uang")
    print("4. Keluar")

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
        menu()
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


