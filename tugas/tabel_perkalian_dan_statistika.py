print("Tabel Perkalian dan Statistik")

# Validasi input n menggunakan while loop
n = int(input("n: "))
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Inisialisasi akumulator keseluruhan dan counter genap
total_semua = 0
count_genap = 0

# Nested Loop untuk tabel perkalian
for i in range(1, n + 1):
    total_baris = 0  # Reset akumulator per baris
    
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="") # Cetak hasil dengan format lebar 4 karakter
        
        total_baris += hasil
        total_semua += hasil
        
        # Hitung jika hasil merupakan bilangan genap
        if hasil % 2 == 0:
            count_genap += 1
            
    # Cetak total baris setelah kolom pada baris tersebut selesai dicetak
    print(f" | jumlah baris = {total_baris}")

# Tampilkan statistik akhir setelah kedua loop selesai
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")