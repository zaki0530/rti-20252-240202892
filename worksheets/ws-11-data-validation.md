# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

`Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data`

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Skor SUS = 110 (di luar batas maksimal 100) |
| **Consistency** | Format seragam di semua run | Responden 1: detik, Responden 2: menit |
| **Completeness** | Tidak ada data hilang dari plan | 24 dari 25 responden mengisi kuesioner |
| **Validity** | Data sesuai desain eksperimen | Data uji Kopi Reman tercampur di data SRUPUT |

### Proses Validasi Progresif

1. **Format validation** — Tipe file CSV, header sesuai, kolom *Time on Task* dan *SUS*
2. **Range validation** — Waktu pengerjaan > 0 detik, Skor SUS 0 - 100
3. **Consistency validation** — Format waktu konsisten menggunakan hitungan detik
4. **Logic validation** — Responden benar-benar masuk dalam kriteria *purposive sampling*

Jika gagal di langkah awal → tidak perlu lanjut.

---

## Template A.11 — Data Validation Checklist

```text
DATA VALIDATION CHECKLIST

Completeness:
  [x] Semua skenario tercakup (Skenario A & B)
  [x] Jumlah run sesuai rencana (25 Responden × 2 Skenario = 50 run)
  [x] Tidak ada file output hilang
  Missing: 0 dari 50 data points

Format Consistency:
  [x] Semua file format sama (.csv hasil export Google Form/Figma Log)
  [x] Header konsisten
  [x] Tipe data konsisten (waktu direkam dalam detik (integer))

Range & Logic:
  [x] Nilai dalam range masuk akal
  [x] Tidak ada waktu negatif
  [x] Metrik Skor SUS 0–100, tidak di luar range
  Anomali ditemukan: 1 data waktu penyelesaian jauh lebih lama dari rata-rata (Responden 4)

Cross-Validation:
  [x] Run identik → hasil mendekati
  [x] Trend konsisten dengan ekspektasi teori (Aplikasi SRUPUT lebih cepat dari baseline)

Keputusan:
  [x] Data siap analisis (setelah pembersihan anomali)
  [ ] Perlu cleaning
  [ ] Perlu re-run
---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Eksperimen Skenario A (Kopi Reman) | 25 | 25 | 0 | Dilakukan pendampingan langsung secara offline sehingga semua sesi terekam penuh |
| Eksperimen Skenario B (SRUPUT) | 25 | 25 | 0 |Semua log interaksi terekam otomatis secara akurat melalui fitur prototype Figma  |
|Kuesioner SUS |25 |25 |0 |Responden diwajibkan melakukan submit Google Form sebelum mengakhiri sesi tes |


Total expected:75 data points | Total actual: 75 | Missing: 0
Keputusan untuk data missing:**
> Tidak ada data yang missing. Seluruh 25 responden berhasil menyelesaikan tes dan mengisi kuesioner karena metode pengujian dilakukan secara terawasi langsung (Moderated Usability Testing)

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Accuracy (%) |
|-----|-------------|
| 1 | 45 |
| 2 | 48 |
| 3 | 42 |
| 4 | 125 |
| 5 | 46 |
| 14|12|
|21 |89|
**Deteksi outlier:**
- Q1 = 43.5 | Q3 = 48.0 | IQR = 4.5
- Batas bawah (Q1 - 1.5×IQR) = 36.75
- Batas atas (Q3 + 1.5×IQR) = 54.75
- Outlier terdeteksi: Responden 4 (125 detik)

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
| Run 4 | 125 | Responden menerima panggilan telepon saat mengerjakan task / distraksi lingkungan luar. | Eksklusi (hapus) data Time on Task Responden 4 dari analisis statistik agar tidak merusak mean/rata-rata, karena bukan kesalahan desain antarmuka |
| Run 14 | 12 |Responden melakukan speed-clicking (asal pencet) tanpa membaca instruksi Task Scenario|Eksklusi total data Responden 14 karena perilaku pengujian dianggap tidak valid |
| Run 21|89 |Responden kebingungan mencari ikon keranjang karena area klik (hitbox) terlalu kecil di layar HP-nya|Data dipertahankan. Catat sebagai temuan usability issue untuk perbaikan desain prototipe|
---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

1. Completeness: 100% data terkumpul (25 Responden).
2. Format: [x] Konsisten / [ ] Ada inkonsistensi: -
3. Range check (anomali): 1 Anomali kontekstual ditemukan pada data Time on Task.
4. Logic check: [x] Parameter sesuai plan / [ ] Ada ketidaksesuaian

**Kesimpulan:[x] Data siap analisis / [ ] Perlu tindakan: Eksklusi 1 data outlier dari perhitungan Time on Task.
---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Data yang benar adalah angka aktual yang terekam oleh sistem atau alat ukur (misalnya, stopwatch mencatat 125 detik). Sedangkan "data yang dipercaya" adalah data yang valid secara konteks dan bebas dari variabel pengganggu (noise). Proses validasi formal tetap wajib dilakukan untuk menyaring anomali kontekstual; misalnya, waktu terekam lama bukan karena UI/UX-nya buruk, melainkan karena responden terdistraksi (seperti pada contoh Responden 4). Tanpa validasi, data yang "benar" secara angka bisa menyesatkan kesimpulan penelitian.