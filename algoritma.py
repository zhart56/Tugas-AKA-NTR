import gradio as gr
import time
import matplotlib.pyplot as plt
import sys

# Menambah batas rekursi untuk keamanan input sangat besar (opsional, karena log16 turunnya cepat)
sys.setrecursionlimit(2000)

# ==========================================
# 1. IMPLEMENTASI ALGORITMA
# ==========================================

HEX_CHARS = "0123456789ABCDEF"

def decimal_to_hex_iterative(n):
    """Mengubah desimal ke heksadesimal secara Iteratif"""
    if n == 0:
        return "0"
    
    result = ""
    num = n
    while num > 0:
        remainder = num % 16
        result = HEX_CHARS[remainder] + result
        num = num // 16
    return result

def decimal_to_hex_recursive(n):
    """Mengubah desimal ke heksadesimal secara Rekursif"""
    if n < 16:
        return HEX_CHARS[n]
    else:
        return decimal_to_hex_recursive(n // 16) + HEX_CHARS[n % 16]

# ==========================================
# 2. FUNGSI ANALISIS & BENCHMARK
# ==========================================

def run_analysis(input_number):
    try:
        n = int(input_number)
        if n < 0:
            return "Error: Masukkan bilangan positif", "Error", None, "Input tidak valid"
    except ValueError:
        return "Error: Masukkan angka bulat", "Error", None, "Input tidak valid"

    # --- 1. Cek Hasil Konversi ---
    result_iter = decimal_to_hex_iterative(n)
    result_rec = decimal_to_hex_recursive(n)

    # --- 2. Benchmarking (Sesuai syarat poin 4 PDF) ---
    # Kita akan menguji performa dengan berbagai ukuran input sampai angka yang diinput user
    # Jika input user kecil, kita buat default test case minimal sampai 10.000
    
    # Membuat variasi ukuran input (1, 10, 100, ..., 10000, dst)
    test_inputs = []
    current = 1
    limit = max(n, 10000) # Minimal tes sampai 10.000 agar grafik terlihat
    
    while current <= limit:
        test_inputs.append(current)
        current *= 10
    
    # Jika input user sangat besar dan tidak kelipatan 10, tambahkan ke test case
    if n not in test_inputs:
        test_inputs.append(n)
        test_inputs.sort()

    times_iter = []
    times_rec = []

    # Melakukan pengukuran waktu
    # Karena operasi ini sangat cepat, kita jalankan loop 1000x untuk akurasi (average case)
    loops = 1000 
    
    for val in test_inputs:
        # Ukur Iteratif
        start = time.perf_counter()
        for _ in range(loops):
            decimal_to_hex_iterative(val)
        end = time.perf_counter()
        times_iter.append((end - start) / loops) # Rata-rata per eksekusi

        # Ukur Rekursif
        start = time.perf_counter()
        for _ in range(loops):
            decimal_to_hex_recursive(val)
        end = time.perf_counter()
        times_rec.append((end - start) / loops)

    # --- 3. Membuat Grafik (Sesuai syarat poin 4 PDF) ---
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(test_inputs, times_iter, marker='o', label='Iteratif', color='blue')
    ax.plot(test_inputs, times_rec, marker='x', label='Rekursif', color='red')
    
    ax.set_title('Perbandingan Running Time: Iteratif vs Rekursif')
    ax.set_xlabel('Ukuran Input (Nilai Desimal)')
    ax.set_ylabel('Waktu Eksekusi (detik)')
    ax.set_xscale('log') # Menggunakan skala logaritmik agar grafik 1 vs 10000 terbaca jelas
    ax.grid(True, which="both", ls="-")
    ax.legend()
    
    # Analisis Singkat untuk ditampilkan
    analysis_text = (
        f"Analisis untuk Input N = {n}:\n"
        f"- Kompleksitas Waktu kedua algoritma adalah Logaritmik O(log n).\n"
        f"- Hal ini terlihat dari grafik yang cenderung landai meski input dikali 10.\n"
        f"- Rekursif biasanya sedikit lebih lambat karena overhead pemanggilan fungsi."
    )

    return result_iter, result_rec, fig, analysis_text

# ==========================================
# 3. ANTARMUKA GRADIO (UI)
# ==========================================

with gr.Blocks(title="Tugas Besar AKA - Konversi Desimal ke Hex") as demo:
    gr.Markdown("# Analisis Kompleksitas: Konversi Desimal ke Heksadesimal")
    gr.Markdown("Tugas Besar Analisis Kompleksitas Algoritma - Kelompok Narita Top Road")
    
    with gr.Row():
        input_num = gr.Number(label="Masukkan Bilangan Desimal (Contoh: 10000)", value=10000)
        btn = gr.Button("Hitung & Analisis", variant="primary")
    
    with gr.Row():
        out_iter = gr.Textbox(label="Hasil Iteratif")
        out_rec = gr.Textbox(label="Hasil Rekursif")
    
    with gr.Row():
        out_plot = gr.Plot(label="Grafik Perbandingan Running Time")
    
    with gr.Row():
        out_analysis = gr.Textbox(label="Analisis Singkat", lines=4)

    btn.click(fn=run_analysis, inputs=input_num, outputs=[out_iter, out_rec, out_plot, out_analysis])

if __name__ == "__main__":
    demo.launch()