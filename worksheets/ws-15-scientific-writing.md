# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : ____________________
Target  : [ ] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [ ] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [ ] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [ ] Related Work — concept-centric, gap positioning
  [ ] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [ ] Results — tabel + grafik + observasi (tanpa interpretasi)
  [ ] Discussion — interpretasi, perbandingan, implikasi, limitation
  [ ] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [ ] RQ di Introduction = RQ di Method = RQ di Conclusion
  [ ] Variabel di Method = variabel di Results
  [ ] Klaim di Discussion didukung data di Results
  [ ] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [ ] Clarity — mudah dipahami tanpa re-read
  [ ] Precision — tidak ada istilah ambigu
  [ ] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Aplikasi pemesanan kopi memiliki masalah efisiensi dan usability. Studi ini membandingkan prototipe SRUPUT dengan baseline Kopi Reman menggunakan time on task dan SUS score. Hasil: SRUPUT 14% lebih cepat dengan skor usability 15% lebih tinggi. | 200-250 |
| Introduction | Konteks: antrian panjang di kedai kopi karena aplikasi pemesanan lambat. Gap: belum ada studi yang mengevaluasi UI/UX pemesanan mandiri secara komprehensif. RQ: apakah desain prototipe SRUPUT meningkatkan efisiensi dan usability dibanding aplikasi existing? | 500-700 |
| Related Work | Review studi UI/UX aplikasi F&B, time on task sebagai metrik efisiensi, dan SUS sebagai standar usability measurement. Gap positioning terhadap studi sebelumnya yang fokus fitur tanpa evaluasi user experience. | 700-1000 |
| Method | Within-subject design, 25 responden, 2 skenario pemesanan (simple & complex), metrik time on task dan SUS score, prosedur randomized order, analisis paired t-test. | 800-1200 |
| Results | Statistik deskriptif kedua aplikasi, hasil uji normalitas, paired t-test results dengan effect size, visualisasi perbandingan time on task dan SUS score. | 500-800 |
| Discussion | Interpretasi superioritas SRUPUT, perbandingan dengan benchmark SUS industry, implikasi untuk desain aplikasi F&B, limitation (sample bias, generalisasi), boundary condition. | 600-900 |
| Conclusion | SRUPUT terbukti superior dalam efisiensi dan usability. Kontribusi: framework evaluasi UI/UX aplikasi pemesanan. Future work: evaluasi di setting real-world dan demografis yang lebih luas. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| *Contoh: RQ1* | *✓* | *✓* | *✓* | *✓* | *✓* |
| *Contoh: Metrik-X* | *✗ ←* | *✗ ←* | *✓* | *✗ ←* | *✗ ←* |
|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ: Efisiensi SRUPUT vs Kopi Reman | ✓ | ✓ | ✓ | ✓ | ✓ |
| RQ: Usability SRUPUT vs Kopi Reman | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik Time on Task | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik SUS Score | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel Jenis Aplikasi (IV) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Within-subject design | ✗ | ✓ | ✗ | ✓ | ✗ |
| Limitation sample bias | ✗ | ✗ | ✗ | ✓ | ✓ |
| Klaim kontribusi framework | ✓ | ✗ | ✗ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Within-subject design tidak dijelaskan di Introduction, padahal penting untuk justifikasi mengapa paired comparison valid. Limitation hanya muncul di Discussion tapi tidak di-address di bagian lain. Klaim kontribusi framework tidak didukung detail metodologi.

**Tindakan perbaikan:**
> 1. Tambahkan penjelasan within-subject design di Introduction sebagai bagian metodologi overview
> 2. Sebutkan limitation di Method untuk transparensi, bukan hanya di Discussion  
> 3. Pastikan klaim kontribusi framework sudah didukung evidence di Method dan Results

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Penelitian ini menggunakan metode eksperimen untuk membandingkan performa aplikasi SRUPUT dengan aplikasi Kopi Reman. Variabel yang diukur adalah waktu penyelesaian tugas dan skor usability menggunakan instrumen SUS. Data dikumpulkan dari 25 responden yang menggunakan kedua aplikasi secara berurutan. Hasil menunjukkan bahwa SRUPUT memiliki performa yang lebih baik dalam kedua aspek tersebut.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Kalimat ke-4 ambigu — "performa yang lebih baik" tidak spesifik, bisa berarti apa saja | Ubah menjadi: "SRUPUT 14% lebih cepat dan mendapat skor SUS 15% lebih tinggi" |
| Precision | "secara berurutan" tidak jelas — apakah random order atau fixed sequence? | Spesifikasi: "dalam urutan yang dirandomisasi untuk menghindari order effect" |
| Conciseness | Kalimat pertama redundan dengan informasi di kalimat kedua | Gabungkan: "Eksperimen within-subject membandingkan time on task dan SUS score..." |

**Paragraf setelah perbaikan:**
> Eksperimen within-subject membandingkan time on task dan SUS score antara aplikasi SRUPUT dan Kopi Reman. Sebanyak 25 responden menggunakan kedua aplikasi dalam urutan yang dirandomisasi untuk menghindari order effect. Hasil menunjukkan SRUPUT 14% lebih cepat (45.2 vs 52.7 detik) dan mendapat skor SUS 15% lebih tinggi (78.5 vs 68.3 poin).

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis "tentang" riset cenderung deskriptif dan kronologis, sedangkan menulis sebagai "argumen" riset membangun logical flow dari masalah ke solusi ke kontribusi. Setiap kalimat harus menopang argumen utama, bukan sekedar melaporkan aktivitas.
> 
> Urutan Method → Discussion → Introduction memastikan claims di Introduction selaras dengan temuan aktual. Ketika menulis Introduction terakhir, kita sudah tahu batasan dan kontribusi riil, sehingga framing menjadi lebih akurat dan tidak over-promise.
