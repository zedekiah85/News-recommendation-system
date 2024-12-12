import streamlit as st
import joblib
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the vectorizer and cosine similarity matrix
@st.cache_resource
def load_model():
    vectorizer = joblib.load('vectorizer.pkl')
    cosine_sim = joblib.load('cosine_sim.pkl')
    return vectorizer, cosine_sim

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    df['combined_text'] = df['headline'] + ' ' + df['short_description']
    return df

# Load models and data
vectorizer, cosine_sim = load_model()
df = load_data()

# Define recommendation function with category filtering
def get_recommendations(category, cosine_sim=cosine_sim, df=df):
    # Check if the article with the specified category exists
    matching_rows = df[df['category'] == category]
    
    if matching_rows.empty:
        st.warning(f"No article found with the category: {category}.")
        return
    
    # Get the index of the first article that matches the category
    idx = matching_rows.index[0]

    # Get pairwise similarity scores for all articles with the selected article
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort articles by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices of the top 5 most similar articles within the same category
    recommendations = [
        i for i in sim_scores if df.iloc[i[0]]['category'] == category and i[0] != idx
    ][:5]

    # Display recommended articles
    if recommendations:
        for i in recommendations:
            st.write(f"*Category:* {df.iloc[i[0]]['category']}")
            st.write(f"*Description:* {df.iloc[i[0]]['short_description']}\n")
            st.write(f"*links:* {df.iloc[i[0]]['links']}")
    else:
        st.warning("No similar articles found within the same category.")

# Streamlit user interface
st.title("News Article Recommendations")

category = st.text_input("Enter the category of interest (e.g., environment, politics, u.s news, comedy, parenting, world news, culture art, tech, sport, entertainment, politic, weird news, environment, education, crime, science, wellness, business, style beauty, food drink, medium, queer voice, home living, woman, black voice, travel.etc.):")

if st.button("Get Recommendations"):
    if category:
        get_recommendations(category)
    else:
        st.warning("Please enter a category to get recommendations.")
