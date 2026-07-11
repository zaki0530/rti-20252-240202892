# 05-kode — Source Code Penelitian

Folder ini berisi implementasi algoritma dan skrip analisis data.

## Struktur Kode

### File Utama

1. **baseline_cf.py** — Implementasi algoritma Collaborative Filtering standar (user-based dengan cosine similarity)

2. **context_aware_cf.py** — Implementasi algoritma Context-Aware CF dengan filter spasial Haversine

3. **kfold_experiment.py** — Skrip eksekusi eksperimen 5-Fold Cross Validation untuk kedua algoritma

4. **evaluation.py** — Modul perhitungan metrik evaluasi (MAE, RMSE, Precision@K)

5. **preprocessing.py** — Skrip preprocessing dataset (validasi missing values, normalisasi, stratified splitting)

6. **visualization.py** — Skrip visualisasi hasil (perbandingan MAE, distribusi geografis, heatmap)

7. **utils.py** — Fungsi utilitas (haversine distance, load data, save results)

### File Konfigurasi

- **requirements.txt** — Dependensi Python yang dibutuhkan
- **config.yaml** — Konfigurasi parameter eksperimen (k neighbors, threshold geografis, dll.)

## Cara Menjalankan Eksperimen

### 1. Setup Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Preprocessing Data

```bash
python preprocessing.py --input ../04-data/google_maps_semarang_reviews.csv --output ../04-data/preprocessed_data.csv
```

### 3. Eksekusi Eksperimen K-Fold

```bash
python kfold_experiment.py --data ../04-data/preprocessed_data.csv --folds 5 --output ../06-output/
```

Skrip ini akan:
- Membagi dataset menjadi 5 fold dengan stratified sampling
- Melatih dan menguji Baseline CF pada setiap fold
- Melatih dan menguji Context-Aware CF pada setiap fold
- Menyimpan hasil prediksi dan MAE ke folder `06-output/`

### 4. Visualisasi Hasil

```bash
python visualization.py --results ../06-output/kfold_results.csv --output ../06-output/plots/
```

## Spesifikasi Teknis

- **Python:** 3.8+
- **Library utama:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn
- **Computational environment:** CPU (tidak memerlukan GPU)
- **Estimasi waktu eksekusi:** ~15-20 menit untuk full 5-Fold CV pada dataset 4.362 ulasan

## Parameter Konfigurasi (config.yaml)

```yaml
collaborative_filtering:
  k_neighbors: 50
  similarity_metric: cosine
  min_common_items: 3

context_aware:
  geo_threshold_km: 15
  penalty_weight: 0.1
  min_rating_centroid: 4.0

cross_validation:
  n_folds: 5
  stratify: true
  random_seed: 42

evaluation:
  metrics:
    - mae
    - rmse
    - precision_at_5
    - precision_at_10
```

## Dokumentasi Kode

Setiap modul dilengkapi dengan docstring lengkap yang menjelaskan:
- Tujuan fungsi/kelas
- Parameter input dan output
- Contoh penggunaan
- Referensi teori (jika applicable)

Untuk detail implementasi, lihat komentar inline pada masing-masing file source code.
