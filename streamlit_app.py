import streamlit as st
import pandas as pd
import joblib

st.title("🛒 Product Reorder Recommender")

# Load model + predictions
preds = pd.read_csv("user_product_predictions.csv")

user_ids = preds['user_id'].unique()
user_id = st.selectbox("Choose a user ID", user_ids)

# Show top products
user_recs = preds[preds['user_id'] == user_id].sort_values('reorder_proba', ascending=False)

st.subheader("Top Product Recommendations:")
st.dataframe(user_recs[['product_id', 'reorder_proba']])
