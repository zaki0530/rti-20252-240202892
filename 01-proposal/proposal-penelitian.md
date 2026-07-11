# UNIVERSITAS PUTRA BANGSA - KEBUMEN
## PROPOSAL PENELITIAN - RISET TEKNOLOGI INFORMASI
**PENINGKATAN AKURASI SISTEM REKOMENDASI PARIWISATA MENGGUNAKAN CONTEXT-AWARE COLLABORATIVE FILTERING**

Nama: Kayla Putri Arsonisr | NIM: 240202837 | Kelas: 4IKRA

---

# Peningkatan Akurasi Sistem Rekomendasi Pariwisata Semarang Menggunakan Algoritma Context-Aware Collaborative Filtering

## 1. PENDAHULUAN

### 1.1 Latar Belakang

Sistem rekomendasi pariwisata merupakan komponen krusial dalam mendukung pengalaman wisatawan dalam merencanakan rute perjalanan yang optimal. Algoritma Collaborative Filtering (CF) standar telah banyak digunakan untuk memberikan rekomendasi destinasi wisata berdasarkan pola preferensi pengguna serupa. Namun, pendekatan CF konvensional memiliki keterbatasan signifikan dalam konteks rekomendasi pariwisata: algoritma tersebut sering mengabaikan faktor kontekstual geografis, sehingga menghasilkan rekomendasi destinasi yang memiliki rating tinggi namun terpisah jarak puluhan kilometer satu sama lain.

Permasalahan ini berdampak langsung pada rasionalitas perencanaan rute perjalanan wisatawan. Rekomendasi yang tidak mempertimbangkan kedekatan spasial mengakibatkan inefisiensi waktu tempuh, peningkatan biaya transportasi, dan penurunan kepuasan wisatawan. Dalam konteks kota Semarang yang memiliki sebaran destinasi wisata di berbagai wilayah (pesisir, dataran tinggi, dan perkotaan), kebutuhan akan sistem rekomendasi yang context-aware menjadi sangat penting.

Dataset ulasan destinasi wisata dari Google Maps untuk area Semarang yang digunakan dalam penelitian ini terdiri dari 4.362 data ulasan riil pengguna. Dataset tersebut telah divalidasi dan tidak mengandung missing values (0 missing values), sehingga memenuhi standar kualitas data untuk eksperimen akademik yang reliabel.

### 1.2 Konteks Sistem (System Context)

Ruang lingkup penelitian ini dibatasi pada komponen sistem rekomendasi sebagai berikut:

| Komponen | Deskripsi Operasional |
|---|---|
| **Input** | Data ulasan wisata Google Maps (4.362 records), rating pengguna (skala 1-5), koordinat geografis destinasi (latitude, longitude), dan profil preferensi wisatawan |
| **Process** | Algoritma Collaborative Filtering standar (Baseline) dan Context-Aware Collaborative Filtering dengan filter spasial berbasis formula Haversine untuk perhitungan jarak geografis |
| **Output** | Daftar rekomendasi destinasi wisata terurut berdasarkan prediksi rating dengan mempertimbangkan kedekatan geografis |
| **Outcome** | Peningkatan akurasi prediksi rating (penurunan error MAE) dan peningkatan rasionalitas geografis rekomendasi rute wisata |
| **Constraints** | Keterbatasan cakupan geografis (hanya wilayah Semarang), asumsi akurasi koordinat GPS dari Google Maps, dan kompleksitas komputasi perhitungan jarak antar destinasi |
| **Stakeholders** | Wisatawan sebagai pengguna akhir sistem rekomendasi, pengelola destinasi wisata, dan pengembang aplikasi pariwisata digital |

### 1.3 Rumusan Masalah

Sistem rekomendasi pariwisata berbasis Collaborative Filtering standar menghasilkan prediksi yang mengabaikan konteks geografis, sehingga merekomendasikan destinasi dengan rating tinggi namun tersebar secara spasial dengan jarak yang tidak efisien untuk rute perjalanan. Hal ini mengakibatkan penurunan kualitas pengalaman wisatawan dan inefisiensi perencanaan itinerary.

### 1.4 Tujuan Penelitian

Penelitian ini bertujuan untuk mengevaluasi efektivitas algoritma Context-Aware Collaborative Filtering dalam meningkatkan akurasi prediksi rating destinasi wisata dengan mengintegrasikan filter spasial berbasis perhitungan jarak Haversine, serta membandingkan performanya terhadap algoritma Collaborative Filtering standar sebagai baseline.

### 1.5 Research Question (RQ)

**Apakah algoritma Context-Aware Collaborative Filtering yang mengintegrasikan filter spasial geografis menghasilkan nilai Mean Absolute Error (MAE) yang lebih rendah secara signifikan dibandingkan dengan algoritma Collaborative Filtering standar pada dataset ulasan pariwisata Semarang?**

### 1.6 Hipotesis

- **H₀ (Hipotesis Nol):** Tidak terdapat perbedaan signifikan pada nilai Mean Absolute Error (MAE) antara algoritma Collaborative Filtering standar dan algoritma Context-Aware Collaborative Filtering dengan filter spasial.

- **H₁ (Hipotesis Alternatif):** Algoritma Context-Aware Collaborative Filtering dengan filter spasial menghasilkan nilai Mean Absolute Error (MAE) yang lebih rendah secara signifikan dibandingkan dengan algoritma Collaborative Filtering standar.

### 1.7 Threshold Keberhasilan

Keberhasilan intervensi diukur berdasarkan penurunan nilai MAE minimal 2% dari skor baseline. Target yang ditetapkan adalah pencapaian nilai MAE di bawah 0.665 untuk algoritma Context-Aware CF, dengan asumsi baseline CF standar menghasilkan MAE sekitar 0.672.

### 1.8 Baseline dan Intervensi

- **Baseline:** Algoritma Collaborative Filtering standar berbasis user-based similarity menggunakan cosine similarity untuk menghitung kedekatan pola rating antar pengguna, tanpa mempertimbangkan faktor geografis.

- **Intervensi:** Algoritma Context-Aware Collaborative Filtering yang mengintegrasikan filter spasial pada tahap post-processing rekomendasi. Filter spasial menggunakan formula Haversine untuk menghitung jarak geografis antar destinasi, kemudian menerapkan penalty scoring pada destinasi yang berjarak lebih dari threshold tertentu (misal: 15 km) dari centroid destinasi yang telah dikunjungi atau disukai pengguna.

---

## 2. TINJAUAN PUSTAKA

### 2.1 Collaborative Filtering dalam Sistem Rekomendasi

Algoritma Collaborative Filtering merupakan pendekatan yang banyak digunakan dalam sistem rekomendasi karena kemampuannya menangkap pola preferensi implisit dari data interaksi pengguna. Pendekatan user-based CF menghitung similarity antar pengguna berdasarkan pola rating historis, kemudian merekomendasikan item yang disukai oleh pengguna serupa. Namun, CF standar mengabaikan konteks eksternal seperti lokasi geografis (Ricci et al., 2015).

### 2.2 Context-Aware Recommender Systems (CARS)

Context-Aware Recommender Systems memperluas paradigma CF konvensional dengan mengintegrasikan informasi kontekstual seperti waktu, lokasi, dan kondisi lingkungan (Adomavicius & Tuzhilin, 2011). Dalam domain pariwisata, konteks geografis menjadi faktor krusial karena kedekatan spasial mempengaruhi kelayakan rute perjalanan. Penelitian oleh Bao et al. (2015) menunjukkan bahwa integrasi filter spasial dapat meningkatkan relevansi rekomendasi point-of-interest (POI).

### 2.3 Formula Haversine untuk Perhitungan Jarak Geografis

Formula Haversine digunakan untuk menghitung jarak great-circle antara dua titik koordinat geografis (latitude, longitude) pada permukaan bumi. Formula ini mempertimbangkan kelengkungan bumi dan memberikan akurasi tinggi untuk perhitungan jarak hingga ratusan kilometer (Sinnott, 1984). Dalam konteks sistem rekomendasi pariwisata, Haversine memungkinkan filtering destinasi berdasarkan proximity geografis secara efisien.

### 2.4 Research Gap dan Novelty

Kajian literatur menunjukkan bahwa mayoritas penelitian sistem rekomendasi pariwisata di Indonesia masih menggunakan CF standar atau content-based filtering tanpa mempertimbangkan konteks spasial secara eksplisit. Penelitian yang mengintegrasikan filter geografis pada tahap post-processing dengan validasi menggunakan K-Fold Cross Validation untuk mencegah data leakage masih terbatas.

**Research Gap:** Terdapat kesenjangan (Performance & Context Gap) dalam literatur terkait evaluasi sistematis terhadap dampak integrasi filter spasial pada akurasi prediksi rating sistem rekomendasi pariwisata menggunakan dataset riil berskala besar (>4.000 ulasan) dengan isolasi ketat terhadap data leakage.

**Novelty:** Penelitian ini mengisi kesenjangan tersebut dengan mengevaluasi algoritma Context-Aware CF berbasis filter Haversine pada dataset Google Maps Semarang (4.362 ulasan) menggunakan protokol eksperimen 5-Fold Cross Validation yang ketat untuk memastikan validitas internal hasil.

---

## 3. METODOLOGI PENELITIAN

### 3.1 Desain Eksperimen

Penelitian ini menggunakan desain **eksperimen kuantitatif komparatif** dengan membandingkan performa dua algoritma (Baseline vs Intervensi) pada dataset yang identik. Unit analisis adalah prediksi rating destinasi wisata yang dihasilkan oleh masing-masing algoritma.

### 3.2 Definisi Operasional Variabel

- **Independent Variable (IV):** Jenis algoritma rekomendasi (Collaborative Filtering standar vs Context-Aware Collaborative Filtering dengan filter spasial Haversine)

- **Dependent Variable (DV):** Akurasi prediksi rating yang diukur menggunakan metrik Mean Absolute Error (MAE). MAE menghitung rata-rata selisih absolut antara rating aktual dan rating prediksi (skala ratio, satuan: poin rating).

- **Control Variables (CV):** Dataset yang digunakan (4.362 ulasan Google Maps Semarang), metode splitting data (5-Fold Cross Validation dengan stratified sampling), parameter similarity metric (cosine similarity), dan threshold filter geografis (15 km).

### 3.3 Dataset dan Preprocessing

Dataset penelitian terdiri dari 4.362 ulasan riil destinasi wisata Semarang yang dikumpulkan dari Google Maps API. Dataset mencakup atribut:
- User ID (anonimized)
- Destinasi ID
- Rating (skala 1-5)
- Koordinat geografis destinasi (latitude, longitude)
- Timestamp ulasan

**Preprocessing yang dilakukan:**
1. Validasi missing values (hasil: 0 missing values)
2. Normalisasi rating ke skala 0-1
3. Validasi konsistensi koordinat geografis
4. Penghapusan duplikasi ulasan

### 3.4 Implementasi Algoritma

#### 3.4.1 Baseline: Collaborative Filtering Standar

Algoritma user-based CF menggunakan cosine similarity untuk menghitung kedekatan pola rating antar pengguna. Prediksi rating destinasi untuk pengguna target dihitung sebagai weighted average dari rating pengguna serupa.

#### 3.4.2 Intervensi: Context-Aware CF dengan Filter Spasial

Algoritma ini memperluas CF standar dengan menambahkan tahap post-processing filter geografis:

1. Hitung prediksi rating menggunakan CF standar
2. Identifikasi centroid geografis destinasi yang telah dikunjungi/disukai pengguna target
3. Hitung jarak setiap destinasi kandidat rekomendasi terhadap centroid menggunakan formula Haversine
4. Terapkan penalty scoring pada destinasi dengan jarak > threshold (15 km)
5. Re-ranking rekomendasi berdasarkan skor final (prediksi rating - penalty jarak)

### 3.5 Protokol Eksperimen: 5-Fold Cross Validation

Untuk memastikan validitas internal dan mencegah data leakage, eksperimen menggunakan **5-Fold Stratified Cross Validation**:

1. Dataset dibagi menjadi 5 fold dengan distribusi rating yang seimbang
2. Setiap fold digunakan sekali sebagai test set, 4 fold lainnya sebagai training set
3. Kedua algoritma (Baseline dan Intervensi) dilatih dan diuji pada split yang identik
4. MAE dihitung untuk setiap fold
5. Hasil akhir adalah rata-rata MAE dari 5 iterasi

### 3.6 Metrik Evaluasi: Mean Absolute Error (MAE)

MAE digunakan sebagai metrik utama karena interpretabilitasnya yang tinggi dalam konteks prediksi rating:

$$MAE = \frac{1}{n} \sum_{i=1}^{n} |r_{actual,i} - r_{predicted,i}|$$

di mana:
- $n$ = jumlah prediksi
- $r_{actual}$ = rating aktual
- $r_{predicted}$ = rating prediksi

Nilai MAE yang lebih rendah menunjukkan akurasi prediksi yang lebih baik.

### 3.7 Teknik Analisis Data

Analisis dilakukan dengan membandingkan nilai MAE rata-rata dari 5 fold antara Baseline dan Intervensi. Signifikansi perbedaan diuji menggunakan paired t-test dengan tingkat signifikansi α = 0.05.

### 3.8 Mitigasi Bias dan Validitas

- **Data Leakage:** Dicegah melalui stratified K-Fold CV dengan isolasi ketat antara training dan test set
- **Selection Bias:** Seluruh dataset (4.362 ulasan) digunakan tanpa sampling selektif
- **Implementation Bias:** Kedua algoritma diimplementasikan dengan library dan parameter yang konsisten

### 3.9 Keterbatasan Penelitian

1. Cakupan geografis terbatas pada wilayah Semarang
2. Asumsi akurasi koordinat GPS dari Google Maps
3. Tidak mempertimbangkan faktor kontekstual lain (waktu, cuaca, musim)
4. Threshold jarak geografis (15 km) ditetapkan secara empiris

---

## 4. RENCANA JADWAL PELAKSANAAN

| Tahapan Penelitian | Bulan 1 | Bulan 2 | Bulan 3 | Bulan 4 | Bulan 5 |
|---|---|---|---|---|---|
| Studi Literatur & Identifikasi Masalah | ⬛ | | | | |
| Pengumpulan & Preprocessing Dataset | ⬛ | | | | |
| Perancangan Arsitektur Algoritma | | ⬛ | | | |
| Implementasi Baseline & Context-Aware CF | | ⬛ | ⬛ | | |
| Eksekusi Eksperimen K-Fold CV | | | ⬛ | | |
| Analisis Hasil & Perhitungan MAE | | | | ⬛ | |
| Penyusunan Laporan & Manuskrip Jurnal | | | | ⬛ | ⬛ |

---

## 5. REFERENSI

Adomavicius, G., & Tuzhilin, A. (2011). Context-aware recommender systems. In *Recommender systems handbook* (pp. 217-253). Springer.

Bao, J., Zheng, Y., Wilkie, D., & Mokbel, M. (2015). Recommendations in location-based social networks: A survey. *GeoInformatica*, 19(3), 525-565.

Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender systems: Introduction and challenges. In *Recommender systems handbook* (pp. 1-34). Springer.

Sinnott, R. W. (1984). Virtues of the Haversine. *Sky and Telescope*, 68(2), 159.
