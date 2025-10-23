# Quick Start Guide: Student Loan Pricing Model

Get started with risk-based student loan pricing analysis in 5 minutes.

## Setup

### Requirements
- Python 3.7+
- pandas, numpy

```bash
pip install pandas numpy
```

### Directory Structure
```
student-loan-pricing-model/
├── data/field_risk_scores.json  # Field-level risk data
├── models/pricing_engine.py      # Pricing calculator
└── docs/initial_findings.md      # Full analysis
```

## Usage

### 1. Run the Pricing Model

```bash
cd ~/student-loan-pricing-model/models
python3 pricing_engine.py
```

This generates:
- Full pricing table for all 24 fields
- Scenario comparisons (Engineering vs Philosophy)

### 2. Calculate Custom Scenarios

```python
from pricing_engine import LoanPricingModel

# Initialize model
model = LoanPricingModel(
    data_path="../data/field_risk_scores.json",
    base_rate=5.50  # Current federal rate
)

# Price a loan for a specific field
pricing = model.price_loan(
    field="Computer Science",
    loan_amount=40000,
    apply_fairness=True,
    family_income=35000
)

print(f"Interest Rate: {pricing['adjusted_rate']:.2f}%")
print(f"Monthly Payment: ${pricing['monthly_payment']:.2f}")
print(f"Total Paid: ${pricing['total_paid']:,.2f}")
```

### 3. Generate Full Pricing Table

```python
# Without fairness adjustments (pure risk-based)
table = model.generate_pricing_table(apply_fairness=False)
print(table[['field', 'adjusted_rate', 'monthly_payment']])

# With fairness adjustments
fair_table = model.generate_pricing_table(apply_fairness=True)
print(fair_table[['field', 'adjusted_rate', 'monthly_payment']])
```

### 4. Compare Multiple Scenarios

```python
# Compare all scenarios for a specific field
scenarios = model.compare_scenarios('Business/Management', loan_amount=30000)
print(scenarios[['scenario', 'adjusted_rate', 'monthly_payment']])
```

## Key Results (Quick Reference)

### Interest Rate Range
- **Lowest:** Engineering (5.86%)
- **Highest:** Philosophy/Religion (6.17%)
- **Spread:** 0.32 percentage points

### Monthly Payment ($30k loan, 10yr)
- **Lowest:** Architecture ($330.81)
- **Highest:** Philosophy ($335.55)
- **Difference:** $4.74/month ($569 over life of loan)

### With Fairness Adjustments (Low-Income)
- **Engineering:** 4.82% (saves $15.38/month)
- **Philosophy:** 4.27% (saves $28.02/month)

## Customization

### Change Base Rate
```python
model = LoanPricingModel(data_path="...", base_rate=6.00)  # 6% base
```

### Adjust Fairness Parameters
Edit `_fairness_adjustment()` method in `pricing_engine.py`:
- Income thresholds
- Subsidy amounts
- Risk scaling factors

### Use Different Recovery Rate
```python
pricing = model.price_loan(
    field="Education",
    loan_amount=30000
)
# Modify calculate_risk_premium() to change recovery_rate parameter
```

## Next Steps

1. **Read Full Analysis:** `docs/initial_findings.md`
2. **Understand Methodology:** `README.md` → Methodology section
3. **Explore Data:** `data/field_risk_scores.json`
4. **Build Interactive Tool:** Coming soon (HTML/JavaScript calculator)

## Common Questions

**Q: Why is the spread so small (0.32 pp)?**  
A: Most fields have similar default risk when controlling for institution quality. Extreme outliers (for-profit schools) are excluded from field-level analysis.

**Q: How are default probabilities estimated?**  
A: `Default_Prob = 0.15 × Underemployment_Rate + 0.05`, calibrated to match national 3-year cohort default rate (~10%).

**Q: What about income-driven repayment?**  
A: Current model assumes standard 10-year repayment. IBR/PAYE plans would reduce effective costs but don't eliminate default risk.

**Q: Can I use institutional data instead of field data?**  
A: Yes! The model can be extended to use institution-level default rates. Contact author for assistance.

## Contact

**Isaiah Kamrar**  
Email: rawrdog92@yahoo.com  
GitHub: @kamrawr

## License

CC-BY-4.0 - Attribution required
