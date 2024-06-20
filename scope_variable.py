# message = "ERA"

# def greet():

#     # local variable
#     message = 'ARIN'
    
#     print('Local', message)

# greet()

# # try to access message variable 
# # outside greet() function
# print(message)


# # CONTOH 2
# # global variable
# c = 1 

# def add():
#     # use of global keyword
#     global c

#     # increment c by 2
#     c = c + 2

#     print(c)

# print(c)

# add()

# print(c)

# Contoh 3

saldo = 1000000

def cek_saldo():
    print(saldo)

def tarik_uang():
    global saldo
    saldo = saldo - 250000


tarik_uang()
print(saldo)
tarik_uang()
tarik_uang()

print(saldo)


