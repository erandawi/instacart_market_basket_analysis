# 🛒 Product Recommendation System

This is a **machine learning-based recommendation system** built using the [Instacart Market Basket Analysis](https://www.kaggle.com/competitions/instacart-market-basket-analysis) dataset. The goal is to predict which products a user will reorder in their next purchase and recommend the most relevant items.

## 🚀 Features

- ✅ End-to-end ML pipeline: EDA → Feature Engineering → Model Training → Evaluation
- ✅ Model trained with **XGBoost** + class imbalance tuning
- ✅ Evaluated using **AUC, F1-score, and Recall**
- ✅ Threshold tuning for optimal precision/recall trade-off
- ✅ Deployed on **Streamlit Cloud** with interactive UI
- ✅ Clean, modular code & ready for production

---

## 🧠 Problem Statement

**Objective**: Predict whether a user will reorder a product in their next order based on past purchase behavior.

This is a **binary classification problem**, where:
- `1 = product will be reordered`
- `0 = product will not be reordered`

The challenge is dealing with **severe class imbalance** and optimizing recall without overpredicting.

---

## 📊 Model Performance

| Metric        | Value       |
|---------------|-------------|
| AUC           | `0.82`      |
| Class 1 Recall | `90%`       |
| Class 1 Precision | `17%`   |
| Accuracy      | `55%`       |

---

## 🧱 Tech Stack

- `Python`
- `pandas`, `NumPy`
- `XGBoost`, `Scikit-learn`
- `Streamlit` for web app
- `joblib` for model persistence
- `Git` + `GitHub` for version control

---

## 🧪 Project Structure

```
product-recommender/
│
├── notebooks/experiments.ipynb
│    
├── models/xgb_reorder_model.pkl
│ 
├── prediction/user_product_predictions.csv
│ 
├── streamlit_app.py
│ 
├── requirements.txt
│ 
└── README.md
```

---

## 🗅️ Streamlit App Demo

🔗 [Live Demo](https://your-streamlit-app-link.streamlit.app) *(replace with your actual app link)*

### Preview:
Upload a user ID and get top product recommendations with reorder probabilities.

---

## 💪 How to Run Locally

```bash
git clone https://github.com/yourusername/product-recommender.git
cd product-recommender

# Create environment (optional)
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

---

## 📦 Dataset

- 📦 Kaggle: [Instacart Market Basket Analysis](https://www.kaggle.com/competitions/instacart-market-basket-analysis)

> This dataset contains 3 million grocery orders from over 200,000 users.

---

## 📊 Future Improvements

- Personalized ranking using user-product embeddings
- Use sequence-based models (RNN/Transformer) for better modeling reorder patterns
- Integration with product images and descriptions

---

## 👨‍💻 Author

**Eranda Wijewantha**  
Data Analyst | Freelance Data Scientist  