# 📊 Customer Support Ticket Analysis & Prediction

### **Download Links for Required Technologies**
- 🐍 **Python** → [Download Python 3.9+](https://www.python.org/downloads/)
- 🌐 **Flask** → [Flask Official Documentation](https://flask.palletsprojects.com/en/latest/)
- 📈 **Pandas & NumPy** → [Documentation](https://pandas.pydata.org/)
- 📊 **Matplotlib & Seaborn** → [Visualization Docs](https://matplotlib.org/)
- 🤖 **Scikit-learn** → [Installation Guide](https://scikit-learn.org/stable/install.html)
- ⚡ **XGBoost** → [XGBoost Installation Guide](https://xgboost.readthedocs.io/en/stable/install.html)

---

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Objectives](#objectives)
- [Approach & Methods](#approach--methods)
- [Results](#results)
- [Repository Structure](#repository-structure)
- [Setup & Usage](#setup--usage)
- [Requirements (inline)](#requirements-inline)
- [Visualizations](#visualizations)
- [Limitations](#limitations)
- [Future Work](#future-work)
- [Acknowledgements](#acknowledgements)
- [License](#license)
- [Contact](#contact)

---

## Overview
The **Customer Support Ticket Analysis & Prediction** project is a complete data science and web application solution that:  
- Analyzes **customer support tickets** for insights.  
- Builds predictive models to estimate **customer satisfaction ratings (1–5 stars)**.  
- Offers an interactive **Flask web app** where users can input ticket details and get real-time predictions.  

---

## Dataset
- **File:** `customer_support_tickets.csv`  
- **Rows × Columns:** ~5000 × 7 (core dataset)  
- **Features Used in Web App Form (from `app.py`):**
  - Ticket ID, Customer Name, Customer Email, Customer Age, Gender  
  - Product Purchased, Ticket Type, Ticket Status, Resolution  
  - Ticket Priority, Ticket Channel, First Response Time, Time to Resolution  
  - Ticket Subject, Ticket Description, Date of Purchase  

- **Target:**
  - Predicted **Customer Satisfaction Rating (1–5 stars)**

---

## Objectives
1. Perform **EDA** and gain insights from customer support ticket data.  
2. Build machine learning models to predict satisfaction ratings.  
3. Deploy trained pipeline (`pipeline.pkl`) in a **Flask application**.  
4. Allow real-time predictions and probability outputs via a web form.  

---

## Approach & Methods
- **Preprocessing:** Handle missing values, encoding, scaling.  
- **Imbalance Handling:** Applied resampling when needed.  
- **Modeling:** Logistic Regression, Random Forest, XGBoost (best performing).  
- **Web App:** Flask integration with a saved **pipeline.pkl**.  
- **Evaluation:** Accuracy, Precision, Recall, F1-score.  

---

## Results
- Example model performance (XGBoost):  
  - Accuracy: ~0.85  
  - Precision: ~0.83  
  - Recall: ~0.84  
  - F1-score: ~0.835  
- Flask app outputs:  
  - **Predicted Satisfaction:** e.g., “4 / 5”  
  - **Probability Distribution:** e.g., `1★: 0.05, 2★: 0.10, 3★: 0.20, 4★: 0.40, 5★: 0.25`

---

## Repository Structure
```
customer_support_analysis/
├─ app.py                   # Flask app (prediction interface)
├─ pipeline.pkl             # Trained ML pipeline (preprocessing + model)
├─ metrics.txt              # Saved evaluation metrics
├─ templates/
│   └── index.html          # Web UI form
├─ Customer.ipynb           # Jupyter Notebook (EDA + modeling)
├─ customer_support_tickets.csv # Dataset
└─ README.md                # Documentation
```

---

## Setup & Usage
### 1. Clone Repository
```bash
git clone https://github.com/Zakir-ai/customer-support-analysis.git
cd customer-support-analysis
```
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
### 3. Run Flask App
```bash
python app.py
```
Visit: **http://127.0.0.1:5000/**  

---

## Requirements (inline)
```
flask
pandas
numpy
matplotlib
seaborn
scikit-learn
xgboost
```

---

## Visualizations
- Ticket category distribution  
- Priority vs resolution time  
- Correlation heatmap  
- Confusion matrix  

---

## Limitations
- Dataset lacks **text analysis** of ticket descriptions.  
- Predictions depend on numeric/categorical features only.  

---

## Future Work
- Integrate **NLP models** for analyzing descriptions.  
- Add **SHAP explainability** to web app.  
- Deploy app on **Render / Hugging Face Spaces**.  

---

## Acknowledgements
- Libraries: Flask, pandas, scikit-learn, matplotlib, seaborn, XGBoost  
