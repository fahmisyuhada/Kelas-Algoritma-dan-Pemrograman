"""
Buatlah 1 Kelompok 6 Orang presentasikan senin
depan
Kasus :

Sylpie pergi ke supermarket membeli telur,
tepung, minyak, gula, garam. Harga masing-masing
barang seperti berikut
telur = 2500
tepung = 9000
minyak = 16000
gula = 8000
garam = 2500

Sylpie ingin semua barang tersebut sesuai
keinginnannya. buatlah program yang
akan menampilkan output seperti berikut
================================================
|| Nama barang || Quan || Hrg Satuan || Total ||
|| ========================================== ||
|| Telur       ||   3  ||  2500      || 7500  ||
|| tepung      ||   2  ||  9000      || 18000 ||
|| minyak      ||   1  ||  16000     || 16000 ||
|| gula        ||   14 ||  8000      || 114000||
|| garam       ||   10 ||  2500      || 25000 ||
================================================
||                        Total      || 900000||
||                    Jumlah Uang    ||1000000 ||
||                  Kembalian        || 100000 ||
================================================
||    Terima kasih sudah berbelanja di toko   ||
||             Indri Septiani                 ||
================================================

"""

# 1. Inisialisasi/kumpulkan data data barang 

telur = 2500
tepung = 9000
minyak = 16000
gula = 8000
garam = 2500

# 2. masukkan jumlah masing-masing barang yang ingin dibeli
# sesuai yang diinputkan user
jml_telur = float(input("Masukkan Jumlah Telur : "))
jml_tepung = float(input("Masukkan Jumlah Tepung : "))
jml_minyak = float(input("Masukkan Jumlah Minyak : "))
jml_gula = float(input("Masukkan Jumlah Gula : "))
jml_garam = float(input("Masukkan Jumlah Garam : "))

# 3. Hitung total harga masing-masing barang
total_telur = jml_telur*telur
total_tepung = jml_tepung*tepung
total_minyak = jml_minyak*minyak
total_gula = jml_gula*gula
total_garam = jml_garam*garam

# 4. Hitung total belanja dari total seluruh barang
total_belanja = total_telur + total_tepung+total_minyak+total_gula+total_garam

# 5. Masukkan junlah uang dari input user
jumlah_uang = float(input("Masukkan Jumlah Uang anda : "))

# 6. hitung jumlah kembalian
jumlah_kembalian = jumlah_uang -total_belanja

# 7. Cetak stru

print("=====================================================")
print("|| Nama barang || Quan || Hrg Satuan || Total ||")
print("|| ========================================== ||")
print(f"|| Telur       ||   {jml_telur}  ||  {telur}      || {total_telur}  ||")
print(f"|| Tepung       ||   {jml_tepung}  ||  {tepung}      || {total_tepung}  ||")
print(f"|| Minyak       ||   {jml_minyak}  ||  {minyak}      || {total_minyak}  ||")
print(f"|| Gula       ||   {jml_gula}  ||  {gula}      || {total_gula}  ||")
print(f"|| Garam       ||   {jml_garam}  ||  {garam}      || {total_garam}  ||")
print("================================================")
print(f"||                        Total      || {total_belanja}||")
print(f"||                    Jumlah Uang    ||{jumlah_uang} ||")
print(f"||                  Kembalian        || {jumlah_kembalian} ||")
print("================================================")
print("||    Terima kasih sudah berbelanja di toko   ||")
print("||             Indri Septiani                 ||")
print("================================================")



