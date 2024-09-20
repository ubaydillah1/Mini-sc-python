## CASE BILANGAN GENAP
for i in range(1, 10, 2):
    print(i)

## FAKTORIAL
n = int(input("Masukkan bilangan bulat positif: "))
faktorial = 1

for i in range(1, n + 1):
    faktorial *= i

print(f"Faktorial dari {n} adalah {faktorial}.")

## SEGITIGA BINTANG SIKU
tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    print('*' * i)

## SEGITIGA BINTANG SEMPURNA
tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(tinggi):
    print(' ' * (tinggi - i - 1), end='')
    print('*' * (2 * i + 1))

## FIBONACCI
max_value = int(input("Masukkan nilai maksimum: "))
a, b = 0, 1

while a <= max_value:
    print(a, end=" ")
    a, b = b, a + b