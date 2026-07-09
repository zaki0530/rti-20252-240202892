# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   |          |      |     |        |     |     |   |

2. Uji Hipotesis:
   Uji yang digunakan  : ____________________
   Justifikasi          : ____________________
   Hasil: p = ____, effect size (d/r/η²) = ____
   CI 95%               : [____, ____]

3. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak

4. Interpretasi:
   Hubungan ke RQ       : ____________________
   Practical significance: ____________________
   Perbandingan literatur: ____________________

5. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   |       |         |        |          |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : ____________________
   Boundary condition   : ____________________
   Insight              : ____________________
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 (Prototipe SRUPUT vs Aplikasi Kopi Reman) |
| Apakah data berpasangan (paired)? | Ya - responden yang sama menggunakan kedua aplikasi dalam urutan random |
| Apakah distribusi normal? (uji normalitas) | Perlu diuji dengan Shapiro-Wilk test pada data time on task (detik) dan SUS score (0-100) |
| **Uji yang dipilih:** | **Jika normal:** Paired t-test untuk kedua metrik (time on task & SUS)<br>**Jika tidak normal:** Wilcoxon signed-rank test |
| **Justifikasi:** | Data paired karena within-subject design mengurangi variabilitas individual. Pilihan uji parametrik/non-parametrik tergantung hasil uji normalitas |

**Effect size yang akan dilaporkan:** [x] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data Hipotetis SRUPUT Research:**
| Aplikasi | Time on Task (mean ± std) | SUS Score (mean ± std) | n |
|----------|---------------------------|------------------------|---|
| SRUPUT | 45.2 ± 8.3 detik | 78.5 ± 12.1 | 25 |
| Kopi Reman | 52.7 ± 9.1 detik | 68.3 ± 14.7 | 25 |

Time on Task: p = 0.003, Cohen's d = 0.89, CI 95% = [2.1, 12.9]
SUS Score: p = 0.012, Cohen's d = 0.74, CI 95% = [2.3, 18.1]

| Aspek | Interpretasi |
|-------|-------------|
| Signifikansi statistik | Time on Task: p < 0.01 → sangat signifikan pada α=0.05<br>SUS Score: p < 0.05 → signifikan pada α=0.05 |
| Effect size | Time on Task: d=0.89 → large effect (>0.8)<br>SUS Score: d=0.74 → medium-to-large effect |
| Practical significance | Penghematan 7.5 detik per pemesanan bermakna praktis untuk mengurangi antrian. Peningkatan 10.2 poin SUS menunjukkan perbaikan usability yang substansial |
| Hubungan ke RQ | Kedua hipotesis terdukung: SRUPUT lebih cepat DAN lebih usable dibanding Kopi Reman |
| Perbandingan literatur | SUS score 78.5 masuk kategori "Good" (Nielsen baseline), peningkatan dari 68.3 yang masuk kategori "OK" |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario SRUPUT Failure Analysis:** Prototipe SRUPUT mendapat SUS score = 72.1, Kopi Reman = 74.3. p = 0.18 (tidak signifikan). Time on task tetap signifikan lebih cepat.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Bukan gagal total — hipotesis parsial terdukung (time on task) tapi tidak untuk usability. Ini temuan valid yang berkontribusi pada pemahaman trade-off efficiency vs satisfaction. |
| Kemungkinan penyebab? | SRUPUT lebih cepat karena shortcut UI, tapi mengorbankan intuitiveness. Users menyelesaikan tugas cepat tapi merasa kurang confident dengan proses yang "terlalu singkat". |
| Boundary condition? | Efek kecepatan SRUPUT hanya bermakna untuk power users yang familiar dengan e-commerce. Untuk first-time users, kecepatan tinggi justru menciptakan anxiety dan menurunkan confidence. |
| Insight yang bisa diambil? | Ada trade-off fundamental antara efficiency dan perceived usability. Rekomendasi: adaptive UI yang memberikan shortcut untuk experienced users dan guided flow untuk newcomers. |
| Apakah layak dilaporkan? Mengapa? | Ya — negative result untuk usability + boundary condition analysis adalah kontribusi riset HCI yang diakui komunitas. Mencegah desainer lain jatuh pada "speed trap" yang sama. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| External validity | Sample hanya mahasiswa IT | Generalisasi ke target market (umum) terbatas |
| Construct validity | SUS mungkin tidak capture cognitive load | Missing insight tentang mental effort |
| Statistical | Hanya 25 responden per grup | Power test rendah untuk mendeteksi small effect |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Failure dalam riset bukan kegagalan sebenarnya, melainkan temuan berharga yang mencegah peneliti lain mengulang jalan buntu yang sama. Dalam konteks SRUPUT, jika UI yang terlalu cepat mengorbankan usability, ini insight penting untuk desain aplikasi yang seimbang.
> 
> Failure analysis mengubah mindset dari "mencari validasi hipotesis" menjadi "memahami boundary condition suatu solusi". Hasil negatif + analisis mendalam seringkali lebih berkontribusi daripada hasil positif tanpa refleksi.
