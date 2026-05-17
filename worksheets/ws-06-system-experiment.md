# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: ____________________

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
|          | IV   |                 |                           |
|          | DV   |                 |                           |
|          | CV   |                 |                           |

4 Prinsip Desain:
  [ ] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [ ] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [ ] Measurement Integration — Pengukuran DV built-in
  [ ] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : ____________________
  Parameter      : ____________________
  Output format  : ____________________
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah prototipe UI/UX aplikasi SRUPUT menghasilkan time on task yang lebih cepat dan skor SUS yang lebih tinggi dibandingkan dengan aplikasi baseline Kopi Reman pada skenario pemesanan mandiri

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
|Desain Antarmuka | IV | Prototipe UI Cart & Payment di Figma | Mengganti tautan (link) prototipe yang diuji (SRUPUT vs Kopi Reman). |
|Waktu & Usability | DV |Alat ukur eksternal |Perekaman durasi penyelesaian tugas dan pengumpulan skor kuesioner SUS |
|Skenario Tugas | CV |Dokumen instruksi Task Scenario |Responden diberikan lembar instruksi tugas pemesanan yang sama persis |

**Apakah semua variabel bisa di-map?** [x] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅|Halaman Cart & Payment (IV) langsung terhubung dengan data perekaman waktu (DV) |
| Modularity |✅ |Desain prototipe bisa diuji secara mandiri tanpa harus membangun fungsi backend aplikasinya secara penuh |
| Controllability |✅ |Perangkat smartphone pengujian dan kualitas koneksi internet diseragamkan untuk semua responden. |
| Measurability |✅ |Durasi terekam via layar, dan skor SUS otomatis dikalkulasi melalui Google Form. |

**Prinsip mana yang paling sulit dipenuhi?** _______________
**Strategi untuk mengatasinya:**
> ___________________________________________________

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Komponen A | Komponen B | Komponen C | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full |✅|✅|✅| Time on task paling cepat|
| – A | ❌ (manual upload) | ✅ | ✅ |Waktu penyelesaian tugas membengkak drastis |
| – B | ✅ | ❌ (Harus kembali ke menu menu awal) | ✅ |Waktu sedikit bertambah jika ada salah tekan |
| – C | ✅ | ✅ | ❌ (tanpa indikator) |Kecepatan sama, namun user mungkin sedikit bingung posisiny |

**Komponen mana yang diprediksi paling berkontribusi?** _____
**Mengapa?**
> Karena proses validasi pembayaran manual (seperti menyalin nomor rekening dan mengunggah bukti transfer) adalah titik penyumbat (bottleneck) utama yang paling banyak memakan waktu dan menimbulkan cognitive load pada pengguna saat mengantre.
---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risikonya adalah kita tidak akan tahu persis fitur mana yang sebenarnya meningkatkan efisiensi atau menyebabkan pengguna kebingungan. Jika langsung menguji aplikasi utuh, saat time on task-nya lambat, kita akan kesulitan mendiagnosis sumber masalahnya. Arsitektur modular (seperti menguji komponen Cart dan Payment secara spesifik) penting karena memungkinkan isolasi variabel; kita bisa membuktikan fitur mana yang benar-benar memengaruhi performa (traceability) tanpa gangguan fitur tambahan yang tidak relevan dengan pertanyaan riset (noise)