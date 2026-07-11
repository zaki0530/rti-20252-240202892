# 08-laporan — Laporan Penelitian

Folder ini berisi laporan penelitian komprehensif yang mendokumentasikan seluruh proses penelitian dari awal hingga akhir.

## Isi Folder

- **laporan-penelitian.md** — Laporan lengkap penelitian mencakup ringkasan eksekutif, metodologi per tahap, hasil, interpretasi, dan kesimpulan

## Struktur Laporan

Laporan disusun dengan struktur naratif yang komprehensif:

### 1. Ringkasan Eksekutif
- Overview masalah penelitian
- Solusi yang diajukan
- Hasil utama dan dampak praktis

### 2. Latar Belakang dan Motivasi
- Konteks sistem rekomendasi pariwisata
- Keterbatasan CF standar
- Urgensi integrasi konteks geografis

### 3. Tinjauan Pustaka
- Kajian literatur Collaborative Filtering
- Context-Aware Recommender Systems
- Research gap yang diisi penelitian ini

### 4. Metodologi Penelitian (Per Tahap)

**Tahap 1: Perancangan Arsitektur**
- Desain algoritma Context-Aware CF
- Arsitektur filter spasial Haversine
- Parameter konfigurasi

**Tahap 2: Implementasi Algoritma**
- Implementasi Baseline CF
- Implementasi Context-Aware CF
- Modul preprocessing dan evaluasi

**Tahap 3: Eksperimen K-Fold Validation**
- Protokol 5-Fold Cross Validation
- Stratified splitting untuk mencegah data leakage
- Eksekusi eksperimen pada dataset 4.362 ulasan

**Tahap 4: Analisis Hasil**
- Perhitungan MAE untuk setiap fold
- Uji signifikansi statistik (paired t-test)
- Analisis distribusi geografis rekomendasi
- Visualisasi perbandingan performa

**Tahap 5: Dokumentasi dan Publikasi**
- Penyusunan manuskrip jurnal
- Interpretasi hasil untuk konteks akademik
- Rekomendasi penelitian lanjutan

### 5. Hasil dan Pembahasan

**Hasil Utama:**
- MAE Baseline: 0.672 → Context-Aware CF: 0.651 (penurunan 3.13%, p < 0.001)
- Rata-rata jarak geografis: 22.3 km → 8.7 km (penurunan 61%)
- Precision@10: 0.698 → 0.721 (peningkatan 3.29%)

**Interpretasi:**
- Hipotesis H₁ terbukti secara signifikan
- Penurunan error 3.13% berdampak praktis pada akurasi prediksi
- Filter spasial efektif meningkatkan rasionalitas rekomendasi rute
- Konsistensi hasil across folds menunjukkan robustness algoritma

### 6. Kendala dan Solusi
- Kompleksitas komputasi perhitungan jarak → Optimasi dengan caching
- Penentuan threshold geografis optimal → Analisis empiris berbasis data wisata Semarang

### 7. Kesimpulan dan Kontribusi
- Validasi efektivitas Context-Aware CF dengan filter spasial
- Kontribusi metodologis: protokol K-Fold yang ketat
- Kontribusi praktis: rekomendasi rute wisata yang lebih rasional

### 8. Keterbatasan dan Penelitian Lanjutan

**Keterbatasan:**
- Cakupan geografis terbatas pada wilayah Semarang
- Belum mempertimbangkan konteks temporal (musim, hari libur)
- Threshold geografis ditetapkan secara empiris

**Penelitian Lanjutan:**
- Ekspansi ke multiple cities dengan karakteristik geografis berbeda
- Integrasi konteks temporal untuk seasonality analysis
- Adaptive threshold geografis berbasis clustering destinasi
- Implementasi real-time recommendation system

### 9. Referensi

## Catatan

Laporan ini berfungsi sebagai dokumentasi lengkap untuk keperluan:
- Submission akademik (tugas akhir / skripsi)
- Referensi internal untuk penelitian lanjutan
- Portfolio penelitian
