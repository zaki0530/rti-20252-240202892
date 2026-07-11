# Rencana Penelitian: Peningkatan Akurasi Sistem Rekomendasi Pariwisata Semarang Menggunakan Context-Aware Collaborative Filtering

## 1. Ringkasan

| Item | Keterangan |
|---|---|
| **Judul** | Peningkatan Akurasi Sistem Rekomendasi Pariwisata Semarang Menggunakan Algoritma Context-Aware Collaborative Filtering |
| **Peneliti** | Kayla Putri Arsonisr (NIM: 240202837) — Teknik Informatika 4IKRA |
| **Target Publikasi** | Jurnal RESTI (Sinta 2) atau Jurnal JTIIK (Sinta 2) |
| **Stack Teknologi** | Python, NumPy, Pandas, Scikit-learn, Matplotlib, Jupyter Notebook |
| **Masalah** | Sistem rekomendasi CF standar mengabaikan konteks geografis, menghasilkan rekomendasi destinasi yang terpisah puluhan kilometer (tidak rasional untuk rute wisata harian) |
| **Solusi** | Algoritma Context-Aware Collaborative Filtering dengan integrasi filter spasial berbasis formula Haversine untuk mempertimbangkan kedekatan geografis destinasi |
| **Dataset** | 4.362 ulasan riil destinasi wisata Semarang dari Google Maps (0 missing values) |
| **Metode Evaluasi** | 5-Fold Stratified Cross Validation dengan metrik Mean Absolute Error (MAE) |
| **Target Hasil** | Penurunan MAE minimal 2% dari baseline (target MAE < 0.665) |

---

## 2. Alur Kerja (Roadmap)

Setiap tahap penelitian didokumentasikan dalam file terpisah untuk tracking progres detail:

### Checklist Tahapan

- [x] **Tahap 1** — [Perancangan Arsitektur Context-Aware CF](tahap-1-perancangan-arsitektur.md) — *Selesai (2026-02-10)*
  - Desain arsitektur algoritma Context-Aware CF dengan filter spasial
  - Penentuan parameter konfigurasi (k neighbors, threshold geografis, penalty weight)
  - Dokumentasi arsitektur teknis dan alur algoritma

- [x] **Tahap 2** — [Implementasi Algoritma Baseline dan Context-Aware CF](tahap-2-implementasi-algoritma.md) — *Selesai (2026-03-05)*
  - Implementasi Collaborative Filtering standar sebagai baseline
  - Implementasi Context-Aware CF dengan filter Haversine
  - Pengembangan modul preprocessing, evaluasi, dan utilitas
  - Unit testing untuk validasi implementasi

- [x] **Tahap 3** — [Eksperimen K-Fold Cross Validation](tahap-3-eksperimen-validasi.md) — *Selesai (2026-03-20)*
  - Setup protokol 5-Fold Stratified Cross Validation
  - Eksekusi eksperimen pada dataset 4.362 ulasan
  - Isolasi data leakage dan validasi konsistensi hasil
  - Logging hasil eksperimen per fold

- [x] **Tahap 4** — [Analisis Hasil dan Evaluasi Metrik](tahap-4-analisis-hasil.md) — *Selesai (2026-04-10)*
  - Perhitungan MAE untuk setiap fold (Baseline vs Context-Aware CF)
  - Uji signifikansi statistik menggunakan paired t-test
  - Analisis distribusi geografis rekomendasi
  - Visualisasi perbandingan performa (bar chart, line plot, heatmap)

- [x] **Tahap 5** — [Dokumentasi Manuskrip dan Laporan](tahap-5-dokumentasi-paper.md) — *Selesai (2026-05-15)*
  - Penyusunan draf manuskrip jurnal sesuai template target
  - Penyusunan laporan penelitian komprehensif
  - Interpretasi hasil untuk konteks akademik
  - Persiapan submission ke jurnal target

---

## 3. Hasil Akhir Penelitian

### Metrik Akurasi (Achieved)

| Metrik | Baseline CF | Context-Aware CF | Improvement | Status Target |
|---|---|---|---|---|
| **MAE** | 0.672 | 0.651 | ↓ 3.13% | ✅ Target tercapai (< 0.665) |
| RMSE | 0.884 | 0.856 | ↓ 3.17% | — |
| Precision@10 | 0.698 | 0.721 | ↑ 3.29% | — |

### Metrik Geografis (Achieved)

| Metrik | Baseline CF | Context-Aware CF | Improvement |
|---|---|---|---|
| Rata-rata jarak antar destinasi | 22.3 km | 8.7 km | ↓ 61.0% |
| % rekomendasi dalam radius 10 km | 32.1% | 78.4% | ↑ 144.2% |

### Validasi Statistik

- **Paired t-test:** t = 12.457, p < 0.001 (signifikan pada α = 0.05)
- **Kesimpulan:** Hipotesis H₁ terbukti — Context-Aware CF menghasilkan MAE signifikan lebih rendah dibanding Baseline

---

## 4. Keputusan Teknis Utama

### 4.1 Algoritma dan Parameter

| Aspek | Keputusan | Justifikasi |
|---|---|---|
| **Baseline** | User-based CF dengan cosine similarity | Standar dalam literatur, mudah direplikasi |
| **Similarity metric** | Cosine similarity | Robust untuk sparse matrix, interpretable |
| **k neighbors** | 50 | Keseimbangan coverage dan akurasi |
| **Filter spasial** | Post-filtering dengan Haversine | Modular, tidak mengubah core CF |
| **Threshold geografis** | 15 km | Jarak maksimal rute wisata harian Semarang |
| **Penalty weight** | 0.1 per km | Tuning empiris berbasis data |

### 4.2 Dataset dan Preprocessing

| Aspek | Keputusan | Justifikasi |
|---|---|---|
| **Sumber data** | Google Maps API (4.362 ulasan Semarang) | Data riil, representative, berskala besar |
| **Missing values** | 0 (validated) | Kualitas data terjamin |
| **Normalisasi** | Rating ke skala 0-1 | Standar untuk perhitungan similarity |
| **Stratified splitting** | Ya, berdasarkan kategori rating | Distribusi rating seimbang antar fold |

### 4.3 Protokol Eksperimen

| Aspek | Keputusan | Justifikasi |
|---|---|---|
| **Metode validasi** | 5-Fold Stratified Cross Validation | Mencegah data leakage, robust estimation |
| **Metrik evaluasi** | MAE (primary), RMSE, Precision@K | MAE interpretable untuk rating prediction |
| **Uji statistik** | Paired t-test | Validasi signifikansi perbedaan MAE |
| **Random seed** | 42 (fixed) | Reproducibility |

---

## 5. Kontribusi Penelitian

### 5.1 Kontribusi Metodologis

1. **Protokol K-Fold yang ketat** untuk mencegah data leakage pada eksperimen sistem rekomendasi context-aware
2. **Framework evaluasi komprehensif** yang mengukur akurasi prediksi (MAE) dan rasionalitas geografis (average distance)

### 5.2 Kontribusi Praktis

1. **Peningkatan akurasi prediksi rating** sebesar 3.13% (dari MAE 0.672 ke 0.651)
2. **Peningkatan rasionalitas rute wisata** dengan penurunan rata-rata jarak geografis 61% (dari 22.3 km ke 8.7 km)
3. **Validasi efektivitas filter spasial** pada dataset riil berskala besar (>4.000 ulasan)

### 5.3 Kontribusi Teoritis

1. **Validasi empiris** dampak integrasi konteks geografis pada akurasi CF dalam domain pariwisata
2. **Penelitian pertama** yang menggunakan dataset Google Maps Semarang berskala besar untuk evaluasi Context-Aware CF

---

## 6. Keterbatasan dan Penelitian Lanjutan

### Keterbatasan Penelitian

1. Cakupan geografis terbatas pada wilayah Semarang (generalisasi ke kota lain perlu validasi)
2. Konteks yang dipertimbangkan hanya spasial (belum temporal, cuaca, atau sosial)
3. Threshold geografis ditetapkan secara empiris (belum adaptive berbasis clustering)
4. Evaluasi offline (belum user study atau A/B testing real-world)

### Penelitian Lanjutan

1. **Ekspansi Multi-City:** Validasi algoritma pada multiple cities dengan karakteristik geografis berbeda (kota pesisir vs pegunungan vs urban)
2. **Integrasi Multi-Context:** Tambah konteks temporal (seasonality, weekend/weekday) dan social (group size, age demographic)
3. **Adaptive Threshold:** Implementasi clustering destinasi untuk threshold geografis adaptif per cluster
4. **Real-World Deployment:** Implementasi sistem rekomendasi real-time dan evaluasi melalui user study atau A/B testing
5. **Hybrid Approach:** Kombinasi Context-Aware CF dengan Content-Based Filtering untuk handle cold-start problem

---

## 7. Timeline Pelaksanaan (Actual)

| Periode | Tahap | Status |
|---|---|---|
| 15 Jan - 10 Feb 2026 | Tahap 1: Perancangan Arsitektur | ✅ Selesai |
| 11 Feb - 05 Mar 2026 | Tahap 2: Implementasi Algoritma | ✅ Selesai |
| 06 Mar - 20 Mar 2026 | Tahap 3: Eksperimen K-Fold | ✅ Selesai |
| 21 Mar - 10 Apr 2026 | Tahap 4: Analisis Hasil | ✅ Selesai |
| 11 Apr - 15 May 2026 | Tahap 5: Dokumentasi Paper | ✅ Selesai |

**Total Durasi:** 4 bulan (sesuai rencana)

---

## 8. Catatan

Dokumen ini adalah indeks utama penelitian. Detail teknis, keputusan desain, dan hasil eksperimen masing-masing tahap dicatat pada file `tahap-N-*.md` terkait dan diperbarui seiring progres pengerjaan.

Seluruh hasil eksperimen telah divalidasi dan terbukti reproducible dengan random seed yang konsisten (seed = 42).
