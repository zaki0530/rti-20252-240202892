# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

`Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready`

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |
*(Referensi tabel:)*

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |
*(Referensi tabel:)*

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |
*(Referensi tabel:)*

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data[cite: 3]. Pelanggaran = **data leakage**[cite: 3]. *(Catatan: Konsep Data Leakage khusus untuk Machine Learning, kurang relevan untuk pengujian komparatif UI/UX eksperimental T-Test/ANOVA).*

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing[cite: 3]:
- Normalisasi parameter dari seluruh dataset ← **SALAH**[cite: 3]
- Cross-validation dilakukan sebelum split ← **SALAH**[cite: 3]
- Feature selection menggunakan label test set ← **SALAH**[cite: 3]

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan[cite: 3]
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data[cite: 3]
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis[cite: 3]
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks[cite: 3]

---

## Template A.13 — Preprocessing Documentation Log

```text
PREPROCESSING LOG

Dataset           : Log Usability Testing & Kuesioner SUS (Kopi Reman vs SRUPUT)
Jumlah data awal  : 50 observasi (25 Responden × 2 Aplikasi)

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Outlier Ekstrem | 2 responden (4 observasi) | Listwise deletion | Responden terdistraksi (Run 4) & tidak serius (Run 14) merusak objektivitas. |
| Duplikat| 0           | -          | -           |
| Error   | 0           | -          | -           |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Perhitungan SUS | Skor_SUS_Total | Nilai mentah kuesioner dikonversi menggunakan rumus standar (Brooke). | Merubah skala Likert mentah menjadi metrik baku 0-100. |

Normalization:
  Metode    : Tidak dilakukan.
  Alasan    : Data metrik UX (Time on Task dan Skor SUS) akan diuji menggunakan parametrik komparasi (T-Test) yang tidak memerlukan scaling [0,1].
  Parameter : N/A

Leakage Check:
  [x] Parameter normalisasi dari training set saja (N/A)
  [x] Tidak ada informasi test set dalam preprocessing (N/A)
  [x] Cross-validation dilakukan setelah split (N/A)

Jumlah data akhir : 46 observasi valid (23 Responden × 2 Aplikasi)
Script tersedia   : [ ] Ya → path: ____ | [x] Belum

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Outlier Waktu Ekstrem (Terlalu Lama) | 1 Responden (Run 4) | Listwise deletion | Responden menerima telepon, jeda waktu bukan disebabkan oleh UI/UX aplikasi (Noise/Contextual Anomaly) |
|Outlier Waktu Ekstrem (Terlalu Cepat) |1 Responden (Run 14) |Listwise deletion |Responden melakukan asal klik tanpa membaca task (Invalid data). |
| | | | |
| | | | |

Jumlah data sebelum cleaning: 25 Responden (50 observasi)
Jumlah data setelah cleaning: 23 Responden (46 observasi)
Persentase data yang hilang/berubah: 8%
---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Time on Task | 12 - 125 detik | Normal (setelah cleaning) | Sudah dihapus| Tidak perlu | Uji T-Test tidak mewajibkan normalisasi jarak. |
|Skor SUS |40 - 95 poin |Normal |Tidak  |Tidak perlu |Skala sudah terstandarisasi absolut di 0-100. |

**Apakah normalisasi diperlukan?** [ ] Ya / [x] Tidak
**Justifikasi:**
> Normalisasi (seperti Z-score atau Min-Max) dapat mengubah nilai nyata dari pengujian (detik/skor) menjadi nilai proporsi yang sulit dibaca pemangku kepentingan. Karena ini adalah riset UX dan bukan pemodelan Machine Learning, metode Minimal Distortion diutamakan

**Leakage check:**
- [x] Parameter dihitung dari training set saja
- [x] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: Log Usability (Time on Task) & Kuesioner (Skor SUS)
2. Data awal: 50 records, 2 features (Waktu & Skor)
3. Cleaning:
   - Missing values: 4 records (Listwise deletion, dari 2 responden invalid).
   - Duplikat: 0 kasus, tindakan: -
   - Error: 0 kasus, tindakan: -
4. Transformation: Konversi item kuesioner Likert mentah menjadi Skor SUS 0-100.
5. Normalisasi: Tidak diterapkan (metode), parameter dari (N/A)
6. Data akhir: 46 records, 2 features
7. Leakage check: [x] Lulus / [ ] Ada masalah

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Ya, terkadang ada tendensi untuk memproses data berlebihan agar terlihat rumit dan "ilmiah". Padahal, sesuai jebakan kognitif, "lebih banyak preprocessing = lebih bersih = lebih baik" adalah pemahaman yang salah dan justru dapat mendistorsi data (over-processing)[cite: 3]. Untuk metrik UI/UX, mengubah nilai detik menjadi skala [0,1] justru menghilangkan informasi berharga yang paling dibutuhkan oleh desainer dan stakeholder saat evaluasi.