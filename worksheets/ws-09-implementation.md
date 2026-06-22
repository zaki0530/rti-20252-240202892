# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:
  CPU     : ____________________
  RAM     : ____________________
  GPU     : ____________________
  Storage : ____________________

Software:
  OS        : ____________________
  Runtime   : ____________________
  Framework : ____________________

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
|         |         |        |               |
|         |         |        |               |

Konfigurasi:
  Config file     : ____________________
  Random seed     : ____________________
  Hyperparameters : ____________________

Reproducibility Check:
  [ ] Dependency terdokumentasi (requirements.txt / lock file)
  [ ] Seed ditetapkan di semua level (Python, NumPy, framework)
  [ ] Config di version control
  [ ] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | Intel Core i5-1135G7 (Untuk PC Analisis) / Snapdragon 680 (Untuk Smartphone Pengujian) |
| RAM | 16 GB DDR4 (PC Analisis) / 6 GB (Smartphone Pengujian) |
| GPU | Integrated Intel Iris Xe (PC Analisis) |
| OS | Windows 11 Pro 64-bit (PC Analisis) / Android 13 (Smartphone Pengujian) |
| Runtime |Python 3.10.12 |
| Framework |Figma Desktop App v116+Jupyter Notebook |
| Random Seed |42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| pandas | 2.1.1 | Untuk manipulasi, tabulasi, dan pembersihan data mentah log Time on Task dan SUS |
|scipy |1.11.3 |Untuk mengeksekusi uji statistik deskriptif dan Paired Sample T-Test. |
|matplotlib |3.8.0 |Untuk merender visualisasi grafik perbandingan durasi waktu. |
|seaborn |0.13.0 |Untuk membuat boxplot distribusi skor SUS. |
|openpyxl |3.1.2 |Untuk membaca dan mengekspor dataset mentah dari dan ke format.xlsl. |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 |42| Mean Time on Task & Skor SUS | — |
| 2 |42 |Mean Time on Task & Skor SUS | [x] Ya / [ ] Tidak |
| 3 |42 |Mean Time on Task & Skor SUS | [x] Ya / [ ] Tidak |

**Jika hasil berbeda, kemungkinan penyebab:**

> Perubahan tak sengaja pada sel di dalam file .csv atau .xlsx dataset mentah.

> Perbedaan versi scipy yang mungkin memperbarui algoritma pembulatan nilai p-value pada komputasi T-Test.

> Konfigurasi ambang batas (threshold) SUS yang di-hardcode berbeda di beberapa cell Jupyter Notebook.ya seed independen

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [x] Random seed di-set di semua level (untuk rotasi counterbalancing).
- [x] Tidak ada background process yang mengganggu (Smartphone di-set Do Not Disturb saat pengujian).
- [x] Cache dibersihkan antar-run (Cache aplikasi Screen Recorder dan Figma dibersihkan setiap ganti responden).
- [x] Config file yang sama untuk semua run (Variabel dikunci).
---

## Latihan 3 — README Eksperimen

# Judul Eksperimen: Evaluasi Komparatif Prototipe UI/UX SRUPUT vs Baseline (Kopi Reman)

## 1. Environment
- OS Analisis: Windows 11 Pro 64-bit
- OS Pengujian Lapangan: Android 13 (Resolusi Layar 1080 x 2400 pixels)
- Runtime: Python 3.10.12
- Prototyping: Figma Desktop

## 2. Installation
- Clone repositori riset.
- Buka terminal dan jalankan: `pip install -r requirements.txt` untuk mengunci dependency analisis.

## 3. Data
- File: `raw_data_sruput_eval.csv`
- Deskripsi: Dataset ini berisi 50 baris data observasi dari 25 responden (masing-masing 2 kali uji: Kondisi A dan B). Kolom mencakup `Responden_ID`, `Kondisi_Antarmuka`, `Time_on_Task_Sec`, dan `SUS_Score`.

## 4. Execution
- Untuk menjalankan ulang analisis statistik komparatif, jalankan perintah: 
  `python run_analysis.py`

## 5. Configuration
- Config file: `config.yaml`
- Parameter kunci: 
  - `alpha_level: 0.05` (Taraf signifikansi uji beda)
  - `sus_threshold: 68.0` (Batas kelayakan metrik SUS)
  - `target_time_reduction: 0.20` (Target penurunan durasi 20%)

## 6. Expected Output
- Script akan memunculkan terminal log berisi nilai rata-rata (Mean) untuk setiap metrik.
- Akan men-generate file:
  - `results_ttest.txt` (Berisi laporan lengkap t-statistic dan p-value).
  - `boxplot_sus.png` (Visualisasi sebaran skor kepuasan).

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [x] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Dokumen pedoman detail yang berisi link view-only Figma Prototipe Kondisi A dan Kondisi B agar reviewer bisa mereproduksi klik yang dilakukan responden.
> File requirements.txt yang belum di-ekspor secara final karena masih dalam tahap perancangan proposal awal (baru akan diekspor saat pengumpulan data riil dimulai).
