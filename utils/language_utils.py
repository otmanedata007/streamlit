from googletrans import Translator

# Initialisation du traducteur
translator = Translator()

def get_synopsis_in_language(description, lang='fr'):
    try:
        if lang == "fr":
            # Traduction de l'anglais vers le français si la langue choisie est le français
            translated = translator.translate(description, src='en', dest='fr')  # Traduction vers le français
            return translated.text
        else:
            return description  # Le synopsis est déjà en anglais par défaut
    except Exception as e:
        return description  # Retourner le texte original en cas d'erreur

def render_language_selector():
    with st.sidebar:
        st.write("### Choisir la langue")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('🇫🇷', key="fr"):
                st.session_state.language = "fr"
        with col2:
            if st.button('🇬🇧', key="en"):
                st.session_state.language = "en"
