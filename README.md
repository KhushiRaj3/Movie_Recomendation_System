# Movie Recommendation System

A Python-based content recommendation system that suggests movies based on genre and/or a reference movie title. Designed for flexibility, fast execution, and interactive use.

This project demonstrates the use of Python, Pandas, and Scikit-learn to build a **content-based movie recommender**. It’s interactive, portfolio-ready, and showcases real-world problem-solving with machine learning concepts.

---

## Features

- Recommend movies by **title**, **genre**, or **both**.  
- Handles missing or unmatched titles/genres gracefully.  
- Modular, human-readable Python code suitable for portfolio demos.  
- Uses cosine similarity to compute similarity between movies based on genres.  
- Flexible input options:  
  - If both title and genre are provided, recommendations are filtered by genre and similarity to the given title.  
  - If only a title is provided, it recommends movies similar to the title.  
  - If only a genre is provided, it recommends top movies in that genre.  

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/Movie_Recomendation_system.git
```
2.Navigate to the project folder:
```bash
cd Movie_Recomendation_system
```
3. Install dependencies:
 ```bash
pip install -r requirements.txt
```
Usage
```bash
Run the recommender script:
python src/recommender.py
```
Dataset
```bash
The dataset movie.csv should be placed in the data/ folder.

The CSV must include at least the following columns: movieId, title, and genres.

Genres are space-separated for processing.
```
Technologies Used
```bash
Python 3.11+

Pandas for data handling

Scikit-learn for vectorization and similarity computation
```
Future Improvements
```bash
Add collaborative filtering for personalized recommendations.

Build a web interface for interactive use.

Include user ratings and feedback for hybrid recommendations.
```
---
