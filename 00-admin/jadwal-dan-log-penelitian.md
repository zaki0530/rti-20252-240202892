# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap penelitian sistem rekomendasi pariwisata Context-Aware Collaborative Filtering. Tanggal mengikuti progres aktual pengerjaan.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-01-15 s.d. 2026-02-10 | Tahap 1 | Studi literatur, identifikasi masalah sistem rekomendasi pariwisata, eksplorasi dataset Google Maps Semarang (4.362 ulasan), dan perancangan arsitektur algoritma Context-Aware CF dengan filter spasial Haversine | [09-docs/tahap-1-perancangan-arsitektur.md](../09-docs/tahap-1-perancangan-arsitektur.md) |
| 2026-02-11 s.d. 2026-03-05 | Tahap 2 | Implementasi algoritma Baseline (CF standar) dan algoritma Intervensi (Context-Aware CF dengan filter geografis). Preprocessing dataset, handling missing values (hasil: 0 missing values), normalisasi rating, dan perhitungan matriks similarity | [09-docs/tahap-2-implementasi-algoritma.md](../09-docs/tahap-2-implementasi-algoritma.md) |
| 2026-03-06 s.d. 2026-03-20 | Tahap 3 | Eksekusi eksperimen menggunakan 5-Fold Cross Validation. Pengujian kedua algoritma (Baseline vs Context-Aware CF) pada 4.362 data ulasan destinasi wisata Semarang. Isolasi data leakage menggunakan stratified splitting | [09-docs/tahap-3-eksperimen-validasi.md](../09-docs/tahap-3-eksperimen-validasi.md) |
| 2026-03-21 s.d. 2026-04-10 | Tahap 4 | Analisis hasil eksperimen K-Fold. Perhitungan metrik MAE (Mean Absolute Error). Hasil: Baseline MAE 0.672, Context-Aware CF MAE 0.651. Visualisasi perbandingan error, analisis distribusi rekomendasi geografis, dan pengujian signifikansi statistik | [09-docs/tahap-4-analisis-hasil.md](../09-docs/tahap-4-analisis-hasil.md) |
| 2026-04-11 s.d. 2026-05-15 | Tahap 5 | Penyusunan draf laporan penelitian dan manuskrip jurnal. Dokumentasi metodologi, interpretasi hasil penurunan error 3.13%, validasi hipotesis, dan kesimpulan dampak praktis terhadap rasionalitas rekomendasi rute wisata | [09-docs/tahap-5-dokumentasi-paper.md](../09-docs/tahap-5-dokumentasi-paper.md) |

## Status Ringkas

- Tahap 1–4: Selesai (Eksperimen K-Fold berhasil dieksekusi pada dataset 4.362 ulasan dengan hasil MAE 0.651 untuk Context-Aware CF)
- Tahap 5: Selesai (Draf laporan dan manuskrip final telah tersusun dengan interpretasi hasil yang lengkap)

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Validasi kebersihan dataset Google Maps (4.362 ulasan, 0 missing values)
- [x] Implementasi algoritma Baseline (CF standar) dan Context-Aware CF
- [x] Eksekusi 5-Fold Cross Validation untuk mencegah data leakage
- [x] Perhitungan MAE dan analisis perbandingan error
- [x] Visualisasi distribusi geografis rekomendasi
- [x] Penyusunan draf laporan penelitian lengkap
- [ ] Review akhir format sitasi dan referensi jurnal target
- [ ] Finalisasi abstrak dan kata kunci sesuai template jurnal
- [ ] Proofreading keseluruhan dokumen sebelum submission

## Korespondensi

*(Belum ada — tambahkan catatan korespondensi dengan pembimbing atau editor jurnal di sini saat tersedia)*
