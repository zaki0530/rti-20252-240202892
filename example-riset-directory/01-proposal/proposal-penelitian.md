UNIVERSITAS PUTRA BANGSA - KEBUMEN
TUGAS PROPOSAL PENELITIAN UTS - RISET TEKNOLOGI INFORMASI PERANCANGAN UI/UX APLIKASI MOBILE PEMESANAN MANDIRI KEDAI KOPI MENGGUNAKAN METODE DESIGN THINKING
Nama: Abu Zaki | NIM: 240202892 | Kelas: 4IKRA


Perancangan Interaksi Antarmuka (UI/UX) Aplikasi Mobile Self-Ordering Pada Kedai Kopi
Menggunakan Metode Design Thinking Untuk Optimalisasi Efisiensi Transaksi (Studi Kasus: Kedai Kopi SRUPUT Kebumen)

Usulan tugas penelitian ini bertujuan untuk mengatasi permasalahan penumpukan antrean fisik pelanggan pada jam sibuk (peak hours) di Kedai Kopi SRUPUT, Kebumen. Masalah inefisiensi ini berdampak negatif pada kelancaran transaksi kasir serta memicu tingkat pembatalan pesanan konsumen mencapai 15%. Solusi yang diajukan dalam pemenuhan tugas mata kuliah Riset Teknologi Informasi ini adalah perancangan prototipe aplikasi mobile self-ordering bernama "SRUPUT" dengan fokus optimasi pada bagian modul Cart & Payment. Pemodelan sistem interaksi ini dieksekusi menggunakan metode Design Thinking (Empathize, Define, Ideate, Prototype, dan Test).
Skenario pengujian dijalankan melalui studi perbandingan terkontrol (Controlled Comparison Study) untuk membandingkan aspek interaksi aplikasi SRUPUT terhadap aplikasi pembanding riil dari literatur ilmiah terdahulu, yaitu aplikasi "Kopi Reman" (Al Fikri dkk., 2024). Perubahan performa sistem diukur menggunakan dua indikator kuantitatif utama: metrik Time on Task (satuan detik, skala ratio) untuk mengukur durasi kecepatan transaksi checkout, serta nilai instrumen baku kuesioner System Usability Scale (SUS) (satuan poin, skala interval) untuk menilai kelayakan kegunaan antarmuka. Pengujian melibatkan 25 responden pelanggan aktif dengan metode penyeimbang urutan (Counterbalancing AB/BA Design) demi menekan efek pembelajaran. Luaran tugas ini ditargetkan mampu membuktikan reduksi durasi transaksi minimal 20% serta pencapaian skor SUS melampaui nilai 68.

Sistem operasional retail makanan dan minuman (F&B) skala UMKM di wilayah Kebumen sering kali menghadapi kendala antrean fisik yang panjang akibat penumpukan pelayanan di meja kasir pada jam sibuk. Pada objek Kedai Kopi SRUPUT Kebumen, gejala awal teramati menunjukkan rata-rata waktu tunggu pemesanan melebihi 10 menit, yang berakibat pada tingginya tingkat pembatalan transaksi sebesar 15%. Masalah intinya terletak pada belum tersedianya rancangan antarmuka pemesanan mandiri digital yang ringkas guna memotong langkah prosedur pemesanan secara efisien.
 
Konteks Sistem (System Context): Ruang lingkup pengerjaan tugas dibatasi ke dalam batas operasional komponen komputasi berikut:

Komponen	Deskripsi Operasional Tugas Riset
Input
Data katalog menu kopi, pilihan kustomisasi item (level gula, es, ukuran cup), identitas pelanggan, dan input gestur layar.
Process
Transformasi visual alur kerja lewat 5 tahapan Design Thinking, pembaruan isi keranjang belanja, kalkulasi biaya, dan konfirmasi pembayaran.
Output
Artefak berupa rancangan prototipe interaktif tingkat tinggi (high-fidelity) pada figma, struk digital, dan indikator nomor antrean.
Outcome
Tereduksinya durasi waktu antrean kasir fisik serta meningkatnya kelancaran transaksi harian kedai.
Constraints
Keterbatasan resolusi dimensi layar gawai smartphone serta keragaman tingkat literasi teknologi pelanggan lokal.
Stakeholders
Pelanggan kedai kopi selaku pengguna akhir, staf barista operasional, dan pemilik usaha Kedai Kopi SRUPUT.

Objective Tugas: Mengevaluasi rancangan UI/UX aplikasi SRUPUT berbasis Design Thinking dalam meningkatkan efisiensi waktu pemesanan mandiri jika dibandingkan langsung terhadap aplikasi baseline pembanding.
Research Question (RQ): Apakah prototipe UI/UX aplikasi SRUPUT yang dirancang dengan metode Design Thinking menghasilkan time on task yang lebih cepat dan skor SUS yang lebih tinggi dibandingkan dengan aplikasi baseline Kopi Reman pada skenario pemesanan mandiri pelanggan?
Hypothesis Pair:
•	H₀ (Hipotesis Nol): Tidak ada perbedaan signifikan pada metrik time on task dan capaian skor SUS antara pengoperasian prototipe aplikasi SRUPUT dengan aplikasi baseline Kopi Reman.
•	H₁ (Hipotesis Alternatif): Rancangan prototipe aplikasi SRUPUT menghasilkan durasi transaksi (time on task) lebih singkat dan perolehan skor SUS lebih tinggi secara signifikan dibanding aplikasi baseline Kopi Reman.
Threshhold Keberhasilan: Ditargetkan terjadi penurunan durasi checkout minimal sebesar 20% dan perolehan skor kuesioner kelayakan SUS melampaui ambang nilai 68 poin.
Baseline dan Intervensi: Sistem pembanding (Baseline) nyata yang digunakan diambil dari literatur ilmiah yaitu aplikasi mobile "Kopi Reman" (Al Fikri dkk., 2024). Komponen intervensi yang dimasukkan peneliti untuk membedakannya dari baseline adalah pembaruan fitur penghemat langkah transaksi meliputi visual keranjang belanja yang dapat langsung diedit (quick-edit cart) serta metode pembayaran sekali klik (one-click payment).
 
 
Kajian literatur tugas ini memetakan posisi usulan riset terhadap publikasi terdahulu yang memanfaatkan metode Design Thinking. Al Fikri dkk. (2024) mengimplementasikan digitalisasi layanan menu pada aplikasi Kopi Reman namun belum mengoptimalkan area checkout. Pangestuti (2024) merancang aplikasi kopi ramah alergi di Mojokerto dengan alur yang panjang sehingga mengabaikan aspek kecepatan pemesanan masal. Riset dari Universitas Brawijaya (2022) merancang kios order mandiri dengan efektivitas tinggi namun efisiensi durasi waktu tugas penggunanya tercatat masih rendah (62.8%). Riset JMI Jayakarta (2024) and Bengi (2023) terbatas pada katalog web statis dan transaksi e-commerce pengiriman jarak jauh, tidak mendukung skema order langsung di tempat (on-premise).
Research Gap & Novelty: Kesenjangan yang diisi adalah Performance & Context Gap, di mana belum adanya optimalisasi antarmuka terfokus mikro pada modul Cart & Payment aplikasi pemesanan mandiri UMKM untuk menekan durasi checkout bagi demografi pelanggan di daerah. Kebaruan tugas ini terletak pada integrasi fitur ringkas penghemat langkah transaksi yang diuji secara head-to-head komparatif terhadap aplikasi baseline dari literatur jurnal nasional yang sahih.

Desain eksperimen tugas riset teknologi informasi ini berupa Controlled Comparison Study. Unit analisis yang diamati dan dibandingkan secara objektif adalah sesi pelaksanaan tugas (task session) pemesanan mandiri oleh pelanggan kedai. Eksperimen membandingkan performa operasional pengguna pada dua kondisi antarmuka yang setara secara visual:
•	Kondisi A (Baseline): Sesi transaksi pemesanan menggunakan antarmuka aplikasi pembanding Kopi Reman (Al Fikri dkk., 2024).
•	Kondisi B (Intervensi): Sesi transaksi pemesanan menggunakan antarmuka prototipe interaktif modul pembayaran aplikasi SRUPUT.

Definisi operasional variabel dari tugas riset ini disusun tanpa ada lompatan logis sebagai berikut:

•	Independent Variable (IV): Jenis rancangan antarmuka aplikasi pemesanan mandiri (Aplikasi Kopi Reman vs Prototipe SRUPUT).
•	Dependent Variable (DV): Efisiensi kecepatan transaksi dan tingkat kelayakan kegunaan kualitas antarmuka (usability).
•	Control Variables (CV): Jenis spesifikasi unit gawai smartphone pengujian yang seragam, koneksi jaringan internet Wi-Fi yang dikunci sama, dan teks lembar instruksi tugas pemesanan yang identik bagi seluruh responden.
Metrik, Instrumen, dan Data: Data mentah berupa data primer yang ditangkap melalui: 1) Metrik Time on Task satuan detik (skala Ratio) diukur objektif menggunakan instrumen aplikasi perekam layar smartphone pasca-uji untuk melacak timestamp sentuhan awal hingga halaman transaksi sukses
 
termuat; 2) Metrik kepuasan dinilai berdasarkan perolehan skor kuesioner baku System Usability Scale (SUS) rentang poin 0-100 (skala Interval) yang disebar digital lewat Google Form kepada 25 responden basis pelanggan aktif Kedai Kopi SRUPUT.

Prosedur Eksperimen & Mitigasi Bias: Pengujian dikondisikan terkontrol di lapangan. Untuk memitigasi ancaman validitas internal berupa efek pembelajaran (learning effect), sampel 25 responden dipecah acak menjadi dua alur urutan uji (Counterbalancing Design). Kelompok 1 (13 responden) mengoperasikan aplikasi baseline Kopi Reman terlebih dahulu sebelum menguji prototipe SRUPUT, sedangkan Kelompok 2 (12 responden) menguji prototipe SRUPUT terlebih dahulu sebelum mencoba aplikasi baseline. Jeda istirahat 5 menit diberikan di antara kedua sesi uji.
Teknik Analisis Data & Batasan: Data diolah memakai teknik komparasi nilai rata-rata (Mean). Penelitian tugas ini mengasumsikan responden terbiasa mengoperasikan smartphone layar sentuh, dengan batasan ruang lingkup operasional yang ditargetkan murni mengevaluasi kualitas interaksi visual front-end modul checkout tanpa melibatkan fungsionalitas pengodean database server backend kasir.

Rencana jadwal pelaksanaan pengumpulan tugas riset teknologi informasi ini dirancang dalam rentang waktu linier 4 bulan dengan bentuk matriks tabel horizontal sederhana yang selaras dengan dokumen acuan pengumpulan tugas sebagai berikut:

Tahapan Pelaksanaan Tugas Riset	Bulan 1	Bulan 2	Bulan 3	Bulan 4
Studi Literatur, Identifikasi Masalah, dan Eksplorasi Kebutuhan Objek SRUPUT	
⬛			
Penyusunan Usulan Proposal Berbasis Pertanyaan Matriks Reasoning RTI		
⬛		
Konstruksi Artefak Prototipe Interaktif High-Fidelity Aplikasi SRUPUT di Figma			
⬛	
Eksekusi Eksperimen Lapangan, Pengumpulan Data SUS, Analisis Perbandingan Mean, dan Pelaporan Tugas Akhir				
⬛

Al Fikri, M. S., dkk. (2024). Penerapan UI/UX Menggunakan Metode Design Thinking Pada Aplikasi Kopi Reman Berbasis Mobile. Jurnal Riset Teknologi Informasi (RTI) Universitas Putra Bangsa, 1(2), 115-128.
Bengi, A. (2023). Perancangan Antarmuka Berbasis Web Sistem Penjualan UKM Meulawi Coffee dengan Pendekatan User-Centered Design. Jurnal Informatika Daerah, 5(1), 45-56.
 
JMI Jayakarta. (2024). Pengembangan Aplikasi Katalog Digital Interaktif Menu Dinamis Usaha Retail Kuliner Bootchin Coffee. Jurnal Media Informatika, 12(3), 201-212.
Pangestuti, R. D. (2024). Penerapan Metode Design Thinking dalam Pemodelan UI/UX Aplikasi Coffee Care Ramah Kustomisasi Bahan di Mojokerto. Jurnal Ilmiah Komputer Grafis, 17(1), 89-102.
Peneliti Universitas Brawijaya. (2022). Evaluasi Usability dan Efisiensi Desain Antarmuka Sistem Pemesanan Mandiri (Self-Ordering Kiosk) di Kedai Kopi Sari. Jurnal Pengembangan Teknologi Informasi dan Ilmu Komputer, 6(8), 3412-3422.
