# Risk-Based Student Loan Pricing: Initial Findings

**Author:** Isaiah Kamrar  
**Date:** October 2025  
**Status:** Preliminary Analysis

## Executive Summary

This analysis develops a risk-adjusted pricing model for federal student loans based on academic field of study. Using data from 7,703 U.S. institutions and 24 academic fields, we estimate default probabilities and calculate actuarially fair interest rates.

**Key Finding:** Interest rates would range from **5.85% (Engineering)** to **6.17% (Philosophy/Religion)** under pure risk-based pricing, representing a **0.32 percentage point spread**. However, fairness-adjusted pricing for low-income students can reduce rates by up to **1.9 percentage points**.

## Methodology

### Data Sources
- **College Scorecard** institutional data (7,703 institutions)
- **Field-level outcomes** by 24 PCIP categories
- **Prior research** from Kamrar (2025) underemployment and ML default prediction studies

### Risk Model
```
Default_Probability = 0.15 × Underemployment_Rate + 0.05

Risk_Premium = (Default_Prob × Loss_Given_Default) / Loan_Duration

Interest_Rate = Base_Rate + Risk_Premium
```

### Parameters
- **Base Rate:** 5.50% (current federal undergraduate rate)
- **Recovery Rate:** 30% (assume 70% loss given default)
- **Loan Duration:** 10 years (standard repayment)
- **Default Probability Range:** 5% to 20% (capped)

## Results

### Full Pricing Table (Pure Risk-Based)

| Field | Interest Rate | Monthly Payment | Debt-to-Earnings |
|-------|--------------|-----------------|------------------|
| Philosophy/Religion | 6.17% | $335.55 | 0.141 |
| Family/Consumer Sciences | 6.10% | $334.63 | 0.133 |
| Health Professions | 6.07% | $334.07 | 0.136 |
| Legal Professions | 6.04% | $333.72 | 0.138 |
| Business/Management | 5.96% | $332.43 | 0.112 |
| Computer Science | 5.95% | $332.26 | 0.103 |
| Liberal Arts | 5.94% | $332.10 | 0.132 |
| Education | 5.92% | $331.90 | 0.109 |
| Visual/Performing Arts | 5.91% | $331.73 | 0.118 |
| Communication | 5.89% | $331.44 | 0.094 |
| Engineering | 5.86% | $331.01 | 0.075 |
| Psychology | 5.86% | $331.00 | 0.099 |
| Social Sciences | 5.86% | $330.98 | 0.087 |
| Architecture | 5.85% | $330.81 | 0.085 |

**Spread:** 0.32 percentage points (5.85% - 6.17%)  
**Loan Amount:** $30,000 (national average)  
**Repayment Period:** 10 years

### Scenario Comparison

#### Engineering ($52,900 median earnings)
| Scenario | Interest Rate | Monthly Payment |
|----------|---------------|-----------------|
| Pure Risk-Based | 5.86% | $331.01 |
| Low-Income w/ Fairness | 4.82% | $315.62 |
| High-Income w/ Fairness | 5.86% | $331.01 |
| Current Federal | 5.50% | $325.58 |

**Insight:** Engineering students would pay slightly more than current federal rates but significantly less than high-risk fields.

#### Philosophy/Religion ($28,500 median earnings)
| Scenario | Interest Rate | Monthly Payment |
|----------|---------------|-----------------|
| Pure Risk-Based | 6.17% | $335.55 |
| Low-Income w/ Fairness | 4.27% | $307.53 |
| High-Income w/ Fairness | 6.17% | $335.55 |
| Current Federal | 5.50% | $325.58 |

**Insight:** Philosophy students face higher risk premiums but receive substantial subsidies under fairness-adjusted pricing.

## Key Insights

### 1. Risk Spread is Modest
The **0.32 percentage point spread** between lowest and highest risk fields is relatively small—less than many critics might expect. This suggests that:
- Field choice matters, but not dramatically
- Most fields cluster around similar default risk
- Extreme outliers (e.g., for-profit institutions) drive aggregate default rates

### 2. Fairness Adjustments Are Substantial
Low-income students in high-risk fields receive up to **1.9 pp rate reductions**, bringing Philosophy from 6.17% → 4.27%. This:
- Preserves access to liberal arts for low-SES students
- Maintains incentives for high-earners to choose efficient fields
- Balances equity and efficiency

### 3. Debt-to-Earnings Ratios Vary Widely
- **Engineering:** 0.075 (7.5% of earnings toward debt)
- **Philosophy:** 0.141 (14.1% of earnings toward debt)

Even with higher rates, Philosophy graduates face **87% higher debt burdens** due to lower earnings, not just interest rates.

### 4. Current Federal Rate is Close to Risk-Neutral
At **5.50%**, the current federal rate sits near the middle of the risk distribution. This suggests:
- Low-risk fields (Engineering) slightly subsidize high-risk fields
- Current system approximates a risk pool
- Moving to pure risk-based pricing would create winners/losers

## Policy Implications

### Advantages of Risk-Based Pricing
1. **Actuarial Fairness:** Students pay for their actual default risk
2. **Market Signals:** Encourages enrollment in high-demand fields
3. **Lender Sustainability:** Reduces taxpayer subsidy requirements
4. **Transparency:** Makes true cost of field choice visible

### Disadvantages
1. **Equity Concerns:** Disadvantages low-income students in liberal arts
2. **Public Goods Externalities:** Teachers, social workers penalized despite societal value
3. **Signaling Distortion:** Overemphasizes earnings, undervalues mission-driven careers
4. **Information Asymmetry:** 18-year-olds may not fully understand risk-rate relationship

### Recommended Hybrid Model
**Progressive Risk-Adjusted Pricing:**
- **Base Rate:** 5.00% for all students (slightly below current)
- **Risk Premium:** 0% to +0.75% based on field (half of full actuarial)
- **Income Subsidy:** -0.50% to -2.00% for family income < $60k
- **Effective Range:** 3.00% (low-income engineering) to 5.75% (high-income philosophy)

This balances efficiency, equity, and political feasibility.

## Next Steps

### Data Enhancements
1. **Individual-level data:** Obtain restricted-use NSLDS for student-level analysis
2. **Default timing:** Model when defaults occur (2-year, 3-year, lifetime)
3. **Field switching:** Account for students changing majors
4. **Graduate outcomes:** Extend to master's/doctoral programs

### Model Refinements
1. **Dynamic pricing:** Update rates based on labor market changes
2. **Institution effects:** Adjust for school quality, not just field
3. **Regional variation:** Account for geographic differences in earnings/employment
4. **Cohort effects:** Business cycle impacts on default

### Policy Analysis
1. **Budget neutrality:** Calculate federal subsidy impact
2. **Enrollment effects:** Predict behavioral response to pricing signals
3. **Distributional analysis:** Who wins/loses under different scenarios
4. **Political feasibility:** Congressional Budget Office scoring

### Interactive Tools
1. **Loan calculator:** Web app for students to compare scenarios
2. **Policy simulator:** Dashboard for policymakers to test parameters
3. **Data explorer:** Interactive visualization of field risk rankings

## Technical Notes

### Model Assumptions
- **Linear default-risk relationship:** May understate extreme risks
- **30% recovery rate:** Conservative; actual recoveries vary
- **10-year horizon:** Standard plan; IBR plans would differ
- **Static labor markets:** Doesn't account for automation trends

### Calibration
Model calibrated to match:
- National 3-year cohort default rate (~10%)
- Field-level underemployment proxies (Kamrar 2025)
- Institutional repayment rates from College Scorecard

### Sensitivity Analysis Needed
- Default probability elasticity
- Recovery rate variations
- Interest rate environment changes
- Macroeconomic shocks

## Conclusion

Risk-based student loan pricing is **technically feasible** but requires **fairness constraints** to avoid exacerbating inequality. A **hybrid model** with progressive subsidies can balance efficiency and equity while maintaining incentives for career-relevant education.

The modest **0.32 pp spread** suggests field risk is real but manageable. Combined with income-driven repayment and targeted subsidies, risk-adjusted pricing could improve loan system sustainability without harming access.

**Key Recommendation:** Pilot risk-based pricing at graduate level first (MBAs, law schools) where earnings differences are larger and students are older. Use results to inform undergraduate policy.

---

## Appendix: Calculations

### Default Probability Estimation
```
Philosophy/Religion:
  Underemployment = 30%
  Default_Prob = 0.15 × 0.30 + 0.05 = 0.095 (9.5%)

Engineering:
  Underemployment = 1.3%
  Default_Prob = 0.15 × 0.013 + 0.05 = 0.052 (5.2%)
```

### Risk Premium Calculation
```
Philosophy/Religion:
  Expected_Loss = 0.095 × (1 - 0.30) = 0.0665
  Risk_Premium = (0.0665 / 10) × 100 = 0.665 pp
  Total_Rate = 5.50% + 0.665% = 6.165%

Engineering:
  Expected_Loss = 0.052 × (1 - 0.30) = 0.0364
  Risk_Premium = (0.0364 / 10) × 100 = 0.364 pp
  Total_Rate = 5.50% + 0.364% = 5.864%
```

### Fairness Adjustment (Low-Income Philosophy)
```
Family Income = $25,000 (< $30k threshold)
Income Factor = 1.0 (maximum subsidy)
Default Prob = 0.095

Adjustment = 1.0 × 0.095 × 2.0 × 10 = 1.9 pp
Adjusted Rate = 6.165% - 1.9% = 4.265%
```

---

**For questions or collaboration:**  
Isaiah Kamrar | rawrdog92@yahoo.com | @kamrawr
