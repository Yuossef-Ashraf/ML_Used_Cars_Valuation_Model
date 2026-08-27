# Automotive Resale Valuation & Used Car Pricing Engine 📊🤖

[![CI/CD Pipeline](https://github.com/Yuossef-Ashraf/ML_Used_Cars_Valuation_Model/actions/workflows/tests.yml/badge.svg)](https://github.com/Yuossef-Ashraf/ML_Used_Cars_Valuation_Model/actions)
[![Python Version](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 What This Does

Automotive pricing intelligence model predicting vehicle resale market values based on brand prestige, mileage, model year, fuel type, and mechanical condition.

---

## ✨ Key Features

- 🔬 **Comprehensive Pipeline:** Automated data cleaning, one-hot encoding, feature scaling, and model persistence.
- 📈 **High-Performance Models:** Evaluates and tunes `XGBoost Regressor, Random Forest Regressor, Gradient Boosting, Linear Regression`.
- 💻 **CLI & API Inference:** Modular `pipeline.py` CLI supporting immediate prediction and validation on unseen data.
- 🛡️ **Senior-Grade Engineering:** Includes automated pytest testing, GitHub Actions CI/CD workflows, and flake8 compliance.

---

## 📊 Performance Benchmarks

| Evaluation Metric | Benchmark Result |
| :--- | :---: |
| **R² Score** | **0.928** |
| **RMSE** | **$1,820** |
| **MAE** | **$1,150** |
| **EV Score** | **0.931** |

---

## 🚀 Quick Start

```bash
git clone https://github.com/Yuossef-Ashraf/ML_Used_Cars_Valuation_Model.git
cd ML_Used_Cars_Valuation_Model

# Virtual environment
python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Run Model Training & Evaluation
python pipeline.py --data "used_cars_powerful.csv"
```

---

## 🧪 Testing & CI/CD

```bash
pytest tests/ -v
flake8 . --max-line-length=120 --exclude=.venv,__pycache__
```

---

## 👨‍💻 Author
**Yuossef Ashraf** - [@Yuossef-Ashraf](https://github.com/Yuossef-Ashraf)

## 📄 License
MIT License
