class Mahasiswa:
    def __init__(self, nama, nim, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas

    def hitung_nilai_akhir(self):
        return (self.nilai_tugas + self.nilai_uts + self.nilai_uas) / 3

mahasiswa = []

while True:
    nama = input("Nama: ")
    nim = int(input("NIM: "))
    nilai_tugas = int(input("Nilai Tugas: "))
    nilai_uts = int(input("Nilai UTS: "))
    nilai_uas = int(input("Nilai UAS: "))

    mahasiswa.append(Mahasiswa(nama, nim, nilai_tugas, nilai_uts, nilai_uas))

    tambah_data = input("Tambah data (y/t)? ")
    if tambah_data.lower() == "t":
        break

print("-" * 60)
print("| No | Nama       | NIM  | Tugas | UTS  | UAS  | Akhir     |")
print("-" * 60)

for i, mhs in enumerate(mahasiswa):
    nilai_akhir = mhs.hitung_nilai_akhir()
    print(f"| {i+1:<2} | {mhs.nama:<10} | {mhs.nim:<4} | {mhs.nilai_tugas:<5} | {mhs.nilai_uts:<5} | {mhs.nilai_uas:<5} | {nilai_akhir:<9.2f} |")

print("-" * 60)