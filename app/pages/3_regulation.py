import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

#----------------------HEADER-------------------------#

st.markdown(f"<h1 style='color: {header_color};'>Short-Term Rentals Regulation.</h1>", unsafe_allow_html=True)
st.markdown(f"<h6 style='color: {header_color};'>Airbnb Compliance Overview</h2>", unsafe_allow_html=True)

st.write("")

st.subheader('Licenses')
st.markdown("""
19% of the listings do not have a license.
""")
st.image('img/licenses.png', use_column_width=True)
st.write("")
st.write("")
st.write("")
st.subheader('Annual Stays')
st.markdown("""
Regulation indicates that the maximum number of nights that a property can be rented is 90 nights per year. 

We observe that most properties are under this limit. 

If the host lives in the property, there is no cap on the number of nights that the property can be rented.
""")
st.write("")
st.write("")
st.write("")
st.image('img/noches.png', use_column_width=True)