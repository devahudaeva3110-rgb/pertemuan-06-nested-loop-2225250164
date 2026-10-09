# Peran Loop Luar: Mengatur baris i dari 1 sampai 4
# Peran Loop Dalam: Mengatur kolom j dari 1 sampai 3
# Akumulator: total_baris diinisialisasi di dalam loop luar agar direset ke 0 setiap baris baru

for i in range(1, 5):
    total_baris = 0
    for j in range(1, 4):
        total_baris += i * j
    print(f"Jumlah baris {i} = {total_baris}")