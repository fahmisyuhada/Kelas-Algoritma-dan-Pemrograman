
def encript(pesan_text,kode):
    pesan_tersembunyi = ""
    for i in pesan_text:
        pesan_tersembunyi = pesan_tersembunyi+chr(ord(i)+kode)
    return pesan_tersembunyi


def decript(pesan_text, kode):
    pesan_tersembunyi = ""
    for i in pesan_text:
        pesan_tersembunyi = pesan_tersembunyi+chr(ord(i)-kode)
    return pesan_tersembunyi


pesan_tersembunyi = encript("Pipin dan kiki bertemu dengan romi tadi malam",9)
print(pesan_tersembunyi)

pesan = decript("Yryrw)mjw)trtr)kn{}nv~)mnwpjw){xvr)}jmr)vjujv",10)
print(pesan)

# orek2an
#        print(i,"-",ord(i), "-", ord(i)+4, "-",chr(ord(i)+4))