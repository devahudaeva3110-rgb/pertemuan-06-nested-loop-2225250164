# Peran Loop Luar: Mengatur indeks i dari 1 sampai 3
# Peran Loop Dalam: Mengatur indeks j dari 1 sampai 4 untuk setiap nilai i
# Counter: Menghitung total seluruh pasangan yang terbentuk

count = 0
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")