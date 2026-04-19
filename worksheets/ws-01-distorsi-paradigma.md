# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Abu Zaki
Tanggal          : 19 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: "Berapa jumlah total sampel yang digunakan dan apakah kondisi pengujiannya mencerminkan realitas di lapangan?"
   - Data yang dibutuhkan untuk verifikasi: Metrik performa mentah, distribusi demografi responden, dan detail lingkungan eksperimen (misal: spesifikasi perangkat/jaringan).

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [X] Design Science  [ ] Mixed
   - Alasan: Fokus riset saya adalah menciptakan solusi praktis berupa artefak (prototipe aplikasi SRUPUT) untuk memecahkan masalah antrean di kedai kopi.

3. Identifikasi distorsi:
   - Asumsi tersembunyi: Mengasumsikan bahwa pengguna yang mahir teknologi (mahasiswa) mewakili seluruh spektrum calon pengguna aplikasi.
   - Sumber bias potensial: Sampling bias karena pemilihan responden yang terbatas dan Social Desirability Bias (responden cenderung memberi nilai bagus karena mengenal peneliti).
   - Langkah mitigasi: Melakukan pengujian kepada kelompok usia yang lebih luas dan menggunakan teknik "blind testing" di mana responden tidak tahu siapa pembuat aplikasinya.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Skor asli dari kuesioner System Usability Scale (SUS) dan feedback negatif dari pengguna saat tahap testing.
   - Batasan yang diakui sejak awal: Keterbatasan jumlah responden (hanya 10 orang) dan fokus penelitian yang hanya mencakup wilayah geografis tertentu (Kebumen).
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul:Penerapan UI/UX Menggunakan Metode Design Thinking Pada Aplikasi Coffee Shop Sruput Berbasis Mobile
> Penulis (Tahun):Muhammad Hafidh Hilmi Al Fikri, dkk. (2025)
> Sumber/Link DOI:https://ejournal.itn.ac.id/jati/article/view/13644/7723

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Melakukan observasi dan wawancara kepada pelanggan di kedai kopi wilayah Kebumen untuk mengumpulkan keluhan antrean manual | Sampling Bias: Responden mungkin didominasi oleh kalangan mahasiswa/rekan peneliti, sehingga belum tentu mewakili pelanggan dari kelompok usia lebih tua |
| Data → Processing |Menyusun Empathy Map, User Persona, dan Customer Journey Map dari hasil wawancara |Interpretation Bias: Peneliti mungkin menyederhanakan profil pengguna (Persona) agar sesuai dengan solusi fitur yang sudah direncanakan sebelumnya |
| Processing → Analysis |Membuat prototipe di Figma dan mengujinya menggunakan kuesioner System Usability Scale (SUS) kepada 10 responden |Social Desirability Bias: Responden mungkin memberikan skor tinggi karena merasa sungkan terhadap peneliti, bukan murni karena fungsionalitas aplikasi |
| Analysis → Inference |Menghitung rata-rata skor SUS sebesar 80,25 dan menyimpulkan kategori "Excellent" |Construct Validity: Skor SUS pada prototipe statis mungkin tidak mencerminkan pengalaman nyata jika aplikasi sudah memiliki kendala teknis seperti lag jaringan |
| Inference → Knowledge |Menyarankan penggunaan metode Design Thinking sebagai solusi efektif untuk pengembangan aplikasi retail kopi |Overgeneralization: Keberhasilan pada satu studi kasus di Kebumen dianggap berlaku secara universal untuk semua skala bisnis kopi |

**Distorsi paling besar di tahap:** Reality → Data

**Dua distorsi spesifik yang teridentifikasi:**
1. Jumlah Responden Terbatas: Pengujian hanya dilakukan pada 10 orang, yang secara statistik mungkin belum cukup kuat untuk menggeneralisasi kepuasan seluruh pengguna aplikasi
2. Konteks Lokal: Penelitian terfokus pada pengguna di Kebumen, sehingga pola perilaku pemesanan mungkin berbeda jika diterapkan di kota besar dengan budaya kopi yang berbeda

---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Menghapus outlier hanya agar hasil terlihat signifikan adalah bentuk manipulasi data yang melanggar integritas akademik |
| Transparansi |Peneliti wajib melaporkan semua data, termasuk anomali, karena outlier bisa jadi memberikan wawasan penting tentang kegagalan sistem |
| Peer review |Jika data dimanipulasi, peneliti lain tidak akan bisa mereproduksi (reproducible) hasil yang sama, sehingga kepercayaan terhadap riset tersebut hilang |

**Keputusan akhir dan justifikasi:**
> Peneliti harus tetap melaporkan hasil dengan menyertakan outlier tersebut. Justifikasi: Kegagalan atau anomali data tetap merupakan kontribusi pengetahuan (negative result) yang valid dalam riset IT

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Pengembangan UI/UX Aplikasi Mobile menggunakan Design Thinkin

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 — Karena riset ini menggunakan pengujian objektif melalui skor SUS (System Usability Scale) untuk mengukur tingkat keberhasilan desain secara numerik | 2 — Meskipun ada tahap wawancara, fokus utama riset bukan untuk mendalami makna sosial yang mendalam, melainkan hanya sebagai masukan desain | 5 — Karena tujuan utama riset adalah membangun sebuah artefak (prototipe desain aplikasi) yang bertujuan memecahkan masalah praktis yaitu antrean di kedai kopi |
| Jenis data yang dikumpulkan | Skor kuesioner SUS (numerik) dan tingkat keberhasilan tugas | Catatan wawancara mendalam mengenai perasaan pengguna | Hasil pengujian artefak berupa prototipe aplikasi di Figma. |
| Limitasi paradigma |Angka tidak selalu menjelaskan mengapa pengguna merasa bingung |Hasil sulit digeneralisasi karena sangat bergantung pada konteks individu |Fokus pada "apakah sistem bekerja", bukan pada teori dasar yang mendalam |

**Paradigma yang dipilih:** Design Science Research (DSR)
**Alasan:** Riset ini berfokus pada pembangunan sebuah artefak (prototipe aplikasi SRUPUT) untuk memecahkan masalah praktis (antrean kopi) dan menguji efektivitas artefak tersebut melalui pengujian langsung

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
>Dulu saya langsung percaya pada angka seperti "SUS 84,25". Sekarang, saya akan mempertanyakan: Siapa respondennya? Apakah alat ukurnya valid? Dan apakah hasilnya bisa diterapkan di tempat lain? Saya belajar bahwa data bagus di atas kertas belum tentu sukses di lapangan jika prosesnya bias.