# Landasan Teori UI/UX SRUPUT

## 1. Teori Usability

### 1.1 Nielsen's Usability Principles
Jakob Nielsen mendefinisikan usability sebagai kualitas atribut yang menilai seberapa mudah user interfaces digunakan. Lima komponen usability:

1. **Learnability** - Seberapa mudah pengguna menyelesaikan tugas dasar saat pertama kali melihat desain
2. **Efficiency** - Seberapa cepat pengguna dapat menyelesaikan tugas setelah mempelajari desain
3. **Memorability** - Seberapa mudah pengguna dapat menggunakan kembali desain setelah tidak menggunakannya
4. **Errors** - Berapa banyak error yang dibuat pengguna, seberapa parah, dan seberapa mudah untuk recover
5. **Satisfaction** - Seberapa menyenangkan menggunakan desain tersebut

### 1.2 System Usability Scale (SUS)
SUS adalah kuesioner standar yang dikembangkan oleh John Brooke (1986) untuk mengukur usability. Terdiri dari 10 pertanyaan dengan skala Likert 1-5.

**Interpretasi Skor SUS:**
- < 50: Poor (F)
- 50-60: OK (D)
- 60-70: Good (C)
- 70-80: Excellent (B)
- > 80: Best Imaginable (A)

Rata-rata industri: 68

## 2. Teori Cognitive Load

### 2.1 Cognitive Load Theory (Sweller, 1988)
Teori ini menjelaskan bahwa working memory manusia memiliki kapasitas terbatas. Ada tiga jenis cognitive load:

1. **Intrinsic Load** - Kompleksitas inheren dari tugas itu sendiri
2. **Extraneous Load** - Beban yang tidak perlu yang disebabkan oleh desain interface yang buruk
3. **Germane Load** - Beban yang berkontribusi pada pembelajaran dan schema construction

**Prinsip untuk UI/UX:**
- Minimalisasi extraneous load melalui desain yang clean dan konsisten
- Gunakan chunking untuk mengelola informasi kompleks
- Hindari information overload

## 3. Teori Task Completion Time

### 3.1 Fitts's Law
Waktu untuk mengakses target adalah fungsi dari jarak ke target dan ukuran target:

```
T = a + b × log₂(D/W + 1)
```

Dimana:
- T = waktu untuk move pointer ke target
- D = jarak dari starting point ke target
- W = lebar target
- a, b = konstanta empiris

**Implikasi untuk SRUPUT:**
- Tombol yang sering digunakan harus besar dan mudah dijangkau
- Jarak antara elemen terkait harus diminimalkan
- Touch target minimal 44×44 pixels (Apple HIG) atau 48×48 dp (Material Design)

### 3.2 Hick's Law
Waktu keputusan meningkat secara logaritmik dengan jumlah pilihan:

```
T = b × log₂(n + 1)
```

**Implikasi untuk SRUPUT:**
- Kurangi jumlah pilihan di menu utama
- Gunakan progressive disclosure untuk opsi lanjutan
- Grouping menu berdasarkan kategori

## 4. Information Architecture

### 4.1 Card Sorting & Mental Models
Struktur informasi harus sesuai dengan mental model pengguna tentang bagaimana sistem seharusnya bekerja.

**Untuk Aplikasi Pemesanan Kopi:**
- Home → Browse Menu → Customize → Cart → Payment → Confirmation
- Flow harus linear dan predictable
- Minimize steps untuk reduce cognitive load

### 4.2 Navigation Patterns
**Pattern yang digunakan SRUPUT:**
- Bottom Navigation untuk akses cepat ke section utama
- Tab Bar untuk kategori menu (Coffee, Non-Coffee, Food, Promo)
- FAB (Floating Action Button) untuk Cart yang selalu visible

## 5. Visual Design Principles

### 5.1 Gestalt Principles
- **Proximity** - Elemen yang dekat dianggap related
- **Similarity** - Elemen yang mirip dianggap related
- **Closure** - Otak melengkapi pattern yang tidak lengkap
- **Continuity** - Eye follows lines and paths

**Aplikasi di SRUPUT:**
- Grouping item menu berdasarkan kategori
- Consistent card design untuk setiap menu item
- Visual hierarchy dengan size dan color

### 5.2 Color Psychology
- **Merah/Oranye** - Stimulasi appetite (digunakan untuk CTA buttons)
- **Hijau** - Fresh, healthy (untuk kategori healthy drinks)
- **Coklat** - Warm, comfort (untuk coffee category)

## 6. Mobile-First Design

### 6.1 Responsive Design Principles
- Touch targets minimal 44×44px
- Font size minimal 16px untuk body text
- Spacing adequate untuk prevent misclick
- Thumb-friendly layout (important elements di bottom 1/3 screen)

### 6.2 Progressive Enhancement
Start dengan core functionality, tambahkan enhancement untuk device yang lebih capable:
1. **Base** - Text dan basic navigation
2. **Enhancement** - Images dan styling
3. **Advanced** - Animations dan interactive features

## 7. Framework Evaluasi UI/UX

### 7.1 Metrik Objektif
- **Time on Task** - Waktu untuk menyelesaikan skenario pemesanan
- **Success Rate** - Persentase pengguna yang berhasil complete task
- **Error Rate** - Jumlah error per task
- **Click/Tap Count** - Jumlah interaksi hingga task completion

### 7.2 Metrik Subjektif
- **System Usability Scale (SUS)** - Perceived usability
- **User Satisfaction** - Overall satisfaction rating
- **Net Promoter Score (NPS)** - Likelihood to recommend

## 8. Competitive Analysis Framework

Perbandingan SRUPUT vs Kopi Reman berdasarkan:

| Aspek | SRUPUT (Proposed) | Kopi Reman (Baseline) |
|-------|-------------------|----------------------|
| Navigation | Bottom nav + FAB | Hamburger menu |
| Menu Display | Grid dengan image besar | List dengan image kecil |
| Customization | Inline editor | Separate screen |
| Cart | FAB dengan badge | Hidden di menu |
| Checkout | 2-step (review + payment) | 3-step (review + address + payment) |

## Referensi

1. Nielsen, J. (1993). *Usability Engineering*. Academic Press.
2. Brooke, J. (1996). SUS: A "quick and dirty" usability scale. *Usability Evaluation in Industry*.
3. Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2).
4. Fitts, P. M. (1954). The information capacity of the human motor system. *Journal of Experimental Psychology*, 47(6).
5. Hick, W. E. (1952). On the rate of gain of information. *Quarterly Journal of Experimental Psychology*, 4(1).
6. Apple Inc. (2023). *Human Interface Guidelines*.
7. Google. (2023). *Material Design Guidelines*.
