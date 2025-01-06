import pandas as pd
import streamlit as st

@st.cache_data
def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df.rename(columns={'Titre': 'Title', 'Genres': 'Genres', 'Année': 'Year',
                       'Moyenne': 'Vote_average', 'Synopsis': 'Description', 'Durée': 'Duration'}, inplace=True)
    df['All_Actors'] = df[['Acteur_1', 'Acteur_2', 'Acteur_3', 'Acteur_4', 'Acteur_5']].fillna('').agg(', '.join, axis=1)
    df['Genres'] = df['Genres'].fillna('')
    df['All_Actors'] = df['All_Actors'].str.strip()
    df['Description'] = df['Description'].fillna('Description indisponible.')
    df['Title'] = df['Title'].str.strip().str.lower()
    df['URL_AFFICHE'] = df['URL_AFFICHE'].fillna('placeholder.jpg')  # Gérer les affiches manquantes
    return df
