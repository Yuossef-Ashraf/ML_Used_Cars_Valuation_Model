# Automotive Resale Valuation & Used Car Pricing Engine - Architecture & Pipeline Design

```mermaid
graph TD
    DataInput[Raw CSV Dataset: used_cars_powerful.csv] --> Preproc[Data Cleaning & Column Transformer]
    Preproc -->|Numeric| Scaler[StandardScaler Normalization]
    Preproc -->|Categorical| Encoder[One-Hot Categorical Encoding]
    Scaler --> Split[Train/Test Stratified Split 80/20]
    Encoder --> Split
    Split --> Train[Model Training: XGBoost Regressor]
    Train --> Eval[Evaluation & Benchmarks]
    Eval --> Inference[Production Inference & CLI]
```

## Comparative Models Evaluated
- **XGBoost Regressor**
- **Random Forest Regressor**
- **Gradient Boosting**
- **Linear Regression**
