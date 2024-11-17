Nama: ZAENAL MAULANA RIZKI

Kelas: TI.24.A4

NIM: 312410332

Matkul: Bahasa Pemrograman

# Latihan Praktikum

![Screenshot 2024-11-12 043342](https://github.com/user-attachments/assets/da0566b2-98de-418e-81bd-27c8c573022a)

# Elemen.py

```python
list_a = [1, 2, 3, 4, 5]

print(list_a[2])

print(list_a[1:4])

print(list_a[-1])

list_a[3] = 10
print(list_a)

list_a[3:] = [11, 12, 13]
print(list_a)

list_b = list_a[:2]
print(list_b)

list_b.append("misalnya")
print(list_b)

list_b.extend([14, 15, 16])
print(list_b)

list_a.extend(list_b)
print(list_a)
```

Code Program tersebut:

![code](https://github.com/user-attachments/assets/5ace10b3-4dfe-463f-ab04-2a81f780c072)

hasil program tersebut:

![Screenshot (96)](https://github.com/user-attachments/assets/7b2296f8-6ef2-4de1-b58c-508ebb179828)

# Menambah data.py

```python
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
```

# Penjelasan Code Menambah data

```python
class Mahasiswa:
    def __init__(self, nama, nim, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
```
`__init__`: Konstruktor ini digunakan untuk menginisialisasi objek Mahasiswa dengan atribut: `nama`, `nim`, `nilai_tugas`, `nilai_uts`, `nilai_uas`

```python
def hitung_nilai_akhir(self):
    return (self.nilai_tugas + self.nilai_uts + self.nilai_uas) / 3
```
Metode ini mengembalikan nilai akhir mahasiswa, yang merupakan rata-rata dari `nilai_tugas`, `nilai_uts`, dan `nilai_uas`.

```python
mahasiswa = []
```
Sebuah daftar kosong `mahasiswa` disiapkan untuk menyimpan objek `Mahasiswa` yang akan ditambahkan

```python
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
```
Meminta pengguna untuk memasukkan data mahasiswa berulang kali hingga pengguna memasukkan `t` untuk berhenti, Setiap input digunakan untuk membuat data Mahasiswa, yang kemudian ditambahkan ke dalam daftar mahasiswa

```python
print("-" * 60)
print("| No | Nama       | NIM  | Tugas | UTS  | UAS  | Akhir     |")
print("-" * 60)

for i, mhs in enumerate(mahasiswa):
    nilai_akhir = mhs.hitung_nilai_akhir()
    print(f"| {i+1:<2} | {mhs.nama:<10} | {mhs.nim:<4} | {mhs.nilai_tugas:<5} | {mhs.nilai_uts:<5} | {mhs.nilai_uas:<5} | {nilai_akhir:<9.2f} |")

print("-" * 60)
```
`Header` tabel dicetak terlebih dahulu, diikuti oleh baris-baris data untuk setiap mahasiswa, Untuk setiap mahasiswa, metode `hitung_nilai_akhir` dipanggil untuk menghitung nilai akhir, lalu data ditampilkan dalam format tabel

Code Program tersebut:

![code1](https://github.com/user-attachments/assets/0903d295-6ab5-4e54-af81-5d7aa8a16e07)

Hasil Program tersebut:

![Screenshot (97)](https://github.com/user-attachments/assets/13894f5e-630b-4368-9066-f1a86d341cf7)

Dan ini flowchart nya:

![Screenshot 2024-11-13 083635](https://github.com/user-attachments/assets/29eddd86-de3f-40e8-b1bb-9920b529cede)
