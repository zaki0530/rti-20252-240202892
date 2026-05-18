# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [ ] Problem → Gap: masalah terdokumentasi di literatur
  [ ] Gap → RQ: pertanyaan menjawab gap spesifik
  [ ] RQ → Hypothesis: hipotesis memprediksi jawaban
  [ ] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [ ] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [ ] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [ ] Istilah sama di semua bagian
  [ ] Variabel di RQ = variabel di hipotesis = metrik di desain
  [ ] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [ ] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [ ] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [ ] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [ ] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [ ] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        |      |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   |      |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail |      |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   |      |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Antrean manual di Kedai Kopi SRUPUT panjang dan lama pada jam sibuk. |
| Gap | WS-03 | Belum ada optimalisasi UI/UX khusus pada alur Cart & Payment untuk memangkas waktu pemesanan mandiri di UMKM daerah. |
| RQ | WS-04 | RQ: Apakah prototipe SRUPUT menghasilkan time on task lebih cepat dan skor SUS lebih tinggi dibanding Kopi Reman? |
| Hipotesis | WS-04 | H₁: Prototipe SRUPUT menghasilkan waktu lebih cepat dan skor SUS lebih tinggi. |
| Variabel & Metrik | WS-05 | Time on task (detik) dan Skor SUS (skala 0-100). |
| Sistem | WS-06 | Artefak berupa Prototipe interaktif Figma (Modul Cart & Payment) dan alat rekam pengujian. |
| Desain Eksperimen | WS-07 | Controlled Comparison Study dengan metode Counterbalancing pada 20-30 responden pelanggan kedai. |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✅ | Gap memfokuskan masalah antrean umum ke area spesifik, yaitu kemudahan alur transaksi digital. |
| Gap → RQ | ✅ | RQ langsung menguji solusi pengisian celah tersebut dengan membandingkannya terhadap baseline. |
| RQ → Hypothesis | ✅ | Hipotesis H₁ memprediksi arah performa kedua metrik utama secara tegas dan terukur. |
| Hypothesis → Metric | ✅ | Variabel abstrak (efisiensi & kepuasan) langsung diturunkan ke metrik konkret (detik & poin SUS). |
| Metric → System | ✅ | Modul prototipe Figma dirancang agar bisa memicu pencatatan waktu dan pengisian kuesioner. |
| System → Experiment | ✅ | Desain eksperimen menggunakan prototipe tersebut sebagai objek uji utama ke pengguna. |

**Koneksi mana yang paling lemah?** Metric
**Bagaimana cara memperkuatnya?**
> Menggunakan metode Screen Recording saat pengujian untuk meminimalkan human error atau delay milidetik saat mencatat waktu secara manual

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [x] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? _________

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi |3|Alur dari penemuan masalah di kedai hingga metode eksperimennya tersambung logis tanpa lompatan |
| Specificity | 3|Metrik evaluasi (detik, skor SUS) dan nama baseline (Kopi Reman) sudah tertulis jelas dan numerik. |
| Feasibility |3 |Riset berbasis prototipe Figma sangat realistis diselesaikan tepat waktu tanpa kendala coding backend. |
| Rigor |2 |Perlu komitmen kuat dan waktu ekstra untuk memitigasi threat saat mencari responden pelanggan asli di lapangan. |

**Skor total:** 11 / 12

**Apakah proposal siap untuk fase eksekusi?** [x] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? __________________

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:**Menentukan metrik evaluasi (Time on Task dan SUS) karena standarnya sudah baku dan sangat jelas untuk pengujian UI/UX
**Bagian tersulit:** Menemukan paper baseline (Kopi Reman) yang pas dan menyusun Boolean search query yang benar-benar menyaring jurnal relevan di awal
**Yang akan dilakukan berbeda:**
> Memetakan dan mengumpulkan jurnal referensi bertema sejenis jauh-jauh hari agar memiliki lebih banyak pilihan baseline alternatif yang matang.
