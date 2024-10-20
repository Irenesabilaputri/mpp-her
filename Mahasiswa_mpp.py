# List untuk menyimpan data mahasiswa
mahasiswa_list = []

# Fungsi tambah data mahasiswa
def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    prodi = input("Masukkan Program Studi: ")
    ipk = float(input("Masukkan IPK: "))
    mahasiswa_list.append({"NIM": nim, "Nama": nama, "Prodi": prodi, "IPK": ipk})
    print("Data mahasiswa berhasil ditambahkan.\n")

# Fungsi melihat data mahasiswa
def lihat_mahasiswa():
    if len(mahasiswa_list) == 0:
        print("Belum ada data mahasiswa.\n")
    else:
        for mhs in mahasiswa_list:
            print(f"NIM: {mhs['NIM']}, Nama: {mhs['Nama']}, Prodi: {mhs['Prodi']}, IPK: {mhs['IPK']}")
        print()

# Fungsi mencari mahasiswa
def cari_mahasiswa():
    nim = input("Masukkan NIM yang dicari: ")
    for mhs in mahasiswa_list:
        if mhs['NIM'] == nim:
            print(f"Data ditemukan: NIM: {mhs['NIM']}, Nama: {mhs['Nama']}, Prodi: {mhs['Prodi']}, IPK: {mhs['IPK']}\n")
            return
    print("Data mahasiswa tidak ditemukan.\n")

# Fungsi ubah data mahasiswa
def ubah_mahasiswa():
    nim = input("Masukkan NIM yang ingin diubah: ")
    for mhs in mahasiswa_list:
        if mhs['NIM'] == nim:
            mhs['Nama'] = input("Masukkan Nama baru: ")
            mhs['Prodi'] = input("Masukkan Program Studi baru: ")
            mhs['IPK'] = float(input("Masukkan IPK baru: "))
            print("Data mahasiswa berhasil diubah.\n")
            return
    print("Data mahasiswa tidak ditemukan.\n")

# Fungsi hapus data mahasiswa
def hapus_mahasiswa():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    for mhs in mahasiswa_list:
        if mhs['NIM'] == nim:
            mahasiswa_list.remove(mhs)
            print("Data mahasiswa berhasil dihapus.\n")
            return
    print("Data mahasiswa tidak ditemukan.\n")

# Fungsi utama
def main():
    while True:
        print("=== Menu ===")
        print("1. Tambah Data Mahasiswa")
        print("2. Lihat Data Mahasiswa")
        print("3. Cari Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            lihat_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            ubah_mahasiswa()
        elif pilihan == "5":
            hapus_mahasiswa()
        elif pilihan == "6":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")

if __name__ == "__main__":
    main()
