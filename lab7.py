class DaftarMahasiswa:
    def __init__(self):
        # Menyimpan data mahasiswa dalam dictionary
        self.mahasiswa = {}

    # Method untuk menambah data
    def tambah(self):
        print("\n=== Tambah Data Mahasiswa ===")
        nama = input("Nama        : ")
        tugas = float(input("Nilai Tugas : "))
        uts = float(input("Nilai UTS   : "))
        uas = float(input("Nilai UAS   : "))

        self.mahasiswa[nama] = {
            "tugas": tugas,
            "uts": uts,
            "uas": uas
        }

        print(f"Data '{nama}' berhasil ditambahkan!\n")

    # Method untuk menampilkan data
    def tampilkan(self):
        print("\n=== Daftar Nilai Mahasiswa ===")
        if not self.mahasiswa:
            print("Belum ada data.\n")
            return

        for nama, nilai in self.mahasiswa.items():
            print(f"Nama  : {nama}")
            print(f"  Tugas : {nilai['tugas']}")
            print(f"  UTS   : {nilai['uts']}")
            print(f"  UAS   : {nilai['uas']}")
            print("-" * 30)

    # Method untuk menghapus data
    def hapus(self, nama):
        if nama in self.mahasiswa:
            del self.mahasiswa[nama]
            print(f"Data '{nama}' berhasil dihapus!\n")
        else:
            print(f"Data '{nama}' tidak ditemukan!\n")

    # Method untuk mengubah data
    def ubah(self, nama):
        if nama in self.mahasiswa:
            print(f"\n=== Ubah Data Mahasiswa: {nama} ===")
            tugas = float(input("Nilai Tugas baru : "))
            uts = float(input("Nilai UTS baru   : "))
            uas = float(input("Nilai UAS baru   : "))

            self.mahasiswa[nama]["tugas"] = tugas
            self.mahasiswa[nama]["uts"] = uts
            self.mahasiswa[nama]["uas"] = uas

            print(f"Data '{nama}' berhasil diperbarui!\n")
        else:
            print(f"Data '{nama}' tidak ditemukan!\n")


# ==========================
# PROGRAM UTAMA
# ==========================

dm = DaftarMahasiswa()

while True:
    print("""
=== MENU PILIHAN ===
1. Tambah Data
2. Tampilkan Data
3. Ubah Data
4. Hapus Data
5. Keluar
""")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        dm.tambah()
    elif pilihan == "2":
        dm.tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama yang akan diubah: ")
        dm.ubah(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama yang akan dihapus: ")
        dm.hapus(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid! Silakan coba lagi.\n")
