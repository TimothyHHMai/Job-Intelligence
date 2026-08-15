import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Job Market Intelligence: Resume Matcher")
st.write("Upload or paste a candidate resume to find top-matching job listings.")

user_resume = st.text_area("Paste Resume Text Here:")

if st.button("Find Matching Jobs"):
    if user_resume.strip():
        # Replace this path with the exact folder path where your job_clean.csv is saved
      
        job_df = pd.read_csv('job_clean.csv').dropna(subset=['clean_description'])
        
        # Quick inference vectorization
        vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
        job_vectors = vectorizer.fit_transform(job_df['clean_description'])
        user_vec = vectorizer.transform([user_resume])
        
        similarities = cosine_similarity(user_vec, job_vectors).flatten()
        top_indices = similarities.argsort()[::-1][:5]
        
        st.subheader("Top Matching Roles:")
        for idx in top_indices:
            st.markdown(f"**Score:** {similarities[idx]:.4f}")
            st.write(job_df.iloc[idx]['clean_description'][:400] + "...")
            st.markdown("---")
    else:
        st.warning("Please enter some resume text first.")