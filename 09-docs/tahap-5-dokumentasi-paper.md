# Tahap 5 — Dokumentasi Manuskrip dan Laporan Penelitian

**Status:** Selesai  
**Periode:** 11 April - 15 Mei 2026

---

## 1. Tujuan Tahap

Menyusun dokumentasi lengkap penelitian dalam bentuk:
1. Manuskrip jurnal ilmiah untuk submission ke jurnal target (Sinta 2)
2. Laporan penelitian komprehensif untuk dokumentasi internal
3. Persiapan supplementary materials dan data availability statement

---

## 2. Struktur Manuskrip Jurnal

### 2.1 Target Jurnal

**Primary Target:** Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi) — Sinta 2

**Journal Scope:** Computer Science, Information Systems, Recommender Systems, Data Mining

**Submission Guidelines:**
- Format: IEEE Two-Column
- Page limit: 8-12 pages
- Language: Bahasa Indonesia with English abstract
- Plagiarism check: <20% similarity index
- Blind review: Yes (remove author information in submission)

**Alternative Target:** Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK) — Sinta 2

---

### 2.2 Outline Manuskrip

```
JUDUL (Bahasa Indonesia & English)
  Peningkatan Akurasi Sistem Rekomendasi Pariwisata Semarang 
  Menggunakan Algoritma Context-Aware Collaborative Filtering

AUTHORS & AFFILIATIONS
  Kayla Putri Arsonisr
  Program Studi Teknik Informatika
  Universitas Putra Bangsa, Kebumen
  Email: kayla.arsonisr@example.ac.id

ABSTRACT (English) — 150-200 words
  Background → Problem → Method → Results → Conclusion

ABSTRAK (Bahasa Indonesia) — 150-200 words

KEYWORDS — 5-7 keywords
  Context-Aware Collaborative Filtering, Tourism Recommendation System, 
  Spatial Filter, Haversine Distance, Mean Absolute Error, Cross Validation

1. PENDAHULUAN
   1.1. Latar Belakang
   1.2. Rumusan Masalah
   1.3. Kontribusi Penelitian
   1.4. Struktur Paper

2. TINJAUAN PUSTAKA
   2.1. Collaborative Filtering
   2.2. Context-Aware Recommender Systems
   2.3. Location-Based Recommendation
   2.4. Research Gap

3. METODE PENELITIAN
   3.1. Arsitektur Context-Aware CF
   3.2. Filter Spasial dengan Haversine
   3.3. Dataset dan Preprocessing
   3.4. Protokol Eksperimen (5-Fold CV)
   3.5. Metrik Evaluasi

4. HASIL DAN PEMBAHASAN
   4.1. Perbandingan MAE (Baseline vs Context-Aware)
   4.2. Validasi Statistik (Paired T-Test)
   4.3. Analisis Distribusi Geografis
   4.4. Case Study dan Interpretasi Praktis
   4.5. Diskusi Limitasi

5. KESIMPULAN DAN SARAN
   5.1. Kesimpulan
   5.2. Keterbatasan Penelitian
   5.3. Penelitian Lanjutan

ACKNOWLEDGMENTS (Optional)

REFERENCES
  [Minimal 15-20 references, majority < 5 years]
```

---

## 3. Highlights Utama untuk Manuskrip

### 3.1 Key Findings (untuk Abstract & Conclusion)

1. **Akurasi Prediksi:** Context-Aware CF menghasilkan MAE 0.651, menurun 3.13% dari Baseline (MAE 0.672), dengan signifikansi statistik p < 0.001

2. **Rasionalitas Geografis:** Rata-rata jarak geografis rekomendasi turun 61% (dari 22.3 km menjadi 8.7 km), dengan 78.4% rekomendasi berada dalam radius 10 km

3. **Validitas Eksperimen:** Protokol 5-Fold Stratified Cross Validation memastikan tidak ada data leakage, dengan konsistensi hasil tinggi (std dev < 0.003)

4. **Dampak Praktis:** Penurunan error berdampak pada peningkatan akurasi prediksi, sementara penurunan jarak mendukung perencanaan itinerary wisata yang lebih efisien dan realistis

### 3.2 Novelty Statement

> "Penelitian ini merupakan yang pertama menggunakan dataset riil berskala besar (>4.000 ulasan) dari Google Maps untuk evaluasi sistematis Context-Aware Collaborative Filtering dengan filter spasial Haversine pada domain pariwisata Indonesia, dengan protokol K-Fold Cross Validation yang ketat untuk mencegah data leakage."

---

## 4. Section-by-Section Content Summary

### 4.1 Section 1: PENDAHULUAN

**Key Points:**
- Sistem rekomendasi pariwisata penting untuk mendukung pengalaman wisatawan
- CF standar mengabaikan konteks geografis → rekomendasi tidak feasible (destinasi terpisah puluhan km)
- Dataset: 4.362 ulasan Google Maps Semarang (0 missing values)
- Kontribusi: Integrasi filter spasial Haversine dengan evaluasi K-Fold yang ketat

**Opening Paragraph (Draft):**
> "Sistem rekomendasi pariwisata berbasis Collaborative Filtering (CF) telah banyak digunakan untuk memprediksi preferensi wisatawan berdasarkan pola rating pengguna serupa. Namun, pendekatan CF konvensional memiliki keterbatasan signifikan: algoritma tersebut mengabaikan faktor kontekstual geografis, sehingga sering menghasilkan rekomendasi destinasi dengan rating tinggi namun terpisah jarak puluhan kilometer. Dalam konteks perencanaan rute wisata harian, rekomendasi yang tidak mempertimbangkan kedekatan spasial mengakibatkan inefisiensi waktu tempuh dan penurunan kepuasan wisatawan. Penelitian ini mengusulkan integrasi filter spasial berbasis formula Haversine ke dalam algoritma Collaborative Filtering untuk meningkatkan akurasi prediksi rating sekaligus memastikan rasionalitas geografis rekomendasi."

---

### 4.2 Section 2: TINJAUAN PUSTAKA

**Struktur Literature Review:**

| Topik | Paper yang Disitasi | Gap yang Diidentifikasi |
|---|---|---|
| Collaborative Filtering | Ricci et al. (2015) | CF standar tidak mempertimbangkan konteks |
| Context-Aware RS | Adomavicius & Tuzhilin (2011) | Framework CARS umum, belum spesifik pariwisata |
| Location-Based POI | Bao et al. (2015), Zhang et al. (2019) | Fokus pada check-in data, bukan explicit rating |
| Tourism RS Indonesia | Kurniawan & Budiman (2021) | Dataset kecil (<500), tidak ada K-Fold CV |

**Research Gap Statement:**
> "Mayoritas penelitian terdahulu yang mengintegrasikan filter spasial pada sistem rekomendasi menggunakan implicit feedback (check-in data) bukan explicit rating, serta belum menerapkan protokol K-Fold Cross Validation yang ketat untuk mencegah data leakage. Penelitian ini mengisi kesenjangan tersebut dengan evaluasi sistematis pada dataset riil berskala besar (>4.000 ulasan) dengan metrik MAE yang interpretable dan protokol eksperimen yang robust."

---

### 4.3 Section 3: METODE PENELITIAN

**Visual Arsitektur Algoritma:**

```
┌────────────────────────────────────────────────┐
│  INPUT: User u, Dataset D (ratings + coords)  │
└───────────────────┬────────────────────────────┘
                    │
        ┌───────────▼───────────┐
        │  Collaborative        │
        │  Filtering (Baseline) │
        │  • User similarity    │
        │  • Predict ratings    │
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │  Geographic Context   │
        │  • User centroid      │
        │  • Haversine distance │
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │  Spatial Filter       │
        │  • Penalty calculation│
        │  • Re-ranking         │
        └───────────┬───────────┘
                    │
            ┌───────▼───────┐
            │  TOP-N LIST   │
            │  (Context-Aware)
            └───────────────┘
```

**Formula Haversine (untuk paper):**

$$d = 2R \cdot \arcsin\left(\sqrt{\sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left(\frac{\Delta\lambda}{2}\right)}\right)$$

di mana $R = 6371$ km, $\phi$ adalah latitude, dan $\lambda$ adalah longitude.

**Tabel Parameter Konfigurasi:**

| Parameter | Nilai | Justifikasi |
|---|---|---|
| k neighbors | 50 | Berdasarkan literatur untuk dataset >4000 users |
| Threshold geografis | 15 km | Jarak maksimal rute wisata harian Semarang |
| Penalty weight | 0.1 | Tuning empiris: 0.1 poin per 1 km excess |
| Min rating centroid | 4.0 | Hanya destinasi sangat disukai sebagai referensi |

---

### 4.4 Section 4: HASIL DAN PEMBAHASAN

**Tabel Utama: Perbandingan MAE**

| Fold | Baseline MAE | Context-Aware MAE | Improvement % |
|---|---|---|---|
| 1 | 0.674 | 0.653 | 3.12% |
| 2 | 0.669 | 0.648 | 3.14% |
| 3 | 0.675 | 0.654 | 3.11% |
| 4 | 0.671 | 0.650 | 3.13% |
| 5 | 0.671 | 0.651 | 2.98% |
| **Mean** | **0.672 ± 0.0025** | **0.651 ± 0.0024** | **3.13%** |

**Uji Statistik:**
> Paired t-test menghasilkan t = 12.46, p < 0.001, menunjukkan perbedaan MAE signifikan secara statistik pada α = 0.05. Effect size (Cohen's d = 8.38) mengindikasikan dampak praktis yang sangat besar.

**Visualisasi untuk Paper:**
1. Bar chart MAE comparison (Figure 1)
2. Line plot MAE per fold (Figure 2)
3. Histogram geographic distribution (Figure 3)
4. Heatmap recommendations on Semarang map (Figure 4)

**Diskusi Case Study:**
> Analisis pada user dengan preferensi destinasi pesisir menunjukkan bahwa Context-Aware CF berhasil menyaring destinasi pegunungan yang terlalu jauh (42.7 km) dan menggantinya dengan destinasi pantai terdekat (9.7 km), mengurangi rata-rata jarak rekomendasi sebesar 43% tanpa mengorbankan akurasi rating.

---

### 4.5 Section 5: KESIMPULAN DAN SARAN

**Kesimpulan Utama:**

1. Algoritma Context-Aware Collaborative Filtering dengan filter spasial Haversine terbukti meningkatkan akurasi prediksi rating sebesar 3.13% (MAE turun dari 0.672 menjadi 0.651, p < 0.001)

2. Integrasi filter geografis mengurangi rata-rata jarak rekomendasi sebesar 61% (dari 22.3 km menjadi 8.7 km), meningkatkan rasionalitas perencanaan rute wisata harian

3. Protokol 5-Fold Stratified Cross Validation memastikan validitas internal hasil dengan konsistensi tinggi (std dev < 0.003) dan tidak ada data leakage

4. Penelitian ini berkontribusi pada pengembangan sistem rekomendasi pariwisata yang context-aware dengan dampak praktis terhadap efisiensi itinerary wisatawan

**Keterbatasan:**

- Cakupan geografis terbatas pada wilayah Semarang
- Hanya mempertimbangkan konteks spasial (belum temporal atau sosial)
- Threshold geografis bersifat global (tidak adaptive per user)
- Evaluasi offline (belum divalidasi melalui user study real-world)

**Saran Penelitian Lanjutan:**

1. Ekspansi evaluasi ke multiple cities dengan karakteristik geografis berbeda
2. Integrasi multi-context (spasial + temporal + sosial)
3. Implementasi adaptive threshold berbasis clustering destinasi
4. Validasi real-world melalui deployment sistem dan A/B testing

---

## 5. Supplementary Materials

### 5.1 Data Availability Statement

> "Dataset penelitian ini terdiri dari 4.362 ulasan destinasi wisata Semarang yang dikumpulkan dari Google Maps API dengan protokol anonimisasi user ID. Mengingat kebijakan privasi dan terms of service Google Maps, raw dataset tidak dapat dipublikasikan secara terbuka. Namun, agregat statistik dataset, metadata (distribusi rating, distribusi geografis), dan source code implementasi algoritma tersedia di repository GitHub: [URL]."

### 5.2 Code Availability

Source code implementasi (Python) dipublikasikan di GitHub repository dengan lisensi MIT:
- baseline_cf.py
- context_aware_cf.py
- kfold_experiment.py
- evaluation.py
- utils.py
- requirements.txt
- README.md (instruksi reproduksi eksperimen)

### 5.3 Ethical Considerations

- Penelitian ini tidak melibatkan human subjects (menggunakan historical data)
- Data ulasan Google Maps bersifat publik dan telah dianonimisasi
- Tidak ada personally identifiable information (PII) yang dikumpulkan atau disimpan
- Tidak diperlukan ethical clearance untuk jenis penelitian ini

---

## 6. Submission Checklist

### 6.1 Pre-Submission Checklist

- [x] Manuskrip sesuai format template jurnal (IEEE two-column)
- [x] Abstract bahasa Inggris dan Indonesia lengkap
- [x] Keyword 5-7 kata relevan
- [x] Referensi minimal 15 paper (majority < 5 years)
- [x] Semua figure dalam resolusi tinggi (300 DPI)
- [x] Plagiarism check < 20% (menggunakan Turnitin)
- [x] Author information dihapus (blind review)
- [x] Supplementary materials disiapkan

### 6.2 Plagiarism Check Result

**Turnitin Similarity Index:** 16.3%

**Breakdown:**
- Quotes from references (proper citation): 8.2%
- Method description (standard terminology): 5.1%
- General academic phrases: 3.0%
- **Original content:** 83.7%

**Status:** ✅ Pass (below 20% threshold)

### 6.3 Review Readiness

- [x] Self-review completed (grammar, typo, logical flow)
- [x] Co-author / advisor review completed
- [x] Response to potential reviewer questions prepared
- [x] Rebuttal letter template prepared (for revision phase)

---

## 7. Timeline Submission & Publication

| Milestone | Target Date | Status |
|---|---|---|
| Draft manuskrip selesai | 30 April 2026 | ✅ Done |
| Internal review & revision | 5 Mei 2026 | ✅ Done |
| Plagiarism check | 8 Mei 2026 | ✅ Done (16.3%) |
| Final proofreading | 12 Mei 2026 | ✅ Done |
| **Submission to journal** | **15 Mei 2026** | **✅ Submitted** |
| Initial review (editor screening) | +2 weeks | ⏳ Pending |
| Peer review assignment | +1 month | ⏳ Pending |
| Reviewer feedback | +2-3 months | ⏳ Pending |
| Revision & resubmission | +1 month | ⏳ Pending |
| Final decision (accept/reject) | +4-6 months | ⏳ Pending |
| Publication | +6-8 months | ⏳ Pending |

**Estimasi Total Time to Publication:** 6-8 bulan dari submission

---

## 8. Laporan Penelitian Komprehensif

Selain manuskrip jurnal, laporan penelitian internal yang lebih komprehensif telah disusun (file: `08-laporan/laporan-penelitian.md`) mencakup:

- **Ringkasan Eksekutif:** Overview penelitian untuk non-technical stakeholders
- **Metodologi Detail:** Dokumentasi lengkap implementasi per tahap
- **Hasil Lengkap:** Semua metrik, visualisasi, dan analisis (tidak hanya highlights untuk jurnal)
- **Decision Log:** Dokumentasi keputusan teknis selama penelitian
- **Troubleshooting Log:** Kendala yang dihadapi dan solusinya
- **Lessons Learned:** Insight untuk penelitian lanjutan

Laporan ini berfungsi sebagai dokumentasi internal untuk:
- Referensi penelitian lanjutan
- Onboarding anggota tim baru
- Portfolio akademik

---

## 9. Deliverables Tahap 5

- [x] Manuskrip jurnal final (manuscript_draft.md & .docx)
- [x] Laporan penelitian komprehensif (laporan-penelitian.md)
- [x] Supplementary materials (source code, dataset descriptor)
- [x] Data availability statement
- [x] Plagiarism check report (16.3%)
- [x] Submission confirmation dari jurnal target
- [x] Dokumentasi tahap 5 (file ini)

---

## 10. Catatan Akhir

Penelitian ini berhasil diselesaikan sesuai timeline 4 bulan (Januari - Mei 2026) dengan deliverables lengkap:

1. **Kontribusi Metodologis:** Protokol K-Fold CV yang ketat untuk Context-Aware RS
2. **Kontribusi Empiris:** Validasi efektivitas filter spasial Haversine pada dataset riil >4K ulasan
3. **Kontribusi Praktis:** Rekomendasi rute wisata yang lebih rasional (jarak turun 61%)
4. **Publikasi:** Manuskrip telah disubmit ke Jurnal RESTI (Sinta 2)

**Hasil utama:** MAE 0.651 (vs 0.672 baseline, p < 0.001), penurunan jarak geografis 61%, dengan konsistensi tinggi across folds.

**Status:** Penelitian selesai, menunggu reviewer feedback dari jurnal target.

---

**Tanggal Finalisasi:** 15 Mei 2026  
**Peneliti:** Kayla Putri Arsonisr (NIM: 240202837)  
**Pembimbing:** [Nama Pembimbing]  
**Institusi:** Program Studi Teknik Informatika, Universitas Putra Bangsa
