import tkinter as tk
# import random
import random
angkarandom = 1

def run_mulai():
    global angkarandom
    labeljudul.config(text="Silahkan Pasang Taruhan")
    angkarandom = random.randint(1, 3)

def run_stop():
    label2.config(bg="blue")

def pilihan1():
    global angkarandom
    if angkarandom == 1:
        labeljudul.config(text="Selamat, Anda mendapatkan Jack Pot")
    else:
        labeljudul.config(text="Mohon Bersabar, Ini Ujian. Anda tertipu")
def pilihan2():
    global angkarandom
    if angkarandom == 2:
        labeljudul.config(text="Selamat, Anda mendapatkan Jack Pot")
    else:
        labeljudul.config(text="Mohon Bersabar, Ini Ujian. Anda tertipu")
def pilihan3():
    global angkarandom
    if angkarandom == 3:
        labeljudul.config(text="Selamat, Anda mendapatkan Jack Pot")
    else:
        labeljudul.config(text="Mohon Bersabar, Ini Ujian. Anda tertipu")
window1 = tk.Tk()
window1.geometry("400x400")

labeljudul = tk.Label(window1, text="Game tebak-tebakan")
label1 = tk.Label(window1, text="Kotak", bg="red")
label2 = tk.Label(window1, text="kotak", bg="green")
label3 = tk.Label(window1, text="kotak", bg="red")

tombol1 = tk.Button(window1, text="Kotak 1", command=pilihan1)
tombol2 = tk.Button(window1, text="Kotak 2", command=pilihan2)
tombol3 = tk.Button(window1, text="Kotak 3", command=pilihan3)

tombol_mulai = tk.Button(window1, text="MULAI", command=run_mulai)
tombol_stop = tk.Button(window1, text="STOP", command=run_stop)

labeljudul.grid(row=0, column=0, columnspan=3, pady=10)
label1.grid(row=1, column=0, padx=20)
label2.grid(row=1, column=1, padx=20)
label3.grid(row=1, column=2, padx=20)
tombol1.grid(row=2, column=0,padx=20, pady=20)
tombol2.grid(row=2, column=1,padx=20, pady=20)
tombol3.grid(row=2, column=2,padx=20, pady=20)

tombol_mulai.grid(row=3, column=0,columnspan=3, padx=20, pady=20)
tombol_stop.grid(row=4, column=0,padx=20, columnspan=3, pady=20)

window1.mainloop()