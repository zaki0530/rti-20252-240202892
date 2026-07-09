# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : ____ (target: 10-12 konten + title/closing)
  Time per slide : ~2 min
  Total time     : ____ menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Title       |        | 30s   |
| 2 | Problem     |        | 2min  |
| 3 | Gap + RQ    |        | 2min  |
| ..|             |        |       |

Anticipatory Defense Matrix:
| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|---------------------|---------------|
| Problem  |                     |               |
| Gap      |                     |               |
| Method   |                     |               |
| Results  |                     |               |
| Generalization |               |               |

Latihan:
  Latihan 1: [tanggal] — [catatan timing & feedback]
  Latihan 2: [tanggal] — [catatan timing & feedback]
  Latihan 3: [tanggal] — [catatan timing & feedback]
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Masalah antrian panjang di kedai kopi karena aplikasi pemesanan lambat | Foto antrian + screenshot aplikasi existing | 2 min |
| 2 | Gap: belum ada evaluasi UI/UX aplikasi F&B secara komprehensif | Tabel gap literatur + positioning | 1.5 min |
| 3 | RQ: Apakah prototipe SRUPUT lebih efisien dan usable dibanding Kopi Reman? | Screenshot kedua aplikasi side-by-side | 1 min |
| 4 | Method: Within-subject design, 25 responden, time on task + SUS score | Diagram flow eksperimen | 2 min |
| 5 | Hasil utama: SRUPUT lebih cepat dan lebih usable | Bar chart perbandingan kedua metrik | 2.5 min |
| 6 | Statistical significance dan effect size | Tabel hasil uji statistik dengan p-value dan Cohen's d | 2 min |
| 7 | Interpretasi: Trade-off speed vs complexity, boundary conditions | Scatter plot user experience vs task complexity | 2 min |
| 8 | Limitation: Sample bias mahasiswa IT, lab setting | Bullet points limitation dengan impact assessment | 1.5 min |
| 9 | Kontribusi: Framework evaluasi UI/UX + practical guidelines | Summary slide kontribusi teoretis dan praktis | 1.5 min |

**Total waktu estimasi:** 16 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Problem | Mengapa fokus ke UI/UX, bukan fitur aplikasi? | UI/UX langsung berdampak pada waktu pemesanan dan kepuasan pengguna | Antrian >10 menit di jam sibuk, keluhan pengguna soal aplikasi lambat | Aplikasi cepat mengurangi antrian = revenue lebih tinggi untuk kedai |
| 2 | Method | Mengapa hanya 25 responden? | Untuk paired t-test dengan power 0.8, minimal 23 responden untuk detect medium effect | Perhitungan power analysis di Method, effect size d=0.74 terdeteksi | Sample size adequate untuk within-subject design |
| 3 | Results | Apakah perbedaan 7.5 detik bermakna praktis? | Ya, dalam konteks antrian panjang 7.5 detik per customer = penghematan signifikan | 50 customer/jam = hemat 6 menit/jam = 12 customer tambahan per hari | Practical significance tinggi untuk bisnis kedai kopi |
| 4 | Generalization | Apakah hasil bisa digeneralisasi ke aplikasi F&B lain? | Prinsip UI/UX bisa, tapi perlu validasi untuk konteks berbeda | Responden hanya mahasiswa IT, setting lab bukan real-world | Listed sebagai limitation - future work perlu demografis lebih luas |
| 5 | Method | Mengapa tidak ada control group? | Within-subject design lebih powerful dan mengurangi variabilitas individual | Setiap responden jadi control untuk dirinya sendiri, order effect diatasi dengan randomisasi | Design choice untuk maximize statistical power dengan sample terbatas |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | Bagaimana Anda memastikan responden tidak bias karena sudah tahu tujuan penelitian? | Responden hanya diberi instruksi tugas tanpa diberitahu hipotesis. Urutan aplikasi dirandomisasi untuk menghindari order effect. Dijelaskan di bagian prosedur Method. | [✓] Direct [✓] Data-based [✓] Honest |
| 2 | Apakah 25 responden cukup untuk generalisasi? | Untuk within-subject design, 25 responden adequate untuk detect medium-to-large effect (power analysis). Namun generalisasi terbatas karena sample hanya mahasiswa IT - listed sebagai limitation. | [✓] Direct [✓] Data-based [✓] Honest |
| 3 | Mengapa tidak menggunakan eye-tracking atau heatmap untuk evaluasi UI? | Eye-tracking memerlukan peralatan mahal dan analisis kompleks yang di luar scope studi ini. Time on task dan SUS sudah established metrics yang valid untuk usability evaluation. Future work bisa tambahkan eye-tracking. | [✓] Direct [✓] Data-based [✓] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Pertanyaan tentang generalisasi ke demografis yang lebih luas. Sulit dijawab karena memang limitation utama dari sample mahasiswa IT. Perlu acknowledge limitation secara jujur sambil menjelaskan trade-off feasibility vs representativeness.

**Apa yang perlu disiapkan lebih baik:**
> Perlu data benchmark SUS dari aplikasi F&B lain untuk perbandingan konteks yang lebih kaya. Juga perlu siapkan justifikasi lebih detail tentang pemilihan within-subject design vs between-subject design.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?

**Insight terbesar:**
> Riset bukan hanya tentang menemukan jawaban yang "benar", tapi tentang memahami boundary conditions dan trade-offs dari setiap solusi. Failure analysis dan limitation bukan kelemahan, justru menunjukkan kedalaman pemahaman dan kejujuran ilmiah.

**Yang akan selalu diterapkan:**
> Pre-registration metrik sebelum eksperimen dan always report effect size + confidence interval, bukan hanya p-value. Ini mencegah p-hacking dan memberikan gambaran lengkap tentang practical significance dari temuan.
