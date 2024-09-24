# casting (perubahan tipe data)
# data = int(input("Masukkan angka : "))
# print(type(data))

# FUNGSI
# def cetak_halo():
#     print("Halo")

# cetak_halo()
# cetak_halo()
# cetak_halo()
# cetak_halo()


# FUNGSI PERTAMBAHAN
# def pertambahan(a, b):
#     return a + b

# print(pertambahan(10, 20))

# FUNGSI OPERASI MATEMATIKA
# RETURN VALUE LEBIH DARI 1
# def operasi_matematika(a,b):
#     pertambahan = a + b
#     pengurangan = a - b
#     perkalian = a * b
#     pembagian = a / b

#     return pertambahan, pengurangan, perkalian, pembagian

# a, b, c, d = operasi_matematika(20, 10)
# print(a)
# print(b)
# print(c)
# print(d)

# FUNGSI REKURSIF
# def rekursif(n):
#     if (n == 0):
#         return 1
    
#     return n * rekursif(n - 1)

# print(rekursif(4))

# VARIABEL GLOBAL DAN LOKAL VARIABEL
# a = 10
# def cetak():
#     return a # mengambil global variabel
# print(cetak())

def pertambahan(a, b):
    return f"hasil dari {a} + {b} adalah {a + b}"

def pengurangan(a, b):
    return f"hasil dari {a} - {b} adalah {a - b}"

def perkalian(a, b):
    return f"hasil dari {a} * {b} adalah {a * b}"

def pembagian(a, b):
    return f"hasil dari {a} / {b} adalah {a * b}"




while(True):
    print("===SELAMAT DATANG DI OPERASI MATEMATIKA===")
    print("1. pertambahan")
    print("2. pengurangan")
    print("3. perkalian")
    print("4. pembagian")

    input_user = int(input("Masukkan operasi yang kalian mau : "))
    angka1 = int(input("Masukkan angka 1 : "))
    angka2 = int(input("Masukkan angka 2 : "))

    if (input_user == 1):
        print(pertambahan(angka1, angka2))
    elif (input_user == 2):
        print(pengurangan(angka1, angka2))
    elif (input_user == 3):
        print(perkalian(angka1, angka2))
    elif (input_user == 4):
        print(pembagian(angka1, angka2))

    opsi = input("Mau lagi ? (y/n) : ")

    if (opsi == "y"):
        continue
    else:
        break