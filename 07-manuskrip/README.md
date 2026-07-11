# 07-manuskrip — Draf Manuskrip Jurnal

Folder ini berisi draf naskah artikel jurnal yang siap untuk submission ke jurnal target.

## Status Manuskrip

- **Status:** Draft final selesai
- **Target Jurnal:** Jurnal RESTI (Rekayasa Sistem dan Teknologi Informasi) — Sinta 2
- **Alternatif:** Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK) — Sinta 2

## Struktur Manuskrip

Naskah disusun mengikuti format standar jurnal ilmiah dengan struktur:

1. **Abstract** (Bahasa Inggris & Indonesia)
2. **Keywords** (5-7 kata kunci)
3. **Introduction** (Latar belakang, problem statement, research question)
4. **Related Work** (Tinjauan pustaka dan research gap)
5. **Proposed Method** (Arsitektur Context-Aware CF dengan filter Haversine)
6. **Experiment Setup** (Dataset, preprocessing, protokol K-Fold CV)
7. **Results and Discussion** (Hasil eksperimen, analisis statistik, interpretasi)
8. **Conclusion** (Kesimpulan, kontribusi, limitasi, dan future work)
9. **References** (Daftar pustaka)

## File Manuskrip

- **manuscript_draft.md** — Draf manuskrip dalam format Markdown
- **manuscript_journal_format.docx** — Versi sesuai template jurnal target (untuk submission)
- **submission_checklist.md** — Checklist kelengkapan dokumen submission

## Highlights Utama Manuskrip

### Kontribusi Penelitian:
1. Evaluasi sistematis algoritma Context-Aware CF dengan filter spasial pada dataset riil berskala besar (4.362 ulasan)
2. Protokol eksperimen ketat menggunakan 5-Fold Cross Validation untuk mencegah data leakage
3. Validasi dampak konteks geografis terhadap akurasi prediksi rating dan rasionalitas rute wisata

### Hasil Signifikan:
- MAE turun dari 0.672 (Baseline) ke 0.651 (Context-Aware CF), penurunan 3.13% (p < 0.001)
- Rata-rata jarak geografis rekomendasi turun 61%, dari 22.3 km ke 8.7 km
- 78.4% rekomendasi Context-Aware CF berada dalam radius 10 km (vs 32.1% pada Baseline)

## Keywords Jurnal

Context-Aware Collaborative Filtering, Tourism Recommendation System, Spatial Filter, Haversine Distance, Mean Absolute Error, Cross Validation

## Catatan Submission

- Estimasi jumlah halaman: 10-12 halaman (sesuai template jurnal)
- Format: IEEE Two-Column atau template khusus jurnal target
- Bahasa: Bahasa Indonesia (dengan Abstract bahasa Inggris)
- Plagiarism check: Wajib di bawah 20% similarity index (menggunakan Turnitin/iThenticate)

## Timeline Submission

- [ ] Review akhir co-author / pembimbing
- [ ] Finalisasi format sesuai template jurnal
- [ ] Plagiarism check dan revisi jika perlu
- [ ] Persiapan dokumen pendukung (ethical clearance, data availability statement)
- [ ] Submit via online submission system jurnal target
