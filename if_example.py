#n=98
n=int(input("Masukkan Teks :"))
print(str(n))
if n > 90:
    print("Nilai ", n," Bagus Sekali")
elif n > 80 and n <=90:
    print("Nilai ",n, " Bagus")
else:
    print("Nilai ",n," Tidak Bagus")