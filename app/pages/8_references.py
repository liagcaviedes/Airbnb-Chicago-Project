import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

#----------------------HEADER-------------------------#

st.markdown(f"<h1 style='color: {header_color};'>References</h1>", unsafe_allow_html=True)

import streamlit as st

# Define el estilo para los enlaces
st.markdown("""
<style>
a {
    color: #767676;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# Crea los enlaces
st.markdown("[Inside Airbnb](https://insideairbnb.com/chicago/)")
st.markdown("[NBER. National Bureau of Economic Research](https://www.nber.org/)")
st.markdown("[AirDNA](https://www.airdna.co/)")
st.markdown("[World Business Chicago](https://worldbusinesschicago.com/)")
st.markdown("[Enjoy Illinois. Economic Impact of Visitors in Illinois](https://www.enjoyillinois.com/assets/Files-PDFs/Illinois-Tourism-Economic-Impact-2024.pdf)")
st.markdown("[Crain's Chicago Business](https://www.chicagobusiness.com/)")
