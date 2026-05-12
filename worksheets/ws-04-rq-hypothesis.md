# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : ____________________

Research Question:
  Tipe         : [ ] Comparison  [ ] Improvement  [ ] Exploratory
  Formulasi    : ____________________
  Variabel IV  : ____________________
  Variabel DV  : ____________________
  Metrik       : ____________________
  Dataset      : ____________________
  Baseline     : ____________________

Quality Check RQ:
  [ ] Variabel spesifik
  [ ] Metrik jelas
  [ ] Baseline ada
  [ ] Konteks disebutkan
  [ ] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : ____________________
  Jenis kontribusi        : [ ] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : ____________________

Hypothesis Pair:
  H₀ : ____________________
  H₁ : ____________________
  Threshold              : ____________________
  Justifikasi threshold  : ____________________
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:**Rancangan UI/UX pada tahap Cart & Payment belum dioptimalkan untuk mengurangi waktu pemesanan (time on task) secara signifikan di kedai kopi skala UMKM

**RQ versi pertama (tulis bebas):**
>Apakah desain aplikasi SRUPUT bisa bikin pesanan kopi lebih cepat selesai dibanding aplikasi yang sudah ada?

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Ya  |Rancangan UI/UX berbasis Design Thinking |
| Metrik terukur |Ya |Time on task (waktu penyelesaian) dan Skor SUS |
| Baseline |Ya |Aplikasi Kopi Reman |
| Dataset/konteks |Ya |Pelanggan di Kedai SRUPUT |

**Tipe RQ:** [x] Comparison / [ ] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> Apakah prototipe UI/UX aplikasi SRUPUT yang dirancang dengan metode Design Thinking menghasilkan time on task yang lebih cepat dan skor SUS yang lebih tinggi dibandingkan dengan aplikasi baseline Kopi Reman pada skenario pemesanan mandiri?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak ada perbedaan signifikan pada time on task dan skor SUS antara prototipe SRUPUT dengan aplikasi Kopi Reman |
| H₁ |Prototipe SRUPUT menghasilkan time on task yang lebih singkat dan skor SUS yang lebih tinggi dibandingkan aplikasi Kopi Reman |
| Metrik |Durasi waktu penyelesaian pesanan (detik) dan Nilai SUS (0-100) |
| Threshold |Penurunan rata-rata waktu minimal 20% dan skor SUS minimal 68 |
| Justifikasi threshold |Skor 68 adalah rata-rata standar global untuk usability, dan penghematan waktu 20% sudah cukup signifikan untuk mengurai antrean fisik. |

**Apakah hipotesis ini falsifiable?** [x] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah?H₀ terbukti benar (H₁ salah) jika saat diuji ke responden, waktu pakai SRUPUT ternyata sama lamanya atau skor SUS-nya malah lebih rendah dari Kopi Reman

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah prototipe UI/UX aplikasi SRUPUT menghasilkan F1-Score/Waktu lebih baik|
| Variable (IV) | Jenis rancangan antarmuka (Prototipe SRUPUT vs Aplikasi Kopi Reman) |
| Variable (DV) |Tingkat efisiensi pemesanan dan kepuasan pengguna. |
| Metric |Time on task (dalam detik) dan Skor instrumen SUS. |
| Data source |Pengujian langsung (task scenario) dan kuesioner dari calon pengguna kedai. |
| Analysis method |Perbandingan nilai rata-rata (Mean) skor SUS dan durasi waktu. |

**Apakah rantai lengkap?** [x] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:**Penerapan UI/UX Menggunakan Metode Design Thinking Pada Aplikasi Kopi Reman Berbasis Mobile (Al Fikri dkk., 2024)
**RQ yang diekstrak:**Bagaimana merancang UI/UX aplikasi pemesanan kopi menggunakan metode Design Thinking?
**Komponen yang hilang:** RQ di paper tersebut tidak memiliki baseline (pembanding) dan tidak menyebutkan metrik terukur secara eksplisit di dalam pertanyaannya (hanya fokus ingin membuat aplikasinya saja)