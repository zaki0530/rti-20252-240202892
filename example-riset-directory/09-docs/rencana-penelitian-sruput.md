# Rencana Penelitian: Evaluasi Usability SRUPUT UI/UX

**Judul**: Evaluasi Usability dan Efisiensi Prototipe Aplikasi Pemesanan Kopi SRUPUT: Studi Komparatif dengan Aplikasi Kopi Reman

**Peneliti**: [Abu Zaki]  
**Pembimbing**: [Helmi Bahar Alim,S.Kom.,M.Kom]  
**Institusi**: Program Studi Teknik Informatika 

---

## 1. Ringkasan Penelitian

Penelitian ini bertujuan mengevaluasi apakah prototipe aplikasi SRUPUT menghasilkan **time on task** yang lebih cepat dan **System Usability Scale (SUS) score** yang lebih tinggi dibandingkan aplikasi baseline Kopi Reman. Metode within-subject experimental design dengan 25 responden mahasiswa. Analisis menggunakan paired t-test dan Cohen's d untuk effect size.

**Expected Outcome**: SRUPUT terbukti superior dalam efisiensi dan usability, memberikan justifikasi untuk implementasi di Kedai SRUPUT.

---

## 2. Latar Belakang Masalah

### 2.1 Konteks Bisnis
Kedai kopi SRUPUT mengalami antrian panjang (>10 menit) pada jam sibuk, menyebabkan:
- Customer frustration dan abandoned orders
- Lost revenue (estimasi 20-30 customer/hari)
- Penurunan customer satisfaction

### 2.2 Root Cause Analysis
70% waktu antrian dihabiskan untuk proses pemesanan di aplikasi Kopi Reman yang:
- Lambat (terlalu banyak steps)
- Tidak intuitif (hamburger menu hidden, cart tersembunyi)
- Membingungkan (customization di screen terpisah)

### 2.3 Proposed Solution
Desain ulang UI/UX dengan prinsip:
- **Minimize cognitive load**: Bottom navigation, inline editing
- **Maximize accessibility**: FAB cart always visible
- **Reduce steps**: Streamlined checkout flow

---

## 3. Research Questions & Hypotheses

### RQ1: Efisiensi
**Q**: Apakah prototipe SRUPUT menghasilkan time on task yang lebih cepat dibandingkan Kopi Reman?

**H₀**: Tidak ada perbedaan signifikan time on task antara SRUPUT dan Kopi Reman  
**H₁**: SRUPUT memiliki time on task yang lebih cepat (μ_SRUPUT < μ_Kopi Reman)

### RQ2: Usability
**Q**: Apakah prototipe SRUPUT menghasilkan SUS score yang lebih tinggi dibandingkan Kopi Reman?

**H₀**: Tidak ada perbedaan signifikan SUS score antara SRUPUT dan Kopi Reman  
**H₁**: SRUPUT memiliki SUS score yang lebih tinggi (μ_SRUPUT > μ_Kopi Reman)

---

## 4. Roadmap Penelitian (5 Fase)

### Fase 1: Literature Review & Problem Framing (2 minggu)
**Deliverable**:
- Literature matrix (15-20 papers)
- Gap analysis
- Theoretical framework (Nielsen's usability, cognitive load theory)

**Status**: ✅ Complete

### Fase 2: Design & Prototyping (6 minggu)
**Deliverable**:
- High-fidelity prototype SRUPUT (Figma)
- Task scenarios (simple & complex)
- Expert review documentation

**Status**: ✅ Complete

### Fase 3: Data Collection (6 minggu)
**Activities**:
- Pilot testing (n=5)
- Main study (n=25)
- Data cleaning & validation

**Deliverable**:
- Time on task data (CSV)
- SUS responses (CSV)
- Demographics data
- Observation notes

**Status**: 🔄 In Progress (Week 4/6)

### Fase 4: Analysis & Interpretation (2 minggu)
**Activities**:
- Descriptive statistics
- Normality testing (Shapiro-Wilk)
- Paired t-test
- Effect size calculation
- Visualization

**Deliverable**:
- Statistical test results
- Charts & graphs
- Interpretation document

**Status**: ⏳ Scheduled (Week 13-14)

### Fase 5: Scientific Writing (3 minggu)
**Activities**:
- Paper drafting (IMRAD format)
- Internal review
- Revision
- Submission

**Deliverable**:
- Final paper
- Supplementary materials
- Submission confirmation

**Status**: 📅 Scheduled (Week 15-17)

---

## 5. Metodologi Detail

### 5.1 Desain Eksperimen
- **Type**: Within-subject (repeated measures)
- **IV**: Jenis aplikasi (SRUPUT vs Kopi Reman)
- **DV1**: Time on task (detik)
- **DV2**: SUS score (0-100)
- **CV**: Task complexity (simple vs complex)

### 5.2 Participants
- **N**: 25 responden
- **Sampling**: Purposive (mahasiswa IT, frequent coffee buyers)
- **Inclusion criteria**:
  - Usia 18-30 tahun
  - Membeli kopi ≥2x/minggu
  - Familiar dengan mobile apps

### 5.3 Procedures
1. Informed consent + demographics
2. App A → Task 1 → Task 2 → SUS
3. Break 2 menit
4. App B → Task 1 → Task 2 → SUS
5. Post-interview

Order A/B di-randomize untuk counterbalance

### 5.4 Analysis Plan
- Descriptive: mean, std, median
- Normality: Shapiro-Wilk test
- Inference: Paired t-test (α = 0.05)
- Effect size: Cohen's d
- Software: Python (scipy, pandas, matplotlib)

---

## 6. Expected Contributions

### 6.1 Theoretical Contributions
- Framework evaluasi UI/UX untuk mobile F&B apps
- Validation Nielsen's principles di konteks Indonesian F&B
- Evidence cognitive load reduction meningkatkan efficiency & satisfaction

### 6.2 Practical Contributions
- Design guidelines untuk F&B app developers
- Quantitative justification untuk UI/UX investment
- Reusable evaluation methodology

### 6.3 Business Impact
- Reduced antrian time → increased customer throughput
- Better UX → higher customer satisfaction → repeat business
- Estimated ROI: 12 additional customers/day = Rp 600.000/hari additional revenue

---

## 7. Limitations & Mitigation

| Limitation | Impact | Mitigation |
|------------|--------|-----------|
| Sample bias (tech-savvy mahasiswa) | External validity | Acknowledge limitation, recommend future work dengan diverse demographics |
| Lab setting vs real café | Ecological validity | Mention sebagai limitation, plan longitudinal study |
| Self-reported SUS | Response bias | Triangulate dengan objective metrics (time on task) |
| Small sample (n=25) | Statistical power | Adequate untuk within-subject paired design (power = 0.92) |

---

## 8. Timeline & Milestones

Lihat detail di: [../00-admin/timeline-penelitian.md](../00-admin/timeline-penelitian.md)

**Key Dates**:
- Proposal Approval: 15 Feb 2024 ✅
- Data Collection Complete: 15 May 2024 🔄
- Analysis Complete: 31 May 2024 ⏳
- Paper Submission: 15 June 2024 📅

---

## 9. Resources & Budget

**Budget**: Rp 1.500.000
- Incentive responden: Rp 1.250.000
- Miscellaneous: Rp 250.000

**Tools**: Figma, Python, Google Forms, Git (all free)

---

## 10. Risk Management

Lihat detail di: [../00-admin/timeline-penelitian.md](../00-admin/timeline-penelitian.md#risk-management)

**Top Risks**:
1. Recruitment difficulty → Early start + incentive
2. Non-normal data → Non-parametric alternative ready
3. Timeline delay → 2-week buffer

---

## 11. Dissemination Plan

### Target Publications
**Primary**:
- Jurnal Nasional Terakreditasi (Sinta 2-3)
- Konferensi HCI regional

**Secondary**:
- Tech blog post untuk practitioners
- Open data di GitHub untuk replicability

### Knowledge Transfer
- Presentation ke Kedai SRUPUT management
- Sharing di komunitas UI/UX Indonesia
- Workshop tentang usability evaluation methodology

---

## 12. Ethical Considerations

- ✅ Informed consent dari semua responden
- ✅ Anonymity terjaga (responden_id, bukan nama)
- ✅ Voluntary participation (boleh withdraw kapanpun)
- ✅ Data security (encrypted storage)
- ✅ No deception (transparent tentang tujuan penelitian)

---

## 13. Success Criteria

**Minimum Success**:
- [ ] N ≥ 20 responden
- [ ] Data terkumpul lengkap (time on task + SUS)
- [ ] Analysis complete dengan proper statistics

**Target Success**:
- [ ] N = 25 responden
- [ ] Significant results (p < 0.05) untuk minimal 1 metrik
- [ ] Paper accepted di jurnal/konferensi

**Excellent Success**:
- [ ] N = 25 responden
- [ ] Significant results untuk both metrics
- [ ] Large effect size (d > 0.8)
- [ ] Paper accepted + Best Paper Award (aspirational)

---

## 14. Contingency Plans

### Jika Hasil Tidak Signifikan
- Failure analysis mendalam
- Boundary condition investigation
- Shift contribution ke methodological framework

### Jika Timeline Severely Delayed
- Prioritize core analysis
- Defer publication ke periode berikutnya
- Focus on thesis completion first

---

## 15. Next Steps (Immediate Actions)

1. ☐ Complete data collection (remaining 5 responden)
2. ☐ Data validation & cleaning
3. ☐ Run statistical analysis scripts
4. ☐ Generate visualizations
5. ☐ Start paper drafting (Introduction & Method sections)

---

**Document Version**: 1.0  
**Last Updated**: [Date]  
**Status**: Living document (updated weekly)
