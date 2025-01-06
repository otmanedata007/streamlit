from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def knn_recommendations(movie_title, df, k=5):
    df['Titre_normalized'] = df['Title'].str.strip().str.lower()
    movie_title_normalized = movie_title.strip().lower()

    if movie_title_normalized not in df['Titre_normalized'].values:
        return pd.DataFrame()

    features = ['Vote_average', 'Duration', 'Genres', 'All_Actors']
    X = df[features].dropna()

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['Vote_average', 'Duration']),
            ('cat', OneHotEncoder(handle_unknown='ignore'), ['Genres', 'All_Actors'])
        ]
    )

    pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('knn', NearestNeighbors(n_neighbors=k, metric='euclidean'))
    ])

    X_transformed = pipeline['preprocessor'].fit_transform(X)
    pipeline['knn'].fit(X_transformed)

    movie_index = df[df['Titre_normalized'] == movie_title_normalized].index[0]
    movie_features = X.iloc[movie_index:movie_index+1]
    movie_transformed = pipeline['preprocessor'].transform(movie_features)

    distances, indices = pipeline['knn'].kneighbors(movie_transformed)

    similar_movies = df.iloc[indices[0]]
    return similar_movies
