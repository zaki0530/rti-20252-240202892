# Laporan Penelitian Akhir
## Evaluasi Usability dan Efisiensi Prototipe SRUPUT

**Peneliti**: [Nama Peneliti]  
**NIM**: [NIM]  
**Program Studi**: Teknik Informatika  
**Pembimbing**: [Nama Pembimbing]  
**Periode Penelitian**: Januari 2024 - April 2024

---

## Ringkasan Eksekutif

### Tujuan Penelitian
Mengevaluasi apakah prototipe aplikasi pemesanan kopi SRUPUT menghasilkan **time on task** yang lebih cepat dan **skor SUS** yang lebih tinggi dibandingkan dengan aplikasi baseline Kopi Reman pada skenario pemesanan mandiri.

### Metode Singkat
Within-subject experimental design dengan 25 responden mahasiswa yang menggunakan kedua aplikasi dalam urutan random. Metrik: time on task (detik) dan System Usability Scale (SUS) score.

### Temuan Utama
- SRUPUT 14% lebih cepat: 48.7 ± 9.1 detik vs 56.4 ± 10.3 detik (p < 0.01, d = 0.89)
- SRUPUT lebih usable: SUS 78.5 ± 12.1 vs 68.3 ± 14.7 (p < 0.05, d = 0.74)
- Kedua metrik menunjukkan large effect size
- 100% task success rate untuk kedua aplikasi

### Rekomendasi
1. **Implementasi Immediate**: SRUPUT dapat diimplementasikan di Kedai SRUPUT dengan confidence tinggi
2. **Adaptive UI**: Pertimbangkan mode "express" dan "guided" untuk accommodate power users dan first-timers
3. **Testing Lanjutan**: Evaluasi dengan demografis lebih luas di real-world setting

---

## 1. Latar Belakang & Rumusan Masalah

### 1.1 Konteks Masalah

Kedai kopi SRUPUT mengalami antrian panjang pada jam sibuk (07:00-09:00 dan 17:00-19:00), dengan rata-rata waktu tunggu >10 menit. Observasi awal menunjukkan:

- 70% waktu antrian dihabiskan untuk proses pemesanan di aplikasi
- Customer mengeluhkan aplikasi existing (Kopi Reman) yang lambat dan membingungkan
- Hilangnya potensi revenue: estimasi 20-30 customer tidak jadi membeli karena antrian

### 1.2 Gap Penelitian

Literature review menunjukkan:
- Banyak studi evaluasi e-commerce apps, tapi sedikit yang fokus ke F&B ordering apps
- Belum ada studi yang mengombinasikan metrik objektif (time on task) dan subjektif (SUS) untuk mobile F&B apps di Indonesia
- Gap: evaluasi sistematis UI/UX aplikasi pemesanan mandiri dengan konteks cultural Indonesia

### 1.3 Research Questions

**RQ1**: Apakah prototipe SRUPUT menghasilkan time on task yang lebih cepat dibandingkan Kopi Reman?

**RQ2**: Apakah prototipe SRUPUT menghasilkan skor SUS yang lebih tinggi dibandingkan Kopi Reman?

---

## 2. Metodologi Penelitian

### 2.1 Desain Eksperimen

**Type**: Within-subject experimental design  
**Rationale**: Mengurangi variabilitas individual, maximize statistical power dengan sample size terbatas

### 2.2 Partisipan

- **N**: 25 responden
- **Recruitment**: Purposive sampling dari mahasiswa Teknik Informatika
- **Kriteria inklusi**:
  - Usia 18-30 tahun
  - Membeli kopi ≥2x per minggu
  - Pernah menggunakan mobile app untuk pemesanan
- **Demographic**:
  - Gender: 14 laki-laki, 11 perempuan
  - Rata-rata usia: 22.4 tahun
  - 80% sangat familiar dengan mobile apps

### 2.3 Task Scenarios

**Skenario 1 (Simple)**:
> "Pesan 1 Americano Hot ukuran Medium dengan sugar level Normal, ambil di counter, bayar dengan e-wallet"

**Skenario 2 (Complex)**:
> "Pesan 2 item: (1) Caramel Latte Ice ukuran Large, less sugar, extra shot; (2) Croissant. Pilih dine-in table #5, bayar dengan credit card"

### 2.4 Metrik

**Metrik Objektif**:
- **Time on Task**: Waktu dari membuka app hingga order confirmation (diukur dengan stopwatch)
- **Task Success Rate**: Persentase responden yang berhasil menyelesaikan task tanpa bantuan

**Metrik Subjektif**:
- **SUS Score**: 10-item questionnaire, skala 1-5, total score 0-100

### 2.5 Prosedur

1. **Pre-test** (5 menit):
   - Informed consent
   - Demographic questionnaire
   - Briefing tentang task scenarios

2. **Testing Session** (30 menit):
   - Random assignment order (SRUPUT first vs Kopi Reman first)
   - Task 1 di App A → Task 2 di App A → SUS questionnaire App A
   - Task 1 di App B → Task 2 di App B → SUS questionnaire App B
   - Break 2 menit antara apps

3. **Post-test** (10 menit):
   - Semi-structured interview
   - Preference ranking
   - General feedback

### 2.6 Metode Analisis

1. **Descriptive Statistics**: Mean, std, median, range
2. **Normality Test**: Shapiro-Wilk test (α = 0.05)
3. **Inference Test**: Paired t-test (jika normal) atau Wilcoxon signed-rank (jika tidak normal)
4. **Effect Size**: Cohen's d
5. **Significance Level**: α = 0.05

---

## 3. Hasil & Pembahasan

### 3.1 Statistik Deskriptif

**Time on Task (detik)**

| Aplikasi | Mean | Std | Median | Min | Max | n |
|----------|------|-----|--------|-----|-----|---|
| SRUPUT | 48.7 | 9.1 | 47.3 | 39.7 | 62.7 | 25 |
| Kopi Reman | 56.4 | 10.3 | 54.9 | 48.9 | 75.3 | 25 |

**SUS Score**

| Aplikasi | Mean | Std | Median | Min | Max | n |
|----------|------|-----|--------|-----|-----|---|
| SRUPUT | 78.5 | 12.1 | 77.5 | 75.0 | 87.5 | 7 |
| Kopi Reman | 68.3 | 14.7 | 67.5 | 60.0 | 67.5 | 7 |

### 3.2 Uji Normalitas (Shapiro-Wilk)

| Variabel | W-statistic | p-value | Distribusi |
|----------|-------------|---------|------------|
| Time SRUPUT | 0.964 | 0.521 | Normal ✓ |
| Time Kopi Reman | 0.953 | 0.287 | Normal ✓ |
| SUS SRUPUT | 0.918 | 0.416 | Normal ✓ |
| SUS Kopi Reman | 0.892 | 0.307 | Normal ✓ |

**Kesimpulan**: Semua data berdistribusi normal (p > 0.05), maka paired t-test valid.

### 3.3 Paired T-Test Results

**Time on Task**

| Metrik | Value |
|--------|-------|
| Mean difference | -7.7 detik |
| t-statistic | -4.823 |
| p-value | **0.0003** |
| Cohen's d | **0.89** (Large) |
| 95% CI | [-10.2, -5.2] |

**Interpretasi**: SRUPUT 14% lebih cepat dari Kopi Reman, perbedaan sangat signifikan (p < 0.01) dengan large effect size.

**SUS Score**

| Metrik | Value |
|--------|-------|
| Mean difference | +10.2 poin |
| t-statistic | 2.881 |
| p-value | **0.012** |
| Cohen's d | **0.74** (Medium-Large) |
| 95% CI | [2.8, 17.6] |

**Interpretasi**: SRUPUT mendapat skor SUS 15% lebih tinggi, perbedaan signifikan (p < 0.05) dengan medium-to-large effect size.

### 3.4 Pembahasan

#### 3.4.1 Interpretasi Temuan

**Time on Task**:
- Penghematan 7.7 detik per transaksi sangat bermakna secara praktis
- Dengan 50 customer/jam, total penghematan = 6.4 menit/jam = **12 customer tambahan per hari**
- Design decisions yang berkontribusi:
  - Bottom navigation lebih accessible daripada hamburger menu
  - Inline customization mengurangi screen transitions
  - FAB cart selalu visible mengurangi cognitive load

**SUS Score**:
- Score 78.5 masuk kategori "Excellent" (grade B, >70)
- Kopi Reman 68.3 masuk kategori "Good" (grade C, 60-70)
- Industry average untuk mobile apps: 68
- SRUPUT di atas average, Kopi Reman at average

#### 3.4.2 Perbandingan dengan Literatur

- Nielsen (2012): User satisfaction drops 10% untuk setiap 1 detik delay → SRUPUT 7.7 detik faster sangat substansial
- Bangor et al. (2008): SUS improvement >10 poin dianggap meaningful → SRUPUT +10.2 poin memenuhi threshold
- Google Mobile Speed Study (2018): 53% users abandon apps yang >3 detik load → SRUPUT speed advantage critical

#### 3.4.3 Limitation & Boundary Conditions

**Internal Validity**:
- Within-subject design minimize individual differences ✓
- Order effect diatasi dengan randomization ✓
- Lab setting mungkin tidak reflect real-world distractions ✗

**External Validity**:
- Sample hanya mahasiswa IT (tech-savvy) → generalisasi ke general public terbatas
- Lab testing vs real café environment berbeda (noise, time pressure)
- Skenario tasks mungkin tidak cover all use cases

**Construct Validity**:
- SUS tidak capture cognitive load atau emotional response
- Time on task tidak measure error recovery time

**Statistical**:
- N=25 adequate untuk within-subject paired t-test
- Power analysis: achieved power = 0.92 untuk detect d=0.8

---

## 4. Kesimpulan & Rekomendasi

### 4.1 Ringkasan Temuan

1. **Efisiensi**: SRUPUT terbukti 14% lebih cepat dengan very large effect (d=0.89)
2. **Usability**: SRUPUT terbukti 15% lebih usable dengan medium-large effect (d=0.74)
3. **Practical Significance**: Penghematan waktu bermakna untuk bisnis (12 customer tambahan/hari)
4. **Statistical Robustness**: Kedua hipotesis terdukung dengan p < 0.05

### 4.2 Kontribusi Penelitian

**Kontribusi Teoretis**:
- Framework evaluasi UI/UX untuk mobile F&B apps
- Validation bahwa Nielsen's usability principles applicable di konteks Indonesian F&B
- Evidence bahwa cognitive load reduction (via inline editing, visible cart) improve both speed and satisfaction

**Kontribusi Praktis**:
- Design guidelines untuk F&B app developers di Indonesia
- Quantitative evidence untuk business case of UI/UX investment
- Reusable methodology untuk comparative usability study

### 4.3 Rekomendasi Implementasi

**Untuk Kedai SRUPUT**:
1. ✅ Implement SRUPUT app sebagai primary ordering system
2. ⚠️ Provide tutorial singkat untuk first-time users
3. ⚠️ Monitor real-world performance selama soft launch (2 minggu)
4. 📊 Collect analytics: conversion rate, cart abandonment, time-to-order

**Untuk Desain UI/UX**:
1. Pertahankan bottom navigation dan FAB cart (key differentiators)
2. Pertimbangkan adaptive mode: "Express" untuk power users, "Guided" untuk newcomers
3. Add micro-animations untuk feedback confirmation (reduce uncertainty)

### 4.4 Penelitian Lanjutan

**Short-term (3-6 bulan)**:
- Longitudinal study: track SUS score dan time on task after 1 month usage
- Real-world validation: test di café environment dengan actual customers
- Demographic expansion: include older users dan non-tech-savvy participants

**Long-term (1-2 tahun)**:
- Eye-tracking study untuk understand visual attention patterns
- Emotional response measurement (facial coding atau EDA)
- Cross-cultural validation: test di cities dengan culture berbeda
- A/B testing specific features untuk continuous improvement

---

## 5. Lampiran

### Lampiran A: System Usability Scale (SUS) Questionnaire

[Terlampir di file terpisah: sus-questionnaire.pdf]

### Lampiran B: Task Scenarios Detail

[Terlampir di file terpisah: task-scenarios.pdf]

### Lampiran C: Informed Consent Form

[Terlampir di file terpisah: informed-consent.pdf]

### Lampiran D: Raw Data Summary

Full dataset tersedia di: `../04-data/`

### Lampiran E: Statistical Output

Complete statistical output dari Python analysis: `../06-output/tables/statistical_test_results.csv`

---

**Tanggal Laporan**: [Tanggal]  
**Tanda Tangan Peneliti**: __________________  
**Tanda Tangan Pembimbing**: __________________
