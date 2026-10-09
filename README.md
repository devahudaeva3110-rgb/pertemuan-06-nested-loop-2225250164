# Pertemuan 06 Nested Loop Python

Nama: HUDAEVA
NIM: 2225250164
Kelas: 3E

## Tujuan
Menggunakan nested loop, pola, akumulasi, dan pencacahan.

## Cara Menjalankan
python3 tugas/tabel_perkalian_dan_statistik.py

## Algoritma Tugas 3
* **Loop Luar**: Mengontrol baris `i` dari 1 sampai `n`.
* **Loop Dalam**: Mengontrol kolom `j` dari 1 sampai `n`.
* **Akumulator (`total_baris`)**: Menyimpan jumlah nilai perkalian pada satu baris (direset setiap iterasi loop luar).
* **Akumulator (`total_semua`)**: Menyimpan akumulasi total seluruh nilai tabel.
* **Counter (`count_genap`)**: Menghitung berapa kali nilai hasil perkalian bersifat genap.

## Hasil Pengujian
* Input `n = 1` -> Total Semua = 1, Hasil Genap = 0 (Status: PASSED)
* Input `n = 2` -> Total Semua = 9, Hasil Genap = 3 (Status: PASSED)
* Input `n = 3` -> Total Semua = 36, Hasil Genap = 5 (Status: PASSED)

## Analisis Efisiensi
Badan loop dalam berjalan sebanyak \(n \times n\) atau \(n^2\) kali untuk input berupa bilangan bulat `n`.

## Refleksi
* **Refleksi Teknis**: `total_baris` harus direset di awal loop luar agar perhitungan jumlah baris berikutnya tidak menjumlahkan nilai dari baris sebelumnya. Sementara `total_semua` diletakkan di luar loop agar mencakup total keseluruhan nilai.
*