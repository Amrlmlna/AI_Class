import random

while True:
    NumRandom = random.choices(range(1, 11), k=20)
    print("List angka acak:", NumRandom)

    NumOption = int(input("Pilih Angka antara 1 s/d 10 : "))

    IndexNumList = [index for index, value in enumerate(NumRandom) if value == NumOption]

    if IndexNumList:
        if NumOption % 2 == 0:
            print(f"Y1 : angka yang anda pilih berada pada index {IndexNumList} dan merupakan bilangan genap")
        else:
            print(f"Y1 : angka yang anda pilih berada pada index {IndexNumList}")
    else:
        print("angka yang anda pilih tidak ada dalam list atau tidak genap")

    retry = input("Apakah anda ingin mencoba program ini lagi? (y/n): ").strip().lower()
    if retry != 'y':
        print("Program selesai. Terima kasih banyak!")
        break
