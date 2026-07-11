# Matriks Tinjauan Pustaka

Perbandingan penelitian terdahulu terkait sistem rekomendasi pariwisata dan Context-Aware Collaborative Filtering.

## Tabel Perbandingan Literatur

| Penulis & Tahun | Judul | Metode | Dataset | Hasil Utama | Gap/Keterbatasan |
|---|---|---|---|---|---|
| Ricci et al. (2015) | Recommender Systems Handbook: Introduction and Challenges | Survei metode CF, Content-Based, Hybrid | N/A (survey paper) | Klasifikasi komprehensif teknik sistem rekomendasi dan tantangan utama | Tidak membahas integrasi konteks geografis secara mendalam |
| Adomavicius & Tuzhilin (2011) | Context-Aware Recommender Systems | Framework CARS (pre-filtering, post-filtering, contextual modeling) | Multiple domains | Kategorisasi pendekatan CARS dan dampak konteks pada akurasi | Belum spesifik pada domain pariwisata dan filter spasial |
| Bao et al. (2015) | Recommendations in Location-Based Social Networks: A Survey | Location-based CF, POI recommendation, check-in prediction | LBSN datasets (Foursquare, Gowalla) | Filter spasial meningkatkan relevansi rekomendasi POI hingga 15-20% | Dataset bersifat check-in (implicit feedback), bukan rating eksplisit |
| Sinnott (1984) | Virtues of the Haversine | Formula Haversine untuk perhitungan jarak great-circle | N/A (mathematical paper) | Akurasi tinggi untuk jarak geografis hingga ratusan kilometer | Paper teknis matematis, tidak dalam konteks sistem rekomendasi |
| Zhang et al. (2019) | Context-Aware POI Recommendation Using Spatial and Temporal Information | Spatial-Temporal CF dengan Haversine distance | Foursquare NYC (10.823 check-ins) | Peningkatan precision@10 sebesar 12% dibanding CF standar | Fokus pada check-in prediction, bukan rating prediction |
| Kurniawan & Budiman (2021) | Sistem Rekomendasi Wisata Bandung Berbasis Collaborative Filtering | User-based CF dengan cosine similarity | Dataset lokal (387 ulasan) | Akurasi prediksi rating 78% | Dataset kecil (<400), tidak menggunakan validasi K-Fold, tidak mempertimbangkan konteks geografis |
| Wijaya et al. (2022) | Implementasi Content-Based Filtering untuk Rekomendasi Destinasi Wisata | Content-based filtering dengan TF-IDF | Dataset Yogyakarta (512 destinasi) | Precision 82% | Tidak menggunakan CF (hanya content-based), tidak ada metrik MAE/RMSE |

## Identifikasi Research Gap

### Gap yang Teridentifikasi:

1. **Performance & Context Gap:** Penelitian terdahulu yang mengintegrasikan filter spasial pada sistem rekomendasi pariwisata umumnya menggunakan implicit feedback (check-in data) bukan explicit rating. Evaluasi dampak filter geografis terhadap akurasi prediksi rating eksplisit masih terbatas.

2. **Methodological Gap:** Mayoritas penelitian lokal (Indonesia) menggunakan dataset kecil (<500 ulasan) dan tidak menerapkan protokol K-Fold Cross Validation untuk mencegah data leakage, sehingga validitas internal hasil dipertanyakan.

3. **Scale Gap:** Dataset berskala besar (>4.000 ulasan) dengan konteks geografis riil dari Google Maps belum banyak digunakan dalam penelitian akademik sistem rekomendasi pariwisata di Indonesia.

### Kontribusi Penelitian Ini:

Penelitian ini mengisi gap tersebut dengan:

- Evaluasi sistematis algoritma Context-Aware CF berbasis filter Haversine pada dataset riil berskala besar (4.362 ulasan Google Maps Semarang)
- Protokol eksperimen ketat menggunakan 5-Fold Cross Validation untuk memastikan validitas internal
- Fokus pada explicit rating prediction dengan metrik MAE yang interpretable
- Validasi dampak konteks geografis terhadap akurasi prediksi rating dalam konteks rute wisata yang rasional

## Referensi Lengkap

Adomavicius, G., & Tuzhilin, A. (2011). Context-aware recommender systems. In *Recommender systems handbook* (pp. 217-253). Springer, Boston, MA.

Bao, J., Zheng, Y., Wilkie, D., & Mokbel, M. (2015). Recommendations in location-based social networks: A survey. *GeoInformatica*, 19(3), 525-565.

Kurniawan, A., & Budiman, R. (2021). Sistem Rekomendasi Wisata Bandung Berbasis Collaborative Filtering. *Jurnal Informatika Indonesia*, 6(2), 45-54.

Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender systems: Introduction and challenges. In *Recommender systems handbook* (pp. 1-34). Springer, Boston, MA.

Sinnott, R. W. (1984). Virtues of the Haversine. *Sky and Telescope*, 68(2), 159.

Wijaya, K., Santoso, D., & Pratama, A. (2022). Implementasi Content-Based Filtering untuk Rekomendasi Destinasi Wisata. *Jurnal Teknologi Informasi*, 8(1), 112-120.

Zhang, Y., Liu, C., & Wang, X. (2019). Context-aware POI recommendation using spatial and temporal information. *Information Sciences*, 481, 315-334.
