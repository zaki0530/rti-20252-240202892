# 04-data

Data mentah hasil pengujian usability — output dari eksperimen, input untuk analisis statistik.

## Isi yang diharapkan

- Hasil pengujian time on task dalam format CSV, per responden × aplikasi (SRUPUT/Kopi Reman) × skenario (simple/complex)
- Hasil kuesioner SUS dalam format CSV, per responden × aplikasi
- Metadata eksekusi tiap session (timestamp, urutan aplikasi, demografi responden)
- Catatan observasi selama pengujian (errors, hesitations, comments)

## Struktur Data

```
04-data/
├── time_on_task.csv         # Waktu penyelesaian tugas
├── sus_responses.csv         # Jawaban SUS per responden
├── demographics.csv          # Data demografi responden
├── task_success_rate.csv    # Success rate per skenario
└── observation_notes.md      # Catatan kualitatif
```

## Catatan

Data di folder ini bersifat mentah (raw) dan belum diolah. Hasil olahan (statistik, grafik) disimpan di [../06-output/](../06-output/).
