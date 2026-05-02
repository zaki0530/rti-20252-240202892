# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : ____________________
  Konteks  : ____________________

System Context
  Input       : ____________________
  Process     : ____________________
  Output      : ____________________
  Outcome     : ____________________
  Constraints : ____________________
  Stakeholders: ____________________

Fenomena → Problem
  Fenomena yang diamati             : ____________________
  Gejala (symptom) yang terukur     : ____________________
  Masalah yang didiagnosis          : ____________________
  Masalah riset (researchable)      : ____________________
  Variabel yang terukur             : ____________________

Problem Quality Check
  [ ] Clarity — Apakah satu orang membaca akan paham?
  [ ] Measurability — Apakah ada metrik kuantitatif?
  [ ] Relevance — Apakah penting untuk domain?
  [ ] Testability — Apakah bisa gagal?
  [ ] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  ____________________
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** ________________________________________

| Tahap | Hasil |
|-------|-------|
| Reality | *Pelanggan di kedai kopi sering mengalami penumpukan antrean manual di meja kasir* |
| Observed Issue (Symptom) | *Waktu tunggu dari datang hingga pesanan diproses rata-rata >10 menit; tingkat pembatalan pesanan saat antrean panjang mencapai 15%* |
| Diagnosed Problem (Root Cause) |Kurangnya media pemesanan mandiri (self-order) yang efisien dan UI/UX aplikasi yang ada (jika ada) terlalu rumit bagi pengguna baru |
| Researchable Problem |Bagaimana merancang antarmuka aplikasi pemesanan yang mampu meminimalkan cognitive load pengguna sehingga proses pemesanan selesai dalam <2 menit? |
| Measurable Variable |Skor SUS,waktu menyelesaikan pesanan, dan Success Rate (persentase pesanan berhasil tanpa bantuan). |

**Apakah terjebak solution-first thinking?** [ ] Ya / [x] Tidak
> Jika ya, kembali ke tahap mana? _Kita fokus pada masalah antrean dan beban kognitif, bukan sekadar "ingin buat aplikasi_______________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | *Kita fokus pada masalah antrean dan beban kognitif, bukan sekadar "ingin buat aplikasi* |
| Process |Alur Design Thinking, navigasi menu, pemrosesan pesanan, dan validasi pembayaran. |
| Output |Prototipe high-fidelity (Figma), invoice digital, dan notifikasi status pesanan |
| Outcome |Berkurangnya kepadatan antrean fisik di kedai dan peningkatan kenyamanan transaksi pelanggan |
| Constraints |Keterbatasan ukuran layar smartphone, variasi kemampuan literasi digital pengguna di Kebumen. |
| Stakeholders | Pemilik Kedai , Barista (sebagai penerima pesanan), dan Pelanggan (User)|

**Komponen mana yang paling relevan dengan masalah riset?** Proses navigasi dalam aplikasi yang harus tetap mudah di bawah batasan layar kecil dan user yang beragam

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | *5 — Fokus pada hambatan antrean & solusi UI/UX sangat spesifi* | |
| Measurability |4|Terukur lewat skor SUS (target >68) dan task completion time |
| Relevance |5|Solusi digital sangat dibutuhkan untuk efisiensi UMKM retail. |
| Testability |5|Bisa dibuktikan melalui pengujian langsung ke calon pengguna |
| Impact |4|Berpotensi meningkatkan omzet kedai melalui layanan yang cepat |

**Skor total:** 23/ 25

**Problem statement versi final (1 paragraf):**
>Penumpukan antrean manual di Kedai menghambat efisiensi pelayanan. Penelitian ini bertujuan merancang UI/UX aplikasi mobile menggunakan metode Design Thinking untuk menciptakan alur pemesanan mandiri yang cepat dan mudah digunakan, yang divalidasi menggunakan metrik System Usability Scale (SUS)

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Fokus pada perbaikan fungsional agar sistem
> Fokus pada pembuktian efektivitas dan pencarian pengetahuan baru melalui data
