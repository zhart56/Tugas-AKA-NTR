# Analisis Kompleksitas Algoritma: Konversi Desimal ke Heksadesimal

**Tugas Besar Analisis Kompleksitas Algoritma (AKA)** **Kelompok Narita Top Road** **Telkom University**

Repositori ini berisi implementasi kode dan laporan analisis perbandingan antara algoritma **Iteratif** dan **Rekursif** untuk mengonversi bilangan desimal ke heksadesimal. Proyek ini bertujuan untuk membuktikan kompleksitas waktu $O(\log n)$ dan membandingkan performa *running time* (empiris) menggunakan Python.

---

## 👥 Anggota Kelompok

| Nama | NIM | Peran |
| :--- | :--- | :--- |
| **Pascal Zaidane A.** | 103012400033 | Developer & Analyst |
| **Muhammad Shaquille Shah Alam Murtopo** | 103012400225 | Developer & Analyst |
| **Mas Ace Ardra Zeva Winata** | 103012400300 | Developer & Analyst |

---

## 🚀 Fitur & Algoritma

Proyek ini mencakup dua pendekatan algoritma utama:

### 1. Pendekatan Iteratif
Menggunakan perulangan (`while loop`) untuk membagi bilangan desimal dengan 16 hingga habis.
- **Kelebihan:** Aman dari *Stack Overflow* untuk input sangat besar.
- **Kekurangan:** Di Python, manipulasi string berulang dalam loop bisa memakan memori lebih banyak.

### 2. Pendekatan Rekursif
Menggunakan pemanggilan fungsi diri sendiri (*self-calling function*) untuk memecah masalah menjadi sub-masalah yang lebih kecil.
- **Kelebihan:** Kode lebih ringkas dan elegan.
- **Kekurangan:** Terbatas oleh *Recursion Depth Limit* pada Python.

---

## 📊 Hasil Analisis

Berdasarkan pengujian dengan input $N$ dari $10^0$ hingga $10^4$:

1.  **Kompleksitas Waktu (Teoretis):** Kedua algoritma memiliki kompleksitas **Logaritmik $O(\log n)$**.
2.  **Performa (Empiris):**
    * Algoritma **Rekursif** terbukti sedikit lebih cepat atau setara dengan Iteratif dalam lingkungan pengujian kami.
    * Hal ini disebabkan oleh efisiensi penanganan memori stack dibandingkan biaya *string concatenation* berulang pada pendekatan iteratif di Python.

![Grafik Perbandingan](https://via.placeholder.com/800x400?text=Masukkan+Link+Gambar+Grafik+Anda+Di+Sini)
*(Ganti link placeholder di atas dengan link gambar grafik dari laporan Anda)*

---

## ⚙️ Persiapan Lingkungan (Installation & Setup)

Sebelum menjalankan program, disarankan untuk menggunakan **Virtual Environment** agar dependensi proyek tidak tercampur dengan sistem global.

### 1. Buat Virtual Environment
Buka terminal/CMD di folder proyek, lalu jalankan perintah berikut:

```bash
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

### 2. Aktifkan Virtual Environment
Setelah berhasil dibuat, aktifkan lingkungan tersebut:

```bash
# Windows (Command Prompt)
venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
```

### 3. Instal Dependensi
Proyek ini memerlukan library untuk visualisasi grafik (Matplotlib). Instal dengan perintah:
```bash
pip install matplotlib
```

---  


## 🛠️ Cara Menjalankan Program

Pastikan Anda telah menginstal **Python 3.x**.

1.  **Clone Repositori**
    ```bash
    git clone [https://github.com/username-anda/repo-name.git](https://github.com/username-anda/repo-name.git)
    cd repo-name
    ```

2.  **Jalankan Script**
    Anda bisa menjalankan file utama untuk melihat hasil konversi dan waktu eksekusi:
    ```bash
    python main.py
    ```

### Contoh Penggunaan Kode
```python
# Import fungsi
from converter import decimal_to_hex_iterative, decimal_to_hex_recursive

# Test Input
n = 10000

# Iteratif
print(decimal_to_hex_iterative(n)) # Output: 2710

# Rekursif
print(decimal_to_hex_recursive(n)) # Output: 2710
