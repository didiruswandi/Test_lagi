#Konsep OOP
#Class
#attribute
#method
#Inheritance

class Mobil: #class
    jumlah_mobil=0 #attribute kelas
    def __init__(self, merk, warna, harga) :
        self.merk=merk #attribute
        self.warna=warna
        self.harga=harga
        Mobil.jumlah_mobil+=1
        
    def into(self):
        return f"{self.merk} berwarna {self.warna}, dengan harga {self.harga}, jumlah mobil saat ini {self.jumlah_mobil}"
#object/instance    
mobil1=Mobil("Toyota","Hitam","100jt") #instance/object
mobil2=Mobil("Toyota","Putih","200jt")

print(mobil2.into())      

@classmethod
def get_jumlah_mobil(cls):
    kali2=cls.jumlah_mobil*2
    return kali2

mobil1=Mobil("Toyota","Hitam","100jt") #instance/object

print(mobil1.into())
print(f"Jumlah Mobil:{Mobil.hitung_jumlah_mobil()}")    
        