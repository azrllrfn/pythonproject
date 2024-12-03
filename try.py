class Orang:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age  # Memperbaiki penamaan atribut

    def tampilkan(self):
        print(f"Nama: {self.name}")
        print(f"Usia: {self.age}")

# Membuat objek dari kelas Orang
orang1 = Orang("Alice", 25)
orang2 = Orang("Bob", 30)  # Menggunakan nilai default untuk usia

# Memanggil metode tampilkan
orang1.tampilkan()
orang2.tampilkan()

# Mencetak atribut langsung dari objek
print(f"Nama dari orang1: {orang1.name}, Usia: {orang1.age}")
print(f"Nama dari orang2: {orang2.name}, Usia: {orang2.age}")