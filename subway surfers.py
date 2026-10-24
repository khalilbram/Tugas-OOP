class KarakterSurfer:
    def __init__(self, nama):
        # TODO 1: Inisialisasi properties
        self.nama = nama
        self.skor = 0
        self.koin = 0
        self.is_running = True

    def berlari(self):
        # TODO 2: Membuat karakter mulai berlari
        print(f"{self.nama} mulai berlari. Karena {self.nama} dikejar oleh Sekuriti dan Sianjing")
        self.is_running = True

    def ambil_koin(self, jumlah):
        # TODO 3: Menambahkan jumlah koin
        self.koin += jumlah
        self.skor += jumlah
        print(f"{self.nama} mengambil {jumlah} koin. Total koin: {self.koin}")

    def tabrak_rintangan(self):
        # TODO 4: Menghentikan karakter
        self.is_running = False
        print(f"{self.nama} menabrak rintangan! Game Over. Kamu tertangkap oleh Sekuriti dan Sianjing.")

    def info_player(self):
        # TODO 5: Menampilkan status karakter
        print(f"Nama: {self.nama}")
        print(f"Skor: {self.skor}")
        print(f"Koin: {self.koin}")
        print(f"Status Berlari: {'Ya' if self.is_running else 'Tidak'}")


# --- PENGUJIAN OBJEK ---
player1 = KarakterSurfer("Bram")

player1.info_player()
player1.berlari()
player1.ambil_koin(80)
player1.ambil_koin(195)
player1.info_player()
player1.tabrak_rintangan()
player1.info_player()
