#!/usr/bin/env python3
"""
Paired T-Test Analysis untuk SRUPUT vs Kopi Reman
Analisis time on task dan SUS score
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

def load_data():
    """Load data dari folder 04-data"""
    time_df = pd.read_csv('../04-data/time_on_task.csv')
    sus_df = pd.read_csv('../04-data/sus_responses.csv')
    return time_df, sus_df

def test_normality(data, name):
    """Test normalitas menggunakan Shapiro-Wilk"""
    stat, p_value = stats.shapiro(data)
    print(f"\n{name} Normality Test:")
    print(f"  Statistic: {stat:.4f}")
    print(f"  p-value: {p_value:.4f}")
    if p_value > 0.05:
        print(f"  ✓ Data {name} berdistribusi normal (p > 0.05)")
        return True
    else:
        print(f"  ✗ Data {name} tidak berdistribusi normal (p <= 0.05)")
        return False

def paired_ttest_analysis(sruput_data, kopi_reman_data, metric_name):
    """Perform paired t-test dengan effect size"""
    # Paired t-test
    t_stat, p_value = stats.ttest_rel(sruput_data, kopi_reman_data)
    
    # Calculate effect size (Cohen's d for paired samples)
    diff = sruput_data - kopi_reman_data
    cohens_d = diff.mean() / diff.std()
    
    # Confidence interval
    ci = stats.t.interval(0.95, len(diff)-1, 
                          loc=diff.mean(), 
                          scale=stats.sem(diff))
    
    print(f"\n{'='*60}")
    print(f"Paired T-Test: {metric_name}")
    print(f"{'='*60}")
    print(f"SRUPUT mean ± std: {sruput_data.mean():.2f} ± {sruput_data.std():.2f}")
    print(f"Kopi Reman mean ± std: {kopi_reman_data.mean():.2f} ± {kopi_reman_data.std():.2f}")
    print(f"\nMean difference: {diff.mean():.2f}")
    print(f"t-statistic: {t_stat:.4f}")
    print(f"p-value: {p_value:.4f}")
    print(f"Cohen's d: {cohens_d:.4f}")
    print(f"95% CI: [{ci[0]:.2f}, {ci[1]:.2f}]")
    
    # Interpretation
    if p_value < 0.01:
        print(f"\n✓ Sangat signifikan (p < 0.01)")
    elif p_value < 0.05:
        print(f"\n✓ Signifikan (p < 0.05)")
    else:
        print(f"\n✗ Tidak signifikan (p >= 0.05)")
    
    # Effect size interpretation
    if abs(cohens_d) > 0.8:
        print(f"Effect size: LARGE (|d| > 0.8)")
    elif abs(cohens_d) > 0.5:
        print(f"Effect size: MEDIUM (|d| > 0.5)")
    elif abs(cohens_d) > 0.2:
        print(f"Effect size: SMALL (|d| > 0.2)")
    else:
        print(f"Effect size: NEGLIGIBLE (|d| <= 0.2)")
    
    return {
        't_stat': t_stat,
        'p_value': p_value,
        'cohens_d': cohens_d,
        'ci_lower': ci[0],
        'ci_upper': ci[1],
        'sruput_mean': sruput_data.mean(),
        'sruput_std': sruput_data.std(),
        'kopi_reman_mean': kopi_reman_data.mean(),
        'kopi_reman_std': kopi_reman_data.std()
    }

def main():
    print("="*60)
    print("ANALISIS STATISTIK: SRUPUT vs KOPI REMAN")
    print("="*60)
    
    # Load data
    time_df, sus_df = load_data()
    
    # Prepare data untuk time on task (average per responden)
    time_avg = time_df.groupby(['responden_id', 'aplikasi'])['waktu_detik'].mean().reset_index()
    time_sruput = time_avg[time_avg['aplikasi'] == 'SRUPUT']['waktu_detik'].values
    time_kopi_reman = time_avg[time_avg['aplikasi'] == 'Kopi Reman']['waktu_detik'].values
    
    # Prepare data untuk SUS
    sus_sruput = sus_df[sus_df['aplikasi'] == 'SRUPUT']['sus_score'].values
    sus_kopi_reman = sus_df[sus_df['aplikasi'] == 'Kopi Reman']['sus_score'].values
    
    # Test normality
    print("\n" + "="*60)
    print("UJI NORMALITAS (Shapiro-Wilk)")
    print("="*60)
    
    test_normality(time_sruput, "Time on Task - SRUPUT")
    test_normality(time_kopi_reman, "Time on Task - Kopi Reman")
    test_normality(sus_sruput, "SUS Score - SRUPUT")
    test_normality(sus_kopi_reman, "SUS Score - Kopi Reman")
    
    # Paired t-test
    time_results = paired_ttest_analysis(time_sruput, time_kopi_reman, "Time on Task (detik)")
    sus_results = paired_ttest_analysis(sus_sruput, sus_kopi_reman, "SUS Score")
    
    # Save results
    results_df = pd.DataFrame({
        'Metric': ['Time on Task', 'SUS Score'],
        'SRUPUT_Mean': [time_results['sruput_mean'], sus_results['sruput_mean']],
        'SRUPUT_Std': [time_results['sruput_std'], sus_results['sruput_std']],
        'KopiReman_Mean': [time_results['kopi_reman_mean'], sus_results['kopi_reman_mean']],
        'KopiReman_Std': [time_results['kopi_reman_std'], sus_results['kopi_reman_std']],
        't_stat': [time_results['t_stat'], sus_results['t_stat']],
        'p_value': [time_results['p_value'], sus_results['p_value']],
        'cohens_d': [time_results['cohens_d'], sus_results['cohens_d']],
        'CI_95_lower': [time_results['ci_lower'], sus_results['ci_lower']],
        'CI_95_upper': [time_results['ci_upper'], sus_results['ci_upper']]
    })
    
    results_df.to_csv('../06-output/tables/statistical_test_results.csv', index=False)
    print("\n✓ Results saved to ../06-output/tables/statistical_test_results.csv")

if __name__ == "__main__":
    main()
