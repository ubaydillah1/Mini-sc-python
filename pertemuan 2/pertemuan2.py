umur = 17

# FORMATTED STRING
# print("umur :", umur)
# print(f"umur : {umur}")

# nama_baru = "UDIN" # SNAKE CASE
# namaBaru = "Udin" # CAMEL CASE

# IF STATEMENT
a = 11

# if (kondisi):
# if a == 10:
#     print("a adalah 10")

# # elif (kondisi):
# a = 11
# if a == 10:
#     print("a adalah 10")
# elif a == 11:
#     print("a adalah 11")
# elif a == 12:
#     print("a adalah 12")

# # else:
# a = 11
# if a > 10:
#     print("a lebih besar dari 10")
# else:
#     print("a kurang dari 10")

# input
# angka = int(input("Masukkan angka : "))

# if (angka % 2 == 0):
#     print("Angka genap")
# else:
#     print("Angka ganjil")


# PERULANGAN

# while(kondisi): (membuka break dan continue)
# a = 1

# while(a < 5):
#     a = a + 1
#     if a == 3:
#         continue

#     print(a)


# for i in range(start, stop, step):

# kondisi 1 parameter
# for i in range(10):
#     print(i)

# kondisi 2 parameter
# for i in range(1, 10):
#     print(i)

# kondisi 3 parameter
# for i in range(1 , 20, 3):
#     print(i)
tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(tinggi):
    print(' ' * (tinggi - i - 1), end='')
    print('*' * (2 * i + 1))
    