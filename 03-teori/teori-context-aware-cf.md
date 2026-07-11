# Landasan Teori: Context-Aware Collaborative Filtering untuk Sistem Rekomendasi Pariwisata

## 1. Collaborative Filtering (CF)

### 1.1 Definisi

Collaborative Filtering merupakan teknik sistem rekomendasi yang memprediksi preferensi pengguna berdasarkan pola interaksi pengguna serupa. CF berasumsi bahwa pengguna yang memiliki pola rating serupa di masa lalu akan memiliki preferensi serupa di masa depan.

### 1.2 User-Based Collaborative Filtering

Pendekatan yang digunakan dalam penelitian ini adalah **user-based CF**, yang terdiri dari tahapan:

1. **Perhitungan Similarity:** Mengukur kedekatan pola rating antar pengguna menggunakan cosine similarity:

$$sim(u, v) = \frac{\sum_{i \in I_{uv}} r_{u,i} \cdot r_{v,i}}{\sqrt{\sum_{i \in I_{uv}} r_{u,i}^2} \cdot \sqrt{\sum_{i \in I_{uv}} r_{v,i}^2}}$$

di mana:
- $u, v$ = pengguna yang dibandingkan
- $I_{uv}$ = himpunan item yang telah dirating oleh kedua pengguna
- $r_{u,i}$ = rating pengguna $u$ pada item $i$

2. **Identifikasi Neighbors:** Memilih top-k pengguna dengan similarity tertinggi terhadap pengguna target.

3. **Prediksi Rating:** Menghitung weighted average dari rating neighbors:

$$\hat{r}_{u,i} = \bar{r}_u + \frac{\sum_{v \in N(u)} sim(u,v) \cdot (r_{v,i} - \bar{r}_v)}{\sum_{v \in N(u)} |sim(u,v)|}$$

di mana:
- $\hat{r}_{u,i}$ = prediksi rating pengguna $u$ pada item $i$
- $\bar{r}_u$ = rata-rata rating pengguna $u$
- $N(u)$ = himpunan neighbors pengguna $u$

### 1.3 Keterbatasan CF Standar dalam Domain Pariwisata

CF standar tidak mempertimbangkan konteks eksternal seperti:
- Kedekatan geografis antar destinasi
- Waktu kunjungan (musim, hari kerja/libur)
- Karakteristik demografis wisatawan

Dalam konteks pariwisata, keterbatasan ini mengakibatkan rekomendasi destinasi yang terpisah jarak jauh, sehingga tidak praktis untuk perencanaan rute.

---

## 2. Context-Aware Recommender Systems (CARS)

### 2.1 Definisi Konteks

Konteks didefinisikan sebagai informasi tambahan yang relevan dengan situasi interaksi pengguna-item. Dalam domain pariwisata, konteks mencakup:
- **Konteks spasial:** lokasi geografis destinasi
- **Konteks temporal:** waktu kunjungan
- **Konteks sosial:** komposisi rombongan wisatawan

### 2.2 Pendekatan Context-Aware

Terdapat tiga pendekatan utama mengintegrasikan konteks dalam sistem rekomendasi:

1. **Contextual Pre-filtering:** Menyaring data berdasarkan konteks sebelum membangun model
2. **Contextual Post-filtering:** Membangun model tanpa konteks, kemudian menyaring hasil berdasarkan konteks
3. **Contextual Modeling:** Mengintegrasikan konteks langsung ke dalam algoritma rekomendasi

Penelitian ini menggunakan pendekatan **post-filtering** dengan menerapkan filter spasial pada hasil rekomendasi CF standar.

---

## 3. Formula Haversine untuk Perhitungan Jarak Geografis

### 3.1 Definisi

Formula Haversine digunakan untuk menghitung jarak great-circle antara dua titik koordinat pada permukaan bola (bumi). Formula ini mempertimbangkan kelengkungan bumi dan memberikan akurasi tinggi untuk jarak hingga ratusan kilometer.

### 3.2 Formula Matematis

$$a = \sin^2\left(\frac{\Delta\phi}{2}\right) + \cos(\phi_1) \cdot \cos(\phi_2) \cdot \sin^2\left(\frac{\Delta\lambda}{2}\right)$$

$$c = 2 \cdot \text{atan2}\left(\sqrt{a}, \sqrt{1-a}\right)$$

$$d = R \cdot c$$

di mana:
- $\phi_1, \phi_2$ = latitude titik 1 dan 2 (dalam radian)
- $\lambda_1, \lambda_2$ = longitude titik 1 dan 2 (dalam radian)
- $\Delta\phi = \phi_2 - \phi_1$
- $\Delta\lambda = \lambda_2 - \lambda_1$
- $R$ = radius bumi (6.371 km)
- $d$ = jarak antara dua titik (km)

### 3.3 Implementasi dalam Python

```python
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius bumi dalam km
    
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi/2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    distance = R * c
    return distance
```

---

## 4. Arsitektur Context-Aware CF dengan Filter Spasial

### 4.1 Alur Algoritma

```
INPUT: User u, Dataset D (user, item, rating, lat, lon)

STEP 1: Collaborative Filtering Standar
  1.1 Hitung similarity matrix antar pengguna (cosine similarity)
  1.2 Identifikasi top-k neighbors untuk user u
  1.3 Prediksi rating untuk semua item yang belum dirating oleh u
  1.4 Urutkan item berdasarkan prediksi rating (descending)

STEP 2: Identifikasi Centroid Geografis User Preference
  2.1 Ambil himpunan destinasi yang telah dirating tinggi (>= 4) oleh user u
  2.2 Hitung centroid geografis:
      lat_centroid = mean(lat_1, lat_2, ..., lat_n)
      lon_centroid = mean(lon_1, lon_2, ..., lon_n)

STEP 3: Filter Spasial (Post-filtering)
  3.1 Untuk setiap item i dalam rekomendasi CF:
      distance_i = haversine(lat_centroid, lon_centroid, lat_i, lon_i)
  3.2 Hitung penalty score:
      penalty_i = 0 jika distance_i <= threshold (15 km)
      penalty_i = (distance_i - threshold) * weight jika distance_i > threshold
  3.3 Hitung final score:
      score_final_i = predicted_rating_i - penalty_i

STEP 4: Re-ranking
  4.1 Urutkan item berdasarkan score_final (descending)
  4.2 Return top-N rekomendasi

OUTPUT: Daftar top-N destinasi dengan mempertimbangkan rating & proximity
```

### 4.2 Parameter Konfigurasi

| Parameter | Nilai | Justifikasi |
|---|---|---|
| k neighbors | 50 | Keseimbangan antara akurasi dan coverage |
| Threshold geografis | 15 km | Jarak maksimal rute wisata dalam satu hari di Semarang |
| Penalty weight | 0.1 | Mengurangi 0.1 poin rating per 1 km kelebihan jarak |
| Minimum rating centroid | 4.0 | Hanya destinasi yang disukai tinggi yang menjadi referensi lokasi |

---

## 5. Metrik Evaluasi: Mean Absolute Error (MAE)

### 5.1 Definisi

MAE mengukur rata-rata selisih absolut antara rating aktual dan rating prediksi. Metrik ini dipilih karena:
- Interpretable: nilai MAE 0.65 berarti rata-rata error prediksi adalah 0.65 poin rating
- Robust terhadap outlier dibanding RMSE
- Standar dalam evaluasi sistem rekomendasi

### 5.2 Formula

$$MAE = \frac{1}{|T|} \sum_{(u,i) \in T} |r_{u,i} - \hat{r}_{u,i}|$$

di mana:
- $T$ = test set
- $r_{u,i}$ = rating aktual pengguna $u$ pada item $i$
- $\hat{r}_{u,i}$ = rating prediksi

### 5.3 Interpretasi

- MAE < 0.5: Akurasi sangat baik
- MAE 0.5-0.7: Akurasi baik
- MAE 0.7-1.0: Akurasi cukup
- MAE > 1.0: Akurasi rendah

Target penelitian ini adalah MAE < 0.665 untuk algoritma Context-Aware CF.

---

## 6. Cross Validation untuk Mencegah Data Leakage

### 6.1 5-Fold Cross Validation

Dataset dibagi menjadi 5 subset (fold) dengan proporsi seimbang. Iterasi dilakukan 5 kali:

```
Iterasi 1: Train [Fold 2,3,4,5] → Test [Fold 1] → MAE_1
Iterasi 2: Train [Fold 1,3,4,5] → Test [Fold 2] → MAE_2
Iterasi 3: Train [Fold 1,2,4,5] → Test [Fold 3] → MAE_3
Iterasi 4: Train [Fold 1,2,3,5] → Test [Fold 4] → MAE_4
Iterasi 5: Train [Fold 1,2,3,4] → Test [Fold 5] → MAE_5

MAE_final = (MAE_1 + MAE_2 + MAE_3 + MAE_4 + MAE_5) / 5
```

### 6.2 Stratified Splitting

Untuk memastikan distribusi rating seimbang di setiap fold, digunakan stratified splitting berdasarkan kategori rating (1-2: rendah, 3: sedang, 4-5: tinggi).

### 6.3 Pencegahan Data Leakage

Prinsip ketat yang diterapkan:
- **Tidak ada informasi dari test set digunakan pada tahap training**
- Normalisasi dan statistik dihitung hanya dari training set
- Centroid geografis user dihitung hanya dari rating dalam training set
- Similarity matrix dibangun hanya dari interaksi dalam training set

---

## Referensi Teori

Adomavicius, G., & Tuzhilin, A. (2011). Context-aware recommender systems. In *Recommender systems handbook* (pp. 217-253). Springer.

Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender systems: Introduction and challenges. In *Recommender systems handbook* (pp. 1-34). Springer.

Sinnott, R. W. (1984). Virtues of the Haversine. *Sky and Telescope*, 68(2), 159.
