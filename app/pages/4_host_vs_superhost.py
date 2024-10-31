import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

#----------------------HEADER-------------------------#

st.markdown(f"<h1 style='color: {header_color};'>Host Vs SuperHost</h1>", unsafe_allow_html=True)

st.write("")
st.write("")

st.subheader('How to become a Superhost?')
st.markdown("""
- Response Rate:  + 90% .
- Minimum Stays: 10 stays in a year or 3 reservations.
- Ratings: Minimum 4.8.
- Cancellations: No unnecessary cancellations.
""")

st.subheader('Host Strategies')
st.markdown("""
- Hosts may choose to become Superhosts to increase their visibility on the platform.
- Fees models:
    - Split Fee Structure: Both guests and hosts pays. Guests 14%, host 3%. 
    - Simplified Fee Structure: Only hosts pays, 14-16%. 
Those who understand the implications of these fees may actively manage their prices and promotional offers to enhance visibility. 
""")

st.subheader('Price')
st.markdown("""
Superhosts listings have higher prices.
""")
st.image('img/price_vs_superhost.png', use_column_width=True)

st.write("")
st.write("")
st.write("")
st.subheader('Review Score')
st.markdown("""
The increase in prices has had an impact on the Review Score.
Although prices have been rising since 2017, we observed another peak in 2020, coinciding with the moment when the review score began to decrease. 
This decline is particularly noticeable in the value-for-money category, which is rated the lowest.
""")
st.write("")
st.write("")
st.write("")
st.image('img/host_vs_review_score.png', use_column_width=True)


st.write("")
st.write("")
st.write("")
st.subheader('Superhost Program Evolution')
st.markdown("""
Superhost program has been growing since 2017, indicating that more hosts are interested in becoming Superhosts.
""")
st.write("")
st.write("")
st.write("")
st.image('img/hosts_vs_number_reviews.png', use_column_width=True)


