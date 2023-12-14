import os
f = open("saldo.txt")

isi = f.read()
saldo = int(isi)
saldo = saldo+100000
print(saldo)
f.close()

os.remove("saldo.txt")
f = open("saldo.txt", "a")
f.write(str(saldo))
f.close()
