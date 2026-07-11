# Tahap 1 — Perancangan Arsitektur Context-Aware Collaborative Filtering

**Status:** Selesai  
**Periode:** 15 Januari - 10 Februari 2026

---

## 1. Tujuan Tahap

Merancang arsitektur algoritma Context-Aware Collaborative Filtering yang mengintegrasikan filter spasial geografis untuk meningkatkan akurasi sistem rekomendasi pariwisata, dengan fokus pada:
1. Desain modular yang memisahkan komponen CF dan filter spasial
2. Penentuan parameter konfigurasi optimal
3. Dokumentasi alur algoritma untuk implementasi

---

## 2. Arsitektur Sistem

### 2.1 Komponen Utama

Sistem terdiri dari tiga komponen utama:

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INPUT                               │
│              (user_id, kandidat destinasi)                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│         KOMPONEN 1: COLLABORATIVE FILTERING (BASELINE)      │
│  • Hitung user similarity (cosine similarity)               │
│  • Identifikasi k-nearest neighbors                         │
│  • Prediksi rating untuk semua destinasi                    │
│  • Output: ranked list berdasarkan predicted rating         │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│         KOMPONEN 2: GEOGRAPHIC CONTEXT MODULE               │
│  • Identifikasi destinasi preference user (rating >= 4)     │
│  • Hitung centroid geografis (lat_mean, lon_mean)           │
│  • Hitung jarak setiap kandidat ke centroid (Haversine)     │
│  • Output: distance map untuk setiap destinasi              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│         KOMPONEN 3: SPATIAL FILTER & RE-RANKING             │
│  • Terapkan penalty pada destinasi jauh (> threshold)       │
│  • Hitung final score = predicted_rating - penalty          │
│  • Re-ranking berdasarkan final score                       │
│  • Output: top-N rekomendasi context-aware                  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │  TOP-N LIST  │
                  └──────────────┘
```

### 2.2 Alur Algoritma Detail

#### Step 1: Collaborative Filtering (Baseline)

```
INPUT: User u, Dataset D (user, item, rating)

1. Hitung similarity matrix S menggunakan cosine similarity:
   
   S[u,v] = Σ(r_u,i × r_v,i) / (||r_u|| × ||r_v||)
   
   untuk semua pasangan user (u, v)

2. Identifikasi k-nearest neighbors N(u):
   
   N(u) = top-k users dengan S[u,v] tertinggi

3. Prediksi rating untuk item i yang belum dirating oleh u:
   
   r̂_u,i = r̄_u + [ Σ_{v∈N(u)} S[u,v] × (r_v,i - r̄_v) ] / [ Σ_{v∈N(u)} |S[u,v]| ]
   
   di mana r̄_u adalah mean rating user u

4. Urutkan semua item berdasarkan r̂_u,i (descending)

OUTPUT: List L_baseline = [(item_1, r̂_1), (item_2, r̂_2), ..., (item_n, r̂_n)]
```

#### Step 2: Geographic Context Extraction

```
INPUT: User u, List L_baseline, Dataset D (item, lat, lon)

1. Ambil himpunan destinasi yang disukai user u:
   
   P(u) = {i | r_u,i >= 4.0 dan r_u,i tidak null}

2. Hitung centroid geografis:
   
   lat_centroid = mean({lat_i | i ∈ P(u)})
   lon_centroid = mean({lon_i | i ∈ P(u)})

3. Untuk setiap item i dalam L_baseline, hitung jarak ke centroid:
   
   d_i = Haversine(lat_centroid, lon_centroid, lat_i, lon_i)

OUTPUT: Distance map D_map = {item_i: d_i}
```

#### Step 3: Spatial Filter & Re-ranking

```
INPUT: List L_baseline, Distance map D_map, Threshold T, Penalty weight W

1. Untuk setiap item i dalam L_baseline:
   
   IF d_i <= T:
       penalty_i = 0
   ELSE:
       penalty_i = (d_i - T) × W
   
   final_score_i = r̂_i - penalty_i

2. Urutkan ulang berdasarkan final_score (descending)

OUTPUT: List L_context_aware = [(item_1, score_1), (item_2, score_2), ..., (item_n, score_n)]
```

---

## 3. Formula Haversine

Perhitungan jarak great-circle antara dua titik koordinat geografis:

```
a = sin²(Δφ/2) + cos(φ₁) × cos(φ₂) × sin²(Δλ/2)
c = 2 × atan2(√a, √(1-a))
d = R × c

di mana:
  φ₁, φ₂ = latitude titik 1 dan 2 (radian)
  λ₁, λ₂ = longitude titik 1 dan 2 (radian)
  Δφ = φ₂ - φ₁
  Δλ = λ₂ - λ₁
  R = 6371 km (radius bumi)
  d = jarak (km)
```

**Implementasi Python:**

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

## 4. Parameter Konfigurasi

### 4.1 Parameter yang Ditetapkan

| Parameter | Nilai | Justifikasi |
|---|---|---|
| **k neighbors** | 50 | Berdasarkan literatur Bao et al. (2015) untuk dataset >4000 users. Trade-off antara coverage dan computational cost |
| **Threshold geografis (T)** | 15 km | Jarak maksimal yang masih realistis untuk rute wisata harian di Semarang (berdasarkan rata-rata jarak antar cluster destinasi wisata) |
| **Penalty weight (W)** | 0.1 | Setiap 1 km kelebihan jarak mengurangi 0.1 poin dari predicted rating (tuning empiris: penalty tidak terlalu agresif) |
| **Min rating centroid** | 4.0 | Hanya destinasi yang sangat disukai (rating >= 4) yang dijadikan referensi lokasi preference user |
| **Similarity metric** | Cosine similarity | Standar untuk user-based CF, robust untuk sparse matrix |

### 4.2 Analisis Sensitivitas Parameter (Rencana)

Parameter yang akan diuji variasinya pada tahap implementasi (jika waktu memungkinkan):

- **Threshold geografis:** 10 km, 15 km, 20 km
- **Penalty weight:** 0.05, 0.10, 0.15
- **k neighbors:** 30, 50, 70

Ekspektasi: Threshold 15 km dan penalty 0.1 akan menghasilkan balance terbaik antara akurasi rating dan proximity geografis.

---

## 5. Skema Data

### 5.1 Input Dataset

**Tabel: user_ratings**

| Kolom | Tipe | Deskripsi |
|---|---|---|
| user_id | string | ID pengguna (anonimized) |
| destination_id | string | ID destinasi wisata |
| rating | float | Rating pengguna (1.0-5.0) |

**Tabel: destinations**

| Kolom | Tipe | Deskripsi |
|---|---|---|
| destination_id | string | ID destinasi wisata |
| destination_name | string | Nama destinasi |
| latitude | float | Koordinat latitude |
| longitude | float | Koordinat longitude |
| category | string | Kategori wisata (pantai/heritage/kuliner) |

### 5.2 Output Rekomendasi

**Format:** JSON array

```json
{
  "user_id": "user_12345",
  "algorithm": "context_aware_cf",
  "recommendations": [
    {
      "destination_id": "dest_001",
      "destination_name": "Lawang Sewu",
      "predicted_rating": 4.52,
      "distance_from_centroid": 2.3,
      "penalty": 0.0,
      "final_score": 4.52,
      "rank": 1
    },
    {
      "destination_id": "dest_089",
      "destination_name": "Sam Poo Kong",
      "predicted_rating": 4.48,
      "distance_from_centroid": 4.1,
      "penalty": 0.0,
      "final_score": 4.48,
      "rank": 2
    }
  ]
}
```

---

## 6. Keputusan Desain

### 6.1 Post-filtering vs Pre-filtering vs Contextual Modeling

**Keputusan:** Menggunakan pendekatan **post-filtering**

**Justifikasi:**
- **Modularitas:** Filter spasial dapat diaktifkan/dinonaktifkan tanpa memodifikasi core CF
- **Baseline comparison:** Memungkinkan perbandingan apple-to-apple dengan CF standar (tanpa filter)
- **Interpretability:** Dampak filter spasial terhadap performa dapat diukur secara eksplisit
- **Computational efficiency:** CF hanya dihitung sekali, filter spasial bersifat lightweight

### 6.2 User-based vs Item-based CF

**Keputusan:** Menggunakan **user-based CF**

**Justifikasi:**
- User preference dalam pariwisata cenderung lebih personal dan konsisten
- Dataset memiliki sparse rating per item (banyak destinasi dengan sedikit ulasan)
- User-based lebih cocok untuk domain dengan item diversity tinggi

### 6.3 Centroid Calculation

**Keputusan:** Centroid dihitung berdasarkan **destinasi dengan rating >= 4.0**

**Justifikasi:**
- Rating rendah (1-3) bukan indikasi preferensi lokasi user
- Rating tinggi (4-5) menunjukkan destinasi yang benar-benar disukai dan kemungkinan dikunjungi lagi
- Menghindari noise dari destinasi yang dikunjungi namun tidak disukai

---

## 7. Validitas dan Asumsi

### Asumsi yang Diadopsi:

1. **Koordinat GPS akurat:** Koordinat dari Google Maps diasumsikan akurat dalam radius error < 100 meter
2. **Jarak Euclidean via Haversine cukup:** Tidak mempertimbangkan rute jalan (driving distance), hanya straight-line distance
3. **Preference geografis konsisten:** User yang menyukai destinasi di area tertentu akan cenderung menyukai destinasi lain di area yang sama
4. **Static context:** Konteks geografis bersifat statik (tidak berubah berdasarkan waktu kunjungan)

### Limitasi Desain:

1. Tidak mempertimbangkan konteks temporal (musim, hari libur)
2. Tidak mempertimbangkan accessibility (transportasi publik, jalan rusak)
3. Threshold geografis bersifat global (tidak adaptive per user)

---

## 8. Deliverables Tahap 1

- [x] Dokumentasi arsitektur algoritma (file ini)
- [x] Pseudocode detail untuk ketiga komponen
- [x] Spesifikasi parameter konfigurasi
- [x] Skema data input dan output
- [x] Decision log untuk keputusan desain utama

---

## 9. Next Steps (Tahap 2)

Implementasi algoritma dalam Python:
1. Modul `baseline_cf.py` untuk Collaborative Filtering standar
2. Modul `context_aware_cf.py` untuk algoritma dengan filter spasial
3. Modul `utils.py` untuk fungsi Haversine dan helper functions
4. Unit tests untuk validasi implementasi

---

**Catatan:** Desain arsitektur ini telah direview dan divalidasi pada tanggal 10 Februari 2026. Ready untuk implementasi di Tahap 2.
