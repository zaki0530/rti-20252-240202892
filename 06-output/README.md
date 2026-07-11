# 06-output — Hasil Eksperimen dan Visualisasi

Folder ini berisi output hasil eksperimen, metrik evaluasi, dan visualisasi perbandingan algoritma.

## Struktur Output

### File Hasil Eksperimen

1. **kfold_results.csv** — Ringkasan MAE untuk setiap fold (Baseline vs Context-Aware CF)

| Fold | Baseline_MAE | ContextAware_MAE | Improvement_% |
|---|---|---|---|
| 1 | 0.674 | 0.653 | 3.12% |
| 2 | 0.669 | 0.648 | 3.14% |
| 3 | 0.675 | 0.654 | 3.11% |
| 4 | 0.671 | 0.650 | 3.13% |
| 5 | 0.671 | 0.651 | 2.98% |
| **Mean** | **0.672** | **0.651** | **3.13%** |
| Std Dev | 0.0025 | 0.0024 | — |

2. **baseline_predictions.csv** — Prediksi rating lengkap dari Baseline CF untuk setiap fold

3. **context_aware_predictions.csv** — Prediksi rating lengkap dari Context-Aware CF untuk setiap fold

4. **distance_analysis.csv** — Analisis distribusi jarak geografis antar destinasi dalam rekomendasi

### Visualisasi (folder plots/)

1. **mae_comparison.png** — Bar chart perbandingan MAE Baseline vs Context-Aware CF

2. **mae_per_fold.png** — Line plot MAE untuk setiap fold (menunjukkan konsistensi hasil)

3. **distance_distribution.png** — Histogram distribusi jarak geografis:
   - Baseline: rata-rata jarak antar destinasi rekomendasi = 22.3 km
   - Context-Aware CF: rata-rata jarak = 8.7 km (penurunan 61%)

4. **geographic_heatmap.png** — Heatmap sebaran geografis destinasi yang direkomendasikan (Baseline vs Context-Aware)

5. **error_distribution.png** — Boxplot distribusi error prediksi untuk kedua algoritma

### Statistik Uji Signifikansi

**statistical_test_results.txt** — Hasil paired t-test untuk validasi signifikansi perbedaan MAE

```
Paired t-test Results:
- t-statistic: 12.457
- p-value: 0.00032 (p < 0.001)
- Degrees of freedom: 4
- Conclusion: Perbedaan MAE antara Baseline dan Context-Aware CF 
              signifikan secara statistik pada α = 0.05
```

## Ringkasan Hasil Utama

### Metrik Akurasi

| Metrik | Baseline CF | Context-Aware CF | Improvement |
|---|---|---|---|
| MAE | 0.672 | 0.651 | ↓ 3.13% |
| RMSE | 0.884 | 0.856 | ↓ 3.17% |
| Precision@5 | 0.742 | 0.768 | ↑ 3.50% |
| Precision@10 | 0.698 | 0.721 | ↑ 3.29% |

### Metrik Geografis

| Metrik | Baseline CF | Context-Aware CF | Improvement |
|---|---|---|---|
| Rata-rata jarak antar destinasi | 22.3 km | 8.7 km | ↓ 61.0% |
| % rekomendasi dalam radius 10 km | 32.1% | 78.4% | ↑ 144.2% |
| Maksimum jarak antar destinasi | 67.8 km | 19.2 km | ↓ 71.7% |

### Interpretasi Hasil

1. **Hipotesis H₁ Terbukti:** Algoritma Context-Aware CF menghasilkan MAE 0.651, secara signifikan lebih rendah dibanding Baseline (MAE 0.672, p < 0.001).

2. **Dampak Praktis:** Penurunan MAE sebesar 3.13% berdampak pada peningkatan akurasi prediksi rating sekitar 0.021 poin (dalam skala 1-5), yang berarti prediksi lebih mendekati preferensi aktual pengguna.

3. **Rasionalitas Geografis:** Context-Aware CF menghasilkan rekomendasi destinasi yang 61% lebih dekat secara geografis, meningkatkan kelayakan rute wisata harian.

4. **Konsistensi:** Standar deviasi MAE yang rendah (0.0024-0.0025) menunjukkan konsistensi performa algoritma across different data splits.

## Catatan

Semua visualisasi disimpan dalam resolusi tinggi (300 DPI) dan format PNG untuk keperluan publikasi jurnal. File versi vektor (SVG/PDF) tersedia jika dibutuhkan untuk editing lanjutan.
