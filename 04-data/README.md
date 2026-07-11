# 04-data — Data Penelitian

Folder ini berisi dataset mentah dan data hasil eksperimen.

## Struktur Data

### Dataset Utama
- **google_maps_semarang_reviews.csv** — Dataset 4.362 ulasan destinasi wisata Semarang dari Google Maps

### Struktur Kolom Dataset:
| Kolom | Tipe | Deskripsi |
|---|---|---|
| user_id | string | ID pengguna (anonimized) |
| destination_id | string | ID destinasi wisata |
| destination_name | string | Nama destinasi |
| rating | float | Rating pengguna (1.0-5.0) |
| latitude | float | Koordinat latitude destinasi |
| longitude | float | Koordinat longitude destinasi |
| review_text | string | Teks ulasan (optional) |
| timestamp | datetime | Waktu ulasan dibuat |

### Data Hasil Eksperimen
- **baseline_predictions.csv** — Hasil prediksi rating algoritma CF standar
- **context_aware_predictions.csv** — Hasil prediksi rating algoritma Context-Aware CF
- **kfold_results.csv** — MAE untuk setiap fold (Baseline vs Context-Aware)
- **distance_analysis.csv** — Analisis distribusi jarak geografis rekomendasi

## Validasi Kualitas Data

- **Total records:** 4.362 ulasan
- **Missing values:** 0 (validated)
- **Unique users:** ~890 pengguna
- **Unique destinations:** ~156 destinasi
- **Rating distribution:**
  - 5 stars: 48.2%
  - 4 stars: 32.7%
  - 3 stars: 12.1%
  - 2 stars: 4.5%
  - 1 star: 2.5%

## Preprocessing yang Diterapkan

1. Penghapusan duplikasi ulasan (berdasarkan user_id + destination_id + timestamp)
2. Validasi konsistensi koordinat geografis (latitude: -7.3 s.d. -6.9, longitude: 110.3 s.d. 110.6)
3. Normalisasi rating ke skala 0-1 untuk perhitungan similarity
4. Validasi missing values pada kolom kritis (user_id, destination_id, rating, lat, lon)

## Catatan Privasi

Dataset telah dianonimisasi. User ID merupakan hash dari ID Google Maps asli untuk melindungi privasi pengguna.
