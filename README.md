# Risk-Based Student Loan Pricing by Academic Major

**Author:** Isaiah Kamrar  
**Status:** Complete  
**Last Updated:** October 2025

## 🚀 Interactive Explorer

**[→ Explore the Interactive Overview Page](https://kamrawr.github.io/research-synthesis-lab/projects/student-loan-risk-pricing/)**

Features:
- **Interactive Pricing Calculator** - Calculate your personalized interest rate
- **Field Risk Visualizations** - D3.js scatter plots and bar charts
- **Graduate Program Analysis** - MBA, JD, MD, and more
- **Policy Analysis** - Implementation roadmap and budget impact
- **Complete Methodology** - Technical documentation

## Project Overview

This project develops a risk-based pricing model for student loans that adjusts interest rates based on the expected default risk associated with different academic majors/fields of study. It builds on:

1. **2018 Capstone Research** - Original college premium and risk modeling using College Scorecard data (1997-2015)
2. **2025 ML Default Prediction** - Machine learning models achieving 87% accuracy in predicting institutional default risk
3. **2025 Field-Labor Polarization** - Analysis of field-specific labor market outcomes and automation exposure
4. **2025 Underemployment Analysis** - Comprehensive field-level risk assessment

## Research Question

**Can we develop actuarially fair student loan pricing that accounts for field-specific default risk while maintaining equity and not disadvantaging low-SES students?**

## Data Sources

### Primary Data
- **College Scorecard** (U.S. Department of Education)
  - Institution-level outcomes (7,703 institutions)
  - Field-specific earnings and completion data
  - 3-year cohort default rates
  - Student demographics (Pell %, first-gen %)

### Derived Metrics (from prior research)
- **Field Risk Scores** - Underemployment proxy by 24 PCIP fields
- **Earnings Potential** - Median earnings 6-10 years post-entry
- **Repayment Capacity** - Debt-to-earnings ratios
- **Completion Rates** - 6-year completion by field

## Methodology

### Completed Analysis

**✅ Phase 1: Risk Assessment**
1. Field-level default risk estimation (24 PCIP fields)
2. Earnings trajectory modeling by major
3. Debt burden analysis (undergraduate + graduate)
4. Expected loss calculation with LGD = 70%

**✅ Phase 2: Pricing Model Development**
1. Simple structural model (production-ready)
2. Risk-adjusted spreads by field (5.85% - 6.17%)
3. Institution quality adjustments (0.40x - 2.18x multipliers)
4. Progressive income subsidies (-0.5% to -2.0%)
5. Ensemble model (survival, structural, ML, actuarial) for comparison

**✅ Phase 3: Policy Simulation**
1. Hybrid model: Base 5.00% + Risk Premium (0-0.75%) - Income Subsidy
2. Budget analysis: $2-3B annual savings from reduced defaults
3. Equity assessment: 55% pay less, all low-income students protected
4. Policy brief for Department of Education (docs/policy_brief_ed.md)

## Key Findings

### Field Risk Rankings (from Underemployment Analysis)

**Highest Risk:**
- Philosophy/Religion (30% underemployment proxy)
- Family/Consumer Sciences (24%)
- Health Professions (21%)

**Lowest Risk:**
- Engineering (1.3%)
- Psychology (1.2%)
- Social Sciences (1.1%)
- Architecture (0%)

### Earnings Differential
- Engineering: $52,900 median (6yr post-entry)
- Philosophy: $28,500 median
- **Spread: $24,400 (86% difference)**

## Proposed Pricing Framework

### Hybrid Model (Implemented & Recommended)

**Formula:**
```
Interest_Rate = Base_Rate(5.00%) + Risk_Premium(0-0.75%) - Income_Subsidy(0.5-2.0%)
```

**Features:**
- **Base Rate Reduction:** 5.50% → 5.00% for all students
- **Capped Risk Premium:** 50% of actuarially fair premium (max 0.75%)
- **Progressive Subsidies:** Largest for low-income students in all fields
- **Net Range:** 3.00% - 5.75% (vs. current flat 5.50%)

**Example Rates:**
| Scenario | Base | Risk | Subsidy | Final Rate | Monthly ($30k) |
|----------|------|------|---------|------------|----------------|
| Engineering, High Income | 5.00% | +0.17% | 0% | 5.17% | $322 |
| Engineering, Low Income | 5.00% | +0.17% | -1.00% | 4.17% | $307 |
| Philosophy, High Income | 5.00% | +0.75% | 0% | 5.75% | $330 |
| Philosophy, Low Income | 5.00% | +0.75% | -1.90% | 3.85% | $301 |

**Key Outcome:** Low-income Philosophy students pay **less** than high-income Engineering students

### Institution Quality Adjustments

| Institution Type | Multiplier | Example Effect on Default Risk |
|-----------------|------------|-------------------------------|
| R1 + Most Selective + Private | 0.40x | 5.2% → 2.1% |
| R1 + Selective + Public | 0.70x | 5.2% → 3.6% |
| Master's + Moderate + Public | 0.90x | 5.2% → 4.7% |
| Associate + Open + Public | 1.32x | 5.2% → 6.9% |
| For-Profit | 2.18x | 5.2% → 11.3% |

## Ethical Considerations

### Concerns
1. **Discrimination:** Could discourage liberal arts, humanities
2. **SES Amplification:** Low-income students concentrated in high-risk fields
3. **Self-Fulfilling Prophecy:** Higher rates → more default → higher rates
4. **Career Flexibility:** Students locked into high-earning fields

### Safeguards
1. **Income-Based Caps:** Monthly payment ≤ 10% discretionary income
2. **Forgiveness Provisions:** Public service, non-profit sector
3. **Fairness Audits:** Regular assessment for demographic bias
4. **Transparency:** Students see risk scores before enrollment

## Technical Implementation

### Default Probability Model

**Structural Approach (Production):**
```python
Default_Prob = 0.15 × Underemployment_Rate + 0.05
Risk_Premium = (Default_Prob × Loss_Given_Default × 100) / Duration
```

**Parameters:**
- Loss Given Default (LGD): 70% (30% recovery rate)
- Duration: 10 years (standard repayment)
- Underemployment: Proxy from job posting data vs. field size

**Ensemble Model (Research):**
1. **Survival Analysis:** Cox proportional hazards for time-to-default
2. **Structural Credit Model:** Merton-style distance-to-default
3. **Machine Learning:** Random Forest with fairness constraints (87% accuracy)
4. **Actuarial Life Table:** Traditional insurance approach

**Recommendation:** Use simple structural model for policy. Ensemble adds complexity without material improvement for pricing applications.

### Software Stack
- **Python 3.9+**: pandas, numpy, scipy (data processing and modeling)
- **R 4.0+**: survival, ggplot2 (survival analysis)
- **JavaScript/D3.js v7**: Interactive visualizations
- **HTML5/CSS3**: Responsive web interface
- **GitHub Pages**: Free hosting for interactive explorer

## Repository Structure

```
student-loan-pricing-model/
├── README.md
├── QUICKSTART.md
├── data/
│   ├── field_risk_updated.csv               # 24 PCIP fields, latest Scorecard data
│   ├── field_risk_scores.json               # Structured JSON version
│   ├── graduate_programs.json               # Graduate/professional programs
│   └── institution_adjustments.json         # Carnegie/selectivity multipliers
├── models/
│   ├── pricing_engine.py                    # Simple structural model (production)
│   ├── pricing_engine_ensemble.py           # Advanced ensemble model (research)
│   ├── pricing_engine_graduate.py           # Graduate program extension
│   └── pricing_engine_institution_quality.py # Institution quality adjustments
├── docs/
│   ├── policy_brief_ed.md                   # Department of Education policy brief
│   ├── findings_simple_vs_ensemble.md       # Model comparison analysis
│   └── implementation_roadmap.md            # 3-phase implementation plan
└── visualizations/
    ├── simple_pricing_tables.png
    ├── ensemble_comparison.png
    ├── graduate_pricing_tables.png
    └── institution_quality_heatmap.png

Interactive Explorer (separate repository):
https://github.com/kamrawr/research-synthesis-lab
├── projects/
│   └── student-loan-risk-pricing/
│       ├── index.html                       # Main interactive page
│       ├── data.js                          # Field and graduate program data
│       └── app.js                           # D3.js visualizations & calculator
```

## Results Summary

### Budget Impact
- **Revenue-neutral** if properly calibrated
- **$2-3B annual savings** from reduced defaults (better price signals)
- High-risk borrowers: +$1.2B revenue
- Low-risk borrowers: -$0.8B revenue  
- Net federal budget impact: **+$2.4-3.4B/year**

### Distribution of Winners/Losers
- **55% pay less**: STEM, Business, Health fields
- **30% neutral**: Middle-tier fields (±$5/month)
- **15% pay more**: Humanities at for-profit institutions
- **100% low-income**: Reduced rates regardless of field

### Implementation Roadmap
1. **Phase 1 (2026-2027)**: Graduate pilot (MBA, JD, MD) - 15% of loan volume
2. **Phase 2 (2028-2030)**: Undergraduate expansion with gradual premiums
3. **Phase 3 (2031+)**: Full implementation with dynamic annual updates

## Resources

- **[Interactive Explorer](https://kamrawr.github.io/research-synthesis-lab/projects/student-loan-risk-pricing/)** - Pricing calculator, visualizations, policy analysis
- **[Policy Brief](docs/policy_brief_ed.md)** - Department of Education summary
- **[Research Synthesis Lab](https://kamrawr.github.io/research-synthesis-lab/)** - All related projects

## References

### Prior Research (Kamrar)
- Kamrar, I. (2018). *College Premium and Risk Modeling*. Undergraduate Capstone.
- Kamrar, I. (2025). *Machine Learning for Default Risk Prediction*. Research Synthesis Lab.
- Kamrar, I. (2025). *Field-Specific Labor Market Polarization*. Research Synthesis Lab.
- Kamrar, I. (2025). *College Underemployment & Long-Term Career Trajectories*. Research Synthesis Lab.

### Related Literature
- Avery, C., & Turner, S. (2012). Student loans: Do college students borrow too much—Or not enough? *Journal of Economic Perspectives*.
- Lochner, L., & Monge-Naranjo, A. (2011). The nature of credit constraints and human capital. *American Economic Review*.
- Webber, D. A. (2014). The lifetime earnings premia of different majors. *Industrial Relations*.

## Contact

Isaiah Kamrar  
Email: rawrdog92@yahoo.com  
GitHub: @kamrawr

## License

CC-BY-4.0 - Attribution required for derivative works
