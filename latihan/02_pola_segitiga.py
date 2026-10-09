# Peran Loop Luar: Mengatur jumlah baris dari 1 sampai n
# Peran Loop Dalam: Mengatur jumlah bintang yang dicetak pada baris ke-i

n = int(input("n: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # Pindah ke baris baru setelah loop dalam selesai