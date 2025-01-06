import streamlit as st

def display_movie_with_synopsis(row, synopsis):
    st.markdown(f"""
        <div class="movie-container">
            <img src="{row['URL_AFFICHE']}" class="movie-poster" alt="{row['Title']}">
            <div class="movie-synopsis">
                <p>{synopsis}</p>
            </div>
            <div style="color: white; padding: 10px 0 0 0;">
                <strong>Année de sortie :</strong> {int(row['Year'])}<br>
                <strong>⭐ Note :</strong> {row['Vote_average']}<br>
                <strong> {row['Genres']}<br>  <!-- Affichage du genre -->
                <strong>Acteurs :</strong> {clean_actor_list(row['All_Actors'])}
            </div>
        </div>
    """, unsafe_allow_html=True)

def clean_actor_list(actor_list):
    return ', '.join([actor.strip() for actor in actor_list.strip("[]").replace("'", "").split(",")])
