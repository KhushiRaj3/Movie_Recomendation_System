# Movie Recommendation System

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


movies = pd.read_csv("D:/Movie_Recomendation_system/data.csv/movie.csv")

print("Movies dataset sample:")
print(movies.head())


movies['genres'] = movies['genres'].str.replace('|', ' ')


indices = pd.Series(movies.index, index=movies['title']).drop_duplicates()


vectorizer = CountVectorizer(stop_words='english')
vectorizer.fit(movies['genres'])

def recommend(title=None, genre=None, n=5):
    """
    Recommend movies based on title and/or genre.
    At least one of title or genre must be provided.
    """
    if not title and not genre:
        return "Please provide at least a movie title or a genre to get recommendations."
    
  
    if genre:
        filtered = movies[movies['genres'].str.contains(genre, case=False)]
        if filtered.empty:
            return f"No movies found in genre '{genre}'"
    else:
        filtered = movies

  
    if title:
        if title not in indices:
            return f"Movie '{title}' not found."
        
        
        if title in filtered['title'].values:
            title_idx = filtered.index.get_loc(indices[title])
        else:
            return f"Movie '{title}' not found in genre '{genre}'" if genre else f"Movie '{title}' not found."
        
        
        filtered_matrix = vectorizer.transform(filtered['genres'])
        sim_scores = cosine_similarity(filtered_matrix[title_idx], filtered_matrix).flatten()
        sorted_indices = sim_scores.argsort()[::-1][1:n+1]  
        
        recommended = filtered.iloc[sorted_indices]['title']
        return recommended

    
    return filtered['title'].head(n)


movie_input = input("Enter a movie title (or leave blank): ").strip()
genre_input = input("Enter a genre (or leave blank): ").strip()

movie_input = movie_input if movie_input else None
genre_input = genre_input if genre_input else None

print("\nRecommended movies:")
print(recommend(movie_input, genre_input))
