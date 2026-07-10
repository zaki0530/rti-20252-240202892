# 06-output

Hasil olahan data & visualisasi — hasil analisis statistik.

Dihasilkan oleh `05-kode/analysis_ttest.py` dan skrip visualisasi lainnya dari data mentah `04-data/`.

## tables/

| File | Isi |
|---|---|
| `statistical_test_results.csv` | Hasil paired t-test untuk time on task dan SUS score (mean±std, t-stat, p-value, Cohen's d, CI 95%) |
| `descriptive_stats.csv` | Statistik deskriptif per aplikasi (mean, median, std, min, max, n) |
| `sus_breakdown.csv` | Breakdown jawaban SUS per pertanyaan untuk analisis mendalam |

## figures/

| File | Isi |
|---|---|
| `fig_time_comparison.png` | Box plot time on task: SRUPUT vs Kopi Reman |
| `fig_sus_comparison.png` | Bar chart SUS score dengan error bars |
| `fig_scatter_time_vs_sus.png` | Scatter plot korelasi time on task vs SUS score |
| `fig_distribution_histogram.png` | Histogram distribusi untuk uji normalitas |

## Acuan

Analisis mengikuti rencana di: [../worksheets/ws-14-analysis-interpretation.md](../../worksheets/ws-14-analysis-interpretation.md)
