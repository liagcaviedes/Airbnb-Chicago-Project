import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

st.markdown(f"<h1 style='color: {header_color};'>Market Dashboard</h1>", unsafe_allow_html=True)

st.components.v1.iframe('https://app.fabric.microsoft.com/view?r=eyJrIjoiZmI1Nzg1Y2ItOTVlOS00YjMyLWE3NDMtMTRlNmRjYTQwYzUyIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9', height=800, width=1000)

st.markdown("""
Estimated Roomnights and Total Income are calculated with reviews, price and minimum stays data with an estimated ratio of 30% guest reviews.
""")