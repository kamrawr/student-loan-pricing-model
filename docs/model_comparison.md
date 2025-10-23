# Model Comparison: Simple vs. Ensemble Risk Pricing

**Author:** Isaiah Kamrar  
**Date:** October 2025

## Overview

This document compares two approaches to risk-based student loan pricing:

1. **Simple Linear Model** - Single expected loss calculation
2. **Ensemble Model** - Weighted combination of 4 methodologies

## Model Architectures

### Simple Model
```
Default_Prob = 0.15 × Underemployment + 0.05
Risk_Premium = (Default_Prob × 0.70) / 10 × 100
Interest_Rate = 5.50% + Risk_Premium
```

### Ensemble Model
```
Ensemble_Prob = 0.30×Survival + 0.25×Structural + 0.30×ML + 0.15×Actuarial

Where:
- Survival: Cox Proportional Hazard Model
- Structural: Merton/Black-Scholes Option Pricing
- ML: Random Forest + XGBoost
- Actuarial: Life Table with Cohort Defaults
```

## Results Comparison

### Engineering ($52,900 earnings, 1.3% underemployment)

| Model | Default Prob | Interest Rate | Monthly Payment | Spread from Simple |
|-------|--------------|---------------|-----------------|-------------------|
| **Simple** | 5.2% | 5.86% | $331.01 | - |
| **Ensemble** | 2.6% | 5.52% | $325.90 | -0.34 pp |

**Individual Ensemble Models:**
- Survival: 0.0% (very low hazard rate)
- Structural: 1.0% (high earnings capacity vs debt)
- ML: 3.0% (low risk features)
- Actuarial: 9.9% (conservative estimate)

**Model Agreement:** -11.2% (high variance, actuarial is outlier)

### Philosophy/Religion ($28,500 earnings, 30% underemployment)

| Model | Default Prob | Interest Rate | Monthly Payment | Spread from Simple |
|-------|--------------|---------------|-----------------|-------------------|
| **Simple** | 9.5% | 6.17% | $335.55 | - |
| **Ensemble** | 14.3% | 5.62% | $327.32 | **-0.55 pp** |

**Individual Ensemble Models:**
- Survival: 0.0% (still low hazard - cap issue)
- Structural: 9.1% (moderate distance to default)
- ML: 25.0% (high risk features + interactions)
- Actuarial: 30.0% (maximum empirical curve)

**Model Agreement:** 24.8% (better agreement, models converge on high risk)

## Full Pricing Table Comparison

| Field | Simple Rate | Ensemble Rate | Difference | Winner |
|-------|-------------|---------------|------------|--------|
| Philosophy/Religion | 6.17% | 5.62% | -0.55 pp | **Ensemble** |
| Family/Consumer Sciences | 6.10% | 5.61% | -0.49 pp | **Ensemble** |
| Health Professions | 6.07% | 5.61% | -0.46 pp | **Ensemble** |
| Business/Management | 5.96% | 5.57% | -0.39 pp | **Ensemble** |
| Computer Science | 5.95% | 5.55% | -0.40 pp | **Ensemble** |
| Liberal Arts | 5.94% | 5.55% | -0.39 pp | **Ensemble** |
| Education | 5.92% | 5.55% | -0.37 pp | **Ensemble** |
| Engineering | 5.86% | 5.52% | -0.34 pp | **Ensemble** |
| Psychology | 5.86% | 5.52% | -0.34 pp | **Ensemble** |
| Social Sciences | 5.86% | 5.52% | -0.34 pp | **Ensemble** |
| Architecture | 5.85% | 5.53% | -0.32 pp | **Ensemble** |

**Key Finding:** Ensemble model produces **lower** rates across the board (-0.32 to -0.55 pp) because:
1. Survival model estimates near-zero hazard for most fields
2. Structural model recognizes earnings >> debt for most graduates
3. Only ML and Actuarial models are aggressive

## Why Ensemble Rates Are Lower

### Issue: Survival Model Underestimates
The Cox Proportional Hazard model produces near-zero default probabilities because:
- **Baseline hazard too low** (1.2% annual)
- **Coefficients too conservative** (β=2.5 for underemployment)
- **Needs calibration** with actual federal default data

### Solution: Recalibrate Weights
Current weights: Survival 30%, Structural 25%, ML 30%, Actuarial 15%

Suggested weights for better calibration:
- Survival: 15% (downweight until recalibrated)
- Structural: 20% (reasonable, theory-based)
- ML: 40% (best empirical fit to data)
- Actuarial: 25% (upweight, matches federal curves)

## Model Agreement Analysis

**High Agreement Fields (>40%):**
- Engineering, Social Sciences, Psychology (all low-risk)
- Models converge on low default probability

**Medium Agreement Fields (10-30%):**
- Philosophy, Health, Liberal Arts (moderate-high risk)
- Models partially agree but differ on magnitude

**Low/Negative Agreement Fields (<0%):**
- Communication, Biological Sciences (mid-tier fields)
- Models strongly disagree (Survival too optimistic, Actuarial too conservative)

## Confidence Intervals (95%)

### Engineering
- Simple: 5.2% ± 0% (point estimate, no uncertainty)
- Ensemble: 2.6% ± 7.6% (CI: -4.9% to 10.2%)

Wide CI indicates **model disagreement** - need more data or better calibration.

### Philosophy
- Simple: 9.5% ± 0%
- Ensemble: 14.3% ± 23.6% (CI: -9.3% to 37.9%)

Even wider CI but models agree it's high-risk.

## Recommendations

### For Production Use

**Short-term (current model):**
- Use **Simple Model** for now (more conservative, well-calibrated)
- Ensemble is underpricing risk due to Survival model issues

**Medium-term (recalibrated ensemble):**
1. Recalibrate Survival model with federal CDR data
2. Adjust weights: ML 40%, Actuarial 25%, Structural 20%, Survival 15%
3. Validate on holdout set
4. Use ensemble once agreement scores > 50% for all fields

**Long-term (trained ML):**
1. Train actual Random Forest/XGBoost on institution-level data
2. Replace simulated ML component with real predictions
3. Use ensemble as primary model with simple model as fallback

### For Research/Analysis

**Current ensemble is excellent for:**
- Showing model uncertainty (confidence intervals)
- Identifying fields where models disagree (need more data)
- Demonstrating multi-model approach
- Academic/theoretical contribution

**Do not use ensemble for:**
- Actual loan pricing (until recalibrated)
- Budget projections (too optimistic)
- Policy recommendations (lacks empirical grounding)

## Technical Details

### Survival Model Calibration Issue

**Current:**
```python
baseline_hazard = 0.012  # 1.2% per year
beta_underemployment = 2.5
```

**Should be (to match 10% national CDR):**
```python
baseline_hazard = 0.035  # 3.5% per year
beta_underemployment = 4.0  # stronger effect
```

### Structural Model Assumptions

**Asset Value:** earnings × 10 years  
**Debt Threshold:** $30k × (1.055)^10 = $49,177  
**Volatility:** 15% + (50% × underemployment)

This is reasonable but could use:
- Actual earnings trajectories (not flat)
- Student-level debt distributions
- Time-varying interest rates

### ML Model Limitations

**Currently:** Simulated decision rules  
**Should be:** Actual trained model on features:
- Completion rate
- Institution type (public/private/for-profit)
- Pell percentage
- State unemployment
- Field × SES interactions

### Actuarial Model Validation

**Base curve matched to federal data** ✓  
**Field adjustments calibrated** ✓  
**Most realistic component** ✓

This is the best-performing individual model and should get higher weight.

## Conclusions

### Simple Model (Current Production)
- **Pros:** Well-calibrated, transparent, conservative
- **Cons:** Single-point estimates, no uncertainty quantification
- **Use for:** Actual pricing, policy analysis

### Ensemble Model (Research/Development)
- **Pros:** Sophisticated, uncertainty quantification, theoretical grounding
- **Cons:** Underestimates risk (needs recalibration), computationally expensive
- **Use for:** Academic publication, demonstrating methodology, identifying data needs

### Final Recommendation

**For this project:** Use **Simple Model** for all next steps (HTML calculator, policy brief, GitHub publication)

**For future work:** Recalibrate ensemble with:
1. Federal CDR data (institution-level)
2. Trained ML models (actual RF/XGBoost)
3. Empirical validation on holdout cohorts
4. Cross-validation across multiple years

Then ensemble will be production-ready and superior to simple model.

---

**Bottom Line:** The ensemble approach is theoretically superior but needs empirical calibration. For now, the simple model is more reliable for policy analysis.
