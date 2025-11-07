#1-misol
def factorial(n):
    natija = 1
    for i in range(1, n + 1):
        natija *= i
    return natija

son = int(input("Son kiriting: "))
print("Faktorial:", factorial(son))

#2-misol
def palindrommi(matn):
    return matn == matn[::-1]

s = input("So‘z yoki satr kiriting: ")
if palindrommi(s):
    print("Bu palindrom!")
else:
    print("Bu palindrom emas.")

#3-misol
def katta_kichik(royxat):
    return max(royxat), min(royxat)

sonlar = list(map(int, input("Raqamlarni probel bilan kiriting: ").split()))
katta, kichik = katta_kichik(sonlar)
print(f"Katta: {katta}, Kichik: {kichik}")

#4-misol
def unli_soni(matn):
    unlilar = "aeiouAEIOUаеиоуяюёэАЕИОУЯЮЁЭ"
    return sum(1 for harf in matn if harf in unlilar)

satr = input("Satr kiriting: ")
print("Unli harflar soni:", unli_soni(satr))

#5-misol
def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

son = int(input("Son kiriting: "))
print("Tub sonmi:", tubmi(son))
