import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

#----------------------HEADER-------------------------#

st.markdown(f"<h1 style='color: {header_color};'>Market Trends</h1>", unsafe_allow_html=True)
st.markdown(f"<h6 style='color: {header_color};'>Higher prices, fewer listings</h2>", unsafe_allow_html=True)

st.write("")

st.subheader('Price Evolution Vs Total Reviews')
st.markdown("""
Since 2017 we see an increase in the number of prices and also in the number of reviews, indicating the growth of the platform.
""")
st.image('img/reviewspermonth.png', use_column_width=True)

st.write("")
st.write("")
st.write("")
st.subheader('Price Vs Review Score')
st.markdown("""
The increase in prices has had an impact on the Review Score.
Although prices have been rising since 2017, we observed another peak in 2020, coinciding with the moment when the review score began to decrease. 
This decline is particularly noticeable in the value-for-money category, which is rated the lowest.
""")
st.write("")
st.write("")
st.write("")
st.image('img/price_vs_review_score.png', use_column_width=True)


st.write("")
st.write("")
st.write("")
st.subheader('Listings Evolution')
st.markdown("""
We observe a decrease in the number of listings since 2017 due to the regulations imposed by the city of Chicago.
This trend indicates that as the number of listings decreases, prices tend to increase due to the supply-demand relationship.
""")
st.write("")
st.write("")
st.write("")

st.image('img/regulations.jpg', use_column_width=True)

