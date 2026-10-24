class Buku:
    def __init__(self, judul, penulis, tahun_terbit, stok):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.stok = stok

    def info_buku(self):
        print("--- INFORMASI BUKU ---")
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Stok: {self.stok}")
        print("----------------------")

    def pinjam_buku(self, jumlah, nama_peminjam):
        if jumlah > 0 and self.stok >= jumlah:
            self.stok -= jumlah
            print(f"Buku '{self.judul}' berhasil dipinjam oleh {nama_peminjam}.")
            print(f"Sisa stok: {self.stok}")
        else:
            print(f"Buku '{self.judul}' tidak bisa dipinjam.")
            print(f"Stok tersedia: {self.stok}")

    def kembalikan_buku(self, jumlah_dipinjam, jumlah_dikembalikan, nama_peminjam):
        if jumlah_dikembalikan <= 0 or jumlah_dikembalikan > jumlah_dipinjam:
            print("Jumlah buku yang dikembalikan tidak valid.")
        else:
            self.stok += jumlah_dikembalikan

            if jumlah_dikembalikan < jumlah_dipinjam:
                sisa_pinjam = jumlah_dipinjam - jumlah_dikembalikan
                print(f"{nama_peminjam} mengembalikan {jumlah_dikembalikan} buku '{self.judul}'.")
                print(f"Masih ada {sisa_pinjam} buku yang belum dikembalikan.")
            else:
                print(f"{nama_peminjam} sudah mengembalikan semua buku '{self.judul}'.")

            print(f"Stok tersedia: {self.stok}")

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.stok += jumlah
            print(f"Stok buku '{self.judul}' berhasil ditambahkan.")
            print(f"Stok sekarang: {self.stok}")
        else:
            print("Jumlah penambahan stok harus lebih dari 0.")


# Uji coba
buku1 = Buku("Arjuna", "Sang Dewa", 2005, 19)
buku2 = Buku("10 Things I Hate About You", "David Levithan", 1999, 7)

buku1.info_buku()
buku1.pinjam_buku(2, "Andy")
buku1.pinjam_buku(4, "Supri")
buku1.kembalikan_buku(2, 1, "Andy")
buku1.tambah_stok(3)

buku2.info_buku()
buku2.pinjam_buku(3, "Budi")
buku2.pinjam_buku(5, "Sinta")
buku2.kembalikan_buku(3, 3, "Budi")
buku2.tambah_stok(5)
