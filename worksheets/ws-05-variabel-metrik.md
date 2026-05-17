# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: ____________________

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
|          | IV   |        |        |       |        |               |             |
|          | DV   |        |        |       |        |               |             |
|          | CV   |        |        |       |        |               |             |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [ ] Setiap langkah terdokumentasi
  [ ] Tidak ada "lompatan logis"
  [ ] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:**Apakah prototipe UI/UX aplikasi SRUPUT menghasilkan time on task yang lebih cepat dan skor SUS yang lebih tinggi dibandingkan dengan aplikasi baseline Kopi Reman pada skenario pemesanan mandiri?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
|Jenis Aplikasi | *IV* | *Pendekatan klasifikasi* | Prototipe SRUPUT vs Aplikasi Kopi Reman | Nominal | — |
|Waktu Selesai | DV |Efisiensi sistem |Waktu dari buka aplikasi sampai pembayaran berhasil |Ratio |Detik |
|Tugas | CV |Kompleksitas pesana |Menyamakan instruksi |Nominal |—|

|Nilai Usability||DV||Kepuasan & kemudahan||Skor akhir instrumen System Usability Scale||Interval||Poin (0-100)|
**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [x] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative |5	|Waktu yang dihitung dalam detik sangat akurat mewakili tingkat "efisiensi kecepatan" pemesanan untuk mengurangi antrean. |
| Sensitive |5|Sangat peka menangkap perbedaan waktu, meskipun SRUPUT dan Kopi Reman hanya selisih 3 detik saja |
| Feasible |5|Sangat praktis untuk dikumpulkan, cukup menggunakan perangkat stopwatch di smartphone saat responden melakukan testing |

**Apakah perlu secondary metric?** [x] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Persentase keberhasilan.Karena percuma waktu pengerjaannya sangat cepat (time on task rendah) jika ternyata pesanannya keliru atau responden gagal mencapai halaman pembayaran.
**Contoh kasus ceiling effect untuk metrik ini:**
>Jika skenario tugas (CV) yang diberikan terlalu gampang (misalnya pengguna hanya diminta menekan 1 tombol "Pesan Ulang"), maka baik di aplikasi SRUPUT maupun Kopi Reman akan mendapatkan waktu 1 detik. Akibatnya, metrik ini mentok pada nilai tertinggi dan gagal membuktikan aplikasi mana yang sebenarnya memiliki desain UI yang lebih baik.
---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point kuesioner terkumpul|Rentan ada responden yang lupa menjawab 1-2 poin pertanyaan SUS. |Menggunakan Google Form dan mengaktifkan fitur "Required" pada setiap butir soal SUS |
| Consistency | Apakah ada kontradiksi internal |Waktu mulai dan berhenti stopwatch mungkin beda-beda tiap responden |Membuat SOP baku (Contoh: Stopwatch ditekan tepat saat jari menyentuh layar pertama, dan distop saat muncul tulisan Invoice) |
| Validity | Apakah benar-benar mengukur yang dimaksud |Responden salah fokus mengkritik kecepatan internet, bukan desain UI-nya |Melakukan pengujian menggunakan Wi-Fi yang sama untuk semua responden agar faktor sinyal internet terkontrol |
| Representativeness | Apakah sampel mewakili populasi target |Responden hanya diisi oleh teman mahasiswa yang jago main HP. |Merekrut responden langsung dari pembeli di Kedai SRUPUT, mencakup berbagai rentang usia. |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Karena memilih metrik setelah melihat data (p-hacking) dianggap sebagai kecurangan karena peneliti bisa sengaja memilih metrik yang hanya menguntungkan atau memuluskan hasil risetnya saja.

> Bedanya dengan eksplorasi yang sah adalah, dalam eksplorasi metrik utama sudah dikunci sejak awal (pre-registration). Jika di tengah jalan ditemukan pola data lain yang menarik, hal itu hanya dilaporkan sebagai temuan tambahan (secondary/exploratory metric) tanpa membuang atau memanipulasi metrik utama