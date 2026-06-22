# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     |          |      |           |        |       |             |
| 2     |          |      |           |        |       |             |
| 3     |          |      |           |        |       |             |
| ...   |          |      |           |        |       |             |

Jumlah runs per skenario : ____
Total runs               : ____

DATA LOG (per run):
  Run ID    : ____________________
  Timestamp : ____________________
  Skenario  : ____________________
  Input     : ____________________
  Output    : ____________________
  Anomali   : ____________________
  Catatan   : ____________________
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Skenario 1 | Nomor Acak 1 | Perangkat, Instruksi, Lingkungan | Responden 1 |
| 2 | Skenario 2 | Nomor Acak 2| Perangkat, Instruksi, Lingkungan | Responden 2 |
| 3 |Skenario 1 |Nomor Acak 3 |Perangkat, Instruksi, Lingkungan |Responden 3 |
| 4 |Skenario 2 |Nomor Acak 4 |Perangkat, Instruksi, Lingkungan |Responden 4 |
| 5 |Skenario 1 |Nomor Acak 5 |Perangkat, Instruksi, Lingkungan |Responden 5 |
|...|(dirotasi terus berselang-seling)|(Nomor acak selanjutnya)|(Sampai 25 responden)|
**Total skenario:**2 Skenario Urutan (A→B dan B→A).
**Run per skenario:** 13 Responden (A→B) dan 12 Responden (B→A).
**Total run keseluruhan:** 25 Sesi Observasi Responden (Menghasilkan 50 pasang data).

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Log_ID| 1 |
| Timestamp_Test| 2026-06-12 10:30:00 |
|Kondisi_Antarmuka|A (Baseline Kopi Reman) |

**Hasil (Metrics):**
|Metrik|	Tipe Data|	Range Valid|
|Time_on_Task_Sec|	Float (Ratio)|	> 0 detik (Hasil ekstraksi dari screen recording)|
|SUS_Q1_Q10_Raw|	Array of Int|	1 sampai 5 (Skala Likert per pertanyaan)|
|SUS_Total_Score|	Float (Interval)|	0.0 – 100.0 (Hasil konversi bobot)|

**Metadata & Observasi:**
| Field | Contoh |
|-------|--------|
| Task_Status |Success / Failed / Abandoned|
| Catatan_Perilaku | Responden sempat kebingungan mencari tombol edit keranjang selama 4 detik. |
| | |


**Format output:** [x] CSV (Disimpan sebagai raw_data_sruput_eval.csv) / [ ] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
|Data hilang/Crash | Perekam layar (screen recorder) mati di tengah sesi atau file video corrupt | Sesi dibatalkan. Responden tersebut dianggap gagal (DNF), data dibuang, dan mencari 1 responden pengganti baru. |
| Task Abandonment|Responden menyerah (tidak bisa menyelesaikan pesanan) pada salah satu aplikasi setelah 5 menit. |Catat durasi maksimal (5 menit), nilai SUS tetap diambil, dan ditandai sebagai task failed untuk analisis lanjutan. |
|Interupsi Eksternal |Ada panggilan telepon masuk atau responden diajak mengobrol orang lain di tengah pengerjaan. |Jika interupsi > 5 detik, durasi waktu akan dipotong secara manual (video editing) di bagian interupsi sebelum dihitung metriknya. |
| Hasil Ekstrem (Outlier) |Responden menyelesaikan pesanan dalam 2 detik (terindikasi tidak membaca tugas asal klik). |Investigasi rekaman layar. Jika terbukti asal klik, data dibuang (ditandai sebagai invalid log) dan cari responden pengganti. |

**Prinsip:** Segala intervensi/pembuangan data harus dicatat alasannya secara transparan di log!

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Dulu saat menguji UI tugas kuliah, saya hanya meminta satu atau dua teman mencoba aplikasi, lalu langsung menyimpulkan "aplikasi ini cepat dan mudah digunakan" hanya karena mereka tidak menemui error.
Risikonya: Hasilnya sangat bias (subjektif). Jika aplikasi dicoba oleh orang tua atau pelanggan awam, mereka bisa jadi kesulitan, sehingga kesimpulan saya patah saat diimplementasi di lapangan.
**Yang akan dilakukan berbeda:**
>Pada riset UTS ini, saya mewajibkan minimal 25 responden dari kalangan umum (multiple runs). Ini akan memberikan distribusi durasi yang masuk akal dan nilai statistik rata-rata yang bisa dipertanggungjawabkan (menghapus faktor kebetulan). Uji beda (T-Test) juga memastikan bahwa kecepatan SRUPUT benar-benar terjadi karena desainnya, bukan karena kebetulan respondennya sedang cepat mengetik
