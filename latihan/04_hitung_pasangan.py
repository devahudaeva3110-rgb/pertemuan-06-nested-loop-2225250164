# Peran Loop Luar: Mengatur baris i dari 1 sampai n
# Peran Loop Dalam: Mengatur kolom j dari 1 sampai n
# Kondisi: Menyaring pasangan yang hasil penjumlahannya <= n

n = int(input("n: "))
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i + j <= n:
            count += 1

print(f"Banyak pasangan = {count}")