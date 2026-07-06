# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

`Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight`

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko menghasilkan kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |
*(Referensi tabel:[cite: 2])*

### Contoh Tabel Hasil yang Baik

| Model (Aplikasi) | Time on Task (Detik) | Skor SUS (0-100) | Jumlah Kesalahan Klik |
|-------|-------------|-------------|---------------------|
| SRUPUT (Prototipe) | 45.2 ± 5.1 | 85.5 ± 4.2 | 1.2 ± 0.5 |
| Kopi Reman (Baseline) | 68.4 ± 8.2 | 62.1 ± 7.4 | 4.1 ± 1.2 |

*N=23 responden valid per model (setelah pembersihan data). Mean ± std. Diurutkan berdasarkan efisiensi waktu.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |
*(Referensi tabel:[cite: 2])*

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |
*(Referensi tabel:[cite: 2])*

---

## Template A.12 — Result Presentation Plan

```text
RESULT PRESENTATION PLAN

Research Question : Apakah desain prototipe SRUPUT meningkatkan efisiensi waktu pemesanan dan kepuasan pengguna dibandingkan aplikasi baseline Kopi Reman?
Metrik Utama      : Time on Task (Detik) dan Skor System Usability Scale (SUS)

Tabel Hasil:
| Skenario | Time on Task (mean ± std) | Skor SUS (mean ± std) | n |
|----------|----------------------|----------------------|---|
| Baseline (Kopi Reman) | 68.4 ± 8.2 | 62.1 ± 7.4 | 23 |
| Treatment (SRUPUT)  | 45.2 ± 5.1 | 85.5 ± 4.2 | 23 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar Chart + Error Bar | Membandingkan rata-rata waktu pengerjaan tugas | Mean Time on Task |
| 2 | Box Plot | Menampilkan distribusi sebaran Skor SUS antar responden | Skor SUS individual |

Bias Check:
  [x] Y-axis mulai dari 0 (atau dijustifikasi)
  [x] Error bar/CI ditampilkan
  [x] Semua data disertakan (tidak cherry-picked)
  [x] Tidak menggunakan 3D tanpa alasan

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Metrik 1 (mean ± std) | Metrik 2 (mean ± std) | n |
|----------|----------------------|----------------------|---|
| Skenario A Kopi Reman  | 68.4 ± 8.2 detik | 62.1 ± 7.4 poin | 23 |
|Skenario B kopi sruput |45.2 ± 5.1 detik |85.5 ± 4.2 poin |23 |
| | | | |

**Checklist tabel:**
- [x] Self-contained (judul jelas, satuan ada, N tercantum)
- [x] Mean ± std (bukan single number)
- [x] Diurutkan berdasarkan metrik utama
- [x] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar chart + error bar | SRUPUT mempercepat waktu penyelesaian task dibanding Kopi Reman | Mean Time on Task ± std |
| 2 | Box plot | Mayoritas responden memberikan rating kepuasan yang lebih seragam dan tinggi untuk SRUPUT | Semua data raw Skor SUS |
| 3 | Scatter plot | Menunjukkan korelasi: semakin cepat waktu task, umumnya semakin tinggi skor SUS | Time on Task vs Skor SUS per responden |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Ya. Karena grafik tidak dimulai dari 0 (Truncated axis), perbedaan 0.4% akan terlihat seperti Metode A dua kali lipat lebih besar dari Metode B, ini manipulatif secara visual. |
| Apakah error bar ditampilkan? |Tidak. Tidak ada indikasi standar deviasi atau rentang error |
| Apakah semua kondisi ditampilkan? |(Asumsi ya, hanya A dan B). |
| Apa solusinya? |Mulai sumbu Y (Y-axis) dari 0 hingga 100%, dan tambahkan garis error bar untuk menunjukkan variabilitas data. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [x] Semua bias check lulus
- [ ] Ada yang perlu diperbaiki: ____

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Tabel sangat penting untuk memberikan nilai presisi yang absolut (misalnya pembaca ingin tahu persis berapa detiknya)[cite: 2]. Namun, manusia lebih mudah membaca pola melalui gambar (grafik)[cite: 2]. Grafik Box Plot, misalnya, bisa langsung menunjukkan seberapa banyak responden yang merasa kesulitan dengan Kopi Reman dibandingkan melihat deretan angka di tabel. Dulu saya pernah membuat grafik bar chart tanpa error bar, sehingga seolah-olah semua responden mencetak waktu yang persis sama, padahal kenyataannya kecepatan tiap orang sangat bervariasi.
