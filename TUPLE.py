
# # tuple of string types
# names = ('James', "Bambang", "Cecep", "Deden", "Elsa","Fikri","Hery", "Indah","Jamal","Kiki","Linda")

# # names[0]= "JAMAL"
# print (names)

# ada = False

# cari_nama = "Linda"
# for nama in names:
#     if nama == cari_nama:
#         ada = True

# print(ada)

# print("Fikri" in names)

# print(names[0][3])

# # names[1][0] = 'k'

# cerita = """
# Sesampainya di pasar, suasana ramai dan hiruk pikuk langsung menyambut mereka. Pedagang berteriak menawarkan dagangannya, aroma rempah dan sayur mayur segar memenuhi udara. Juliani memilih sayuran segar, Rima mencari buah-buahan, dan Arin sibuk membeli bumbu dapur yang langka.
# """

# print("pasar" in cerita)
# print(cerita.index("pasar"))

nama = "azzlinae"

print(nama)
upperName = nama.upper()
print(upperName)
print(upperName.lower())

text = "pantai ini indah sekali, banyak sekali sampai"
print(text)

partText = text.partition(" ")
print(partText)

chars = set(text)
print(chars)
for char in chars:
    print(char , " = ", text.count(char))
