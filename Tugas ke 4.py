masukkan_bilangan = int(input("Masukkan Angka yang Ingin Anda Konversi: "))
print("Pilih metode konversi:")
print("1. Biner")
print("2. Oktal")
print("3. Desimal (Tidak Berubah)")
print("4. Hexadesimal")

masukkan_pilihan_user = int(input("Pilih 1, 2, 3, atau 4: "))

def pilih_operasi(pilihan, bilangan):
    if pilihan == 1:
        print("Bilangan Biner Dari", bilangan, "Adalah", bin(bilangan)[2:])
    elif pilihan == 2:
        print("Bilangan Oktal Dari", bilangan, "Adalah", oct(bilangan)[2:])
    elif pilihan == 3:
        print("Bilangan Desimal Dari", bilangan, "Adalah", bilangan)
    elif pilihan == 4:
        print("Bilangan Hexadesimal Dari", bilangan, "Adalah", hex(bilangan)[2:])
    else:
        print("Pilihan Tidak Valid")

pilih_operasi(masukkan_pilihan_user, masukkan_bilangan)