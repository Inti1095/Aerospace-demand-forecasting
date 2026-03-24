# ✈️ Aerospace Demand Forecasting & Inventory Optimization

## 📌 Overview
This project is an end-to-end data science pipeline designed to forecast aerospace demand and optimize inventory decisions under uncertainty. It simulates real-world supply chain challenges such as demand variability, shortages, and excess inventory.

The system integrates data processing, feature engineering, time-series forecasting, and output generation into a single executable pipeline.

---

## 🎯 Business Problem
In aerospace supply chains, inaccurate demand forecasts can lead to:
- Inventory shortages → delayed operations
- Excess inventory → increased holding costs
- Reduced service levels and delivery performance

This project addresses these challenges by building predictive models and simulation-driven insights to improve forecast accuracy and support decision-making.

---

## 🏗️ Architecture
data/ (raw → processed)
↓
src/data_processing.py
↓
src/feature_engineering.py
↓
src/forecasting_model.py
↓
run_pipeline.py
↓
outputs/forecasts.csv


---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Statsmodels (ARIMA)
- Scikit-learn
- Matplotlib

---

## 📊 Features
- Data ingestion and cleaning pipeline
- Time-series feature engineering (lags, rolling metrics)
- ARIMA-based demand forecasting
- Forecast evaluation (RMSE)
- End-to-end pipeline execution
- Output generation for decision support

---

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt


