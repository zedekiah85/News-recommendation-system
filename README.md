# News Recommendation Sytem
This project is a content-based news recommendation system built using Python and Streamlit. It recommends news articles to users based on a specific category they are interested in. The application utilizes a cosine similarity matrix to identify and recommend articles that are most similar to the user's preference. Basing on my dataset these are the categories that can be recommended:u.s news, comedy, parenting, world news, culture art, tech, sport, entertainment, politic, weird news, environment, education, crime, science, wellness, business, style beauty, food drink, medium, queer voice, home living, woman, black voice, travel.

This is the link to the streamlit app: https://newsrecommendationsytemcapstoneproject-dzjzihfmlyrnnyjgoes4lw.streamlit.app/

## Features
  1. Category-Based Recommendations: Enter a category (e.g., politics, sports, 
     environment) to get tailored news recommendations.
  2. Cosine Similarity: Leverages cosine similarity to find the most relevant 
     articles.
  3. Interactive Web App: Built with Streamlit for an easy-to-use and visually 
     appealing interface.
  4. Dynamic Search: Case-insensitive search for flexible and robust category 
     matching.

## Technologies Used
 1. Python
 2. Streamlit (for the interactive web interface)
 3. Pandas (for data manipulation)
 4. scikit-learn (for cosine similarity)
 5. Joblib (for saving and loading the vectorizer and similarity matrix)
 6. Jupyter Notebook (for model development)

## Dataset
1000 rows were used to train this model.
The dataset (data.csv) has already been processed and contains the following columns:

  1. headline: The title of the article.
  2. short_description: A brief summary of the article.
  3. category: The article's category (e.g., sports, business, environment).
  4. links: URL to the full article.

This is the link to the original dataset: https://www.kaggle.com/datasets/rmisra/news-category-dataset it is in the json format.


## Project Files
  1.  news-recommendation-system.ipynb: Jupyter Notebook with the code for 
      generating the vectorizer and cosine similarity matrix.
  2.  vectorizer.pkl: Saved TF-IDF vectorizer.
  3. cosine_sim.pkl: Pre-computed cosine similarity matrix.
  4. data.csv: Dataset containing news articles, categories, and descriptions.
  5. app.py: Streamlit app for running the recommendation system.
  6. README.md: This file.
