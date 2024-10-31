import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

#----------------------HEADER-------------------------#

st.markdown(f"<h1 style='color: {header_color};'>What's next</h1>", unsafe_allow_html=True)

st.markdown(f"<h6 style='color: {header_color};'>Insights and recommendations</h2>", unsafe_allow_html=True)

st.subheader(' ⬆️ Increase revenue per reservation')
st.markdown("""
    - Regulations might affect the number of listings in the future causing a decrease in revenue.
    - Price increases trends might affect demand or there might not be room for grow by ADR.
    - Look for opportunities to increase the revenue generated per reservation.
        - Superhost program to drive income growth.
        - Fees Structures
        - New Products. 
""")

st.subheader('⚖️ Regulations')
st.markdown("""
    - Review listings to ensure they have the required license.
    - Verify listings with over 90 nights booked annually to confirm the host resides on the property.
""")