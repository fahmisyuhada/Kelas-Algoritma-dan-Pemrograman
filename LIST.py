age = 60

print(age)

ages = [60,70,80]
print(ages)

data = ["Abdul Wahab", 10, 175.5]

print(data)

mahasiswa = []
print(mahasiswa)


nama = "Nursikin"
print(nama)
listNama = list(nama)
print(listNama)
print(listNama[5])
print(listNama[3:])
print(listNama[:5])
print(listNama[1:7])

listNama.append(" ")
listNama.append("U")
listNama.append("L")
listNama.append("Y")
listNama.append("A")

listNama.append(" ")
listNama.append("A")
listNama.append("B")
listNama.append("A")
listNama.append("D")
listNama.append("I")
print(listNama)
listNama.insert(8,"A")
listNama.insert(9,"H")
print(listNama)

listNama2 = ['P','U','T','R','I']
listNama.extend(listNama2)
print(listNama)
listNama[4] = 'A'
print(listNama)
listNama.remove('A')
print(listNama)
print(len(listNama))

jumlah = 0
for item in listNama:
    jumlah+=1
    print(item)


print(jumlah)