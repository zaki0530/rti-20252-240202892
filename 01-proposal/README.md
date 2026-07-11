# 01-proposal — Proposal Penelitian

Folder ini berisi dokumen proposal penelitian lengkap yang telah disusun sesuai format akademik.

## Isi Folder

- **proposal-penelitian.md** — Dokumen proposal lengkap mencakup pendahuluan, tinjauan pustaka, metodologi, rencana jadwal, dan referensi

## Ringkasan Proposal

**Judul:** Peningkatan Akurasi Sistem Rekomendasi Pariwisata Semarang Menggunakan Algoritma Context-Aware Collaborative Filtering

**Masalah:** Sistem rekomendasi CF standar mengabaikan konteks geografis, menghasilkan rekomendasi destinasi yang terpisah puluhan kilometer (tidak efisien untuk rute wisata)

**Solusi:** Integrasi filter spasial berbasis Haversine ke dalam algoritma CF untuk mempertimbangkan kedekatan geografis destinasi

**Metode:** 5-Fold Cross Validation pada dataset 4.362 ulasan Google Maps Semarang

**Metrik:** Mean Absolute Error (MAE)

**Target:** Penurunan MAE minimal 2% dari baseline (target MAE < 0.665)
