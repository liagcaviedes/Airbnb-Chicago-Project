import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

#----------------------HEADER-------------------------#

st.markdown(f"<h1 style='color: {header_color};'>Chicago Highlights</h1>", unsafe_allow_html=True)
st.image('img/high2.png', use_column_width=True)
#----------------------PAGE CONTENT-------------------------#

