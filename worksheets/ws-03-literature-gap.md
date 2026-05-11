# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : ____________________
Database   : ____________________
Query      : ____________________
Tahun      : ____________________
Hasil awal : ____ paper → Screening → ____ paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
|       |       |        |      |        |            |

Pola yang ditemukan:
  Metode dominan     : ____________________
  Dataset umum       : ____________________
  Limitasi berulang  : ____________________

GAP IDENTIFICATION

Gap 1: [Jenis: performance / method / data / context]
  Deskripsi    : ____________________
  Bukti        : ____________________
  Signifikansi : ____________________

Gap 2: [Jenis: ____]
  Deskripsi    : ____________________
  Bukti        : ____________________
  Signifikansi : ____________________

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
|          |           |               |        |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Perancangan UI/UX Aplikasi Mobile Pemesanan Mandiri Kedai Kopi menggunakan Design Thinking
**Query pencarian:**("UI/UX") AND ("Design Thinking") AND ("coffee shop" OR "kedai kopi") AND ("aplikasi" OR "mobile")
**Database:** Google Scholar / Portal Garuda

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | *Al Fikri dkk. - JATI (Jurnal Mahasiswa Teknik Informatika)* | *2024* | *Design Thinking* | *Aplikasi Kopi Reman Berbasis Mobile* | *Peningkatan pelayanan via inovasi digital terpusat pengguna* | *Masih berfokus pada digitalisasi layanan umum, belum menargetkan penyelesaian bottleneck antrean kasir di jam padat.* |
| 2 |Pangestuti - Repositori UPN Jatim |2024 |Design Thinking |Aplikasi "Coffee Care" di Mojokerto |Prototipe aplikasi ramah alergi dengan fitur penggantian bahan. |Solusi terlalu spesifik (kustomisasi bahan alergi), belum mencakup alur pemesanan efisien untuk konsumen umum. |
| 3 |Peneliti UB - J-PTIIK Universitas Brawijaya |2022 |Design Thinking |Pemesanan dari Meja di Kedai Kopi Sari |Efektivitas 85%, kepuasan 72.5%, namun efisiensi waktu hanya 62.8% |Metrik efisiensi (waktu dan kecepatan penyelesaian tugas/transaksi) dari meja masih tergolong rendah |
| 4 |JMI Jayakarta - Jurnal Manajemen Informatika Jayakarta |2024 |Design Thinking |Website Menu di Bootchin Coffe |Digitalisasi menu kertas menjadi web dinamis untuk pengunjung |Hanya berfungsi sebagai katalog digital informatif, belum terintegrasi utuh dengan modul pembayaran dan status antrean pesanan |
| 5 |Bengi - Jurnal Sistem Informasi UMSU |2023 |Design Thinking |Aplikasi Web Penjualan UKM Meulawi Coffee |Tampilan prototipe e-commerce penjualan produk kopi |Fokus pada penjualan kopi online jarak jauh (model e-commerce), bukan transaksi dine-in/takeaway (on-premise) di lokasi kedai. |

**Pola yang terlihat — Metode dominan:** Design Thinking sangat diandalkan untuk pengembangan aplikasi ritel F&B karena empatinya yang tinggi terhadap kebutuhan visual (pain points) pengunjung
**Limitasi yang berulang:** Mayoritas aplikasi hanya memindahkan menu dari media kertas ke layar digital. Belum banyak yang secara objektif mengukur tingkat keberhasilan aplikasi dalam mengurangi durasi antrean (time on task) secara konkret, terbukti dari skor efisiensi di salah satu penelitian yang masih tertahan di persentase 62%

---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [x] Ya / [ ] Tidak | *Efisiensi waktu pemesanan (time on task) pada sistem self-order di kedai kopi masih kurang optimal untuk menangani jam-jam sibuk* |
| Method Gap | [ ] Ya / [x] Tidak | |
| Data Gap | [ ] Ya / [x] Tidak | |
| Context Gap | [x] Ya / [ ] Tidak |Rancangan antarmuka (UI) dan interaksi (UX) pada tahap pembayaran dan modul cart sering kali belum diuji kemudahannya khusus untuk mengurangi panjang antrean fisik di UMKM daerah. |

**Gap utama yang dipilih:**Performance & Context Gap (Optimalisasi alur Cart & Payment untuk memangkas time on task)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
>Karena dalam skenario dunia nyata di lokasi, sebagus apa pun visual desain prototipe di Figma, jika pengguna mengalami cognitive load (kebingungan) saat melakukan proses checkout dan pembayaran, mereka akan memakan waktu terlalu lama di aplikasi. Ujung-ujungnya, antrean fisik di kasir tetap tidak bisa terurai. Fokus perancangan harus ditekankan pada kecepatan penyelesaian tugas
---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Al Fikri dkk. (2024) |Sama-sama mendesain aplikasi mobile kopi | Mewakili praktik digitalisasi retail kopi di tataran aplikasi mobile. | Ya (cukup baru).| JATI|
| 2 |Peneliti UB (2022) |Fokus pada penyelesaian masalah pemesanan on-premise (dari meja). |Mengukur efisiensi sistem pemesanan langsung di tempat menggunakan metrik persentase. |Bukan, tapi relevan dan kokoh. |J-PTIIK |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [ ] Tidak
> Justifikasi:Tidak, pemilihan ini sangat adil. Paper baseline yang dipakai sama-sama menggunakan Design Thinking untuk aplikasi F&B. Jadi perbandingannya sudah seimbang (apple-to-apple), bukan sengaja memilih paper yang jelek cuma agar desain prototipe yang baru kelihatan lebih bagus
---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Bedanya ada di bukti. Klaim "belum ada" biasanya cuma tebakan asumsi saja. Sedangkan research gap yang valid bisa dibuktikan lewat tabel literatur. Dari tabel itu akan langsung kelihatan pola dan kelemahan apa saja yang berulang dari paper-paper sebelumnya, sehingga ruang kosong masalahnya memang benar-benar ada, bukan sekadar karangan peneliti