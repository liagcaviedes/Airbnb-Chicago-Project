import streamlit as st

st.set_page_config(page_title="Airbnb Analytics", page_icon="🏠")

# Colores de Airbnb
header_color = "#FF5A5F"  # Rojo
text_color = "#484848"  # Gris oscuro
background_color = "#FFFFFF"  # Blanco

#----------------------HEADER-------------------------#

st.markdown(f"<h1 style='color: {header_color};'>Hypothesis Test.</h1>", unsafe_allow_html=True)

st.markdown(f"<h6 style='color: {header_color};'>Superhost Vs Prices</h2>", unsafe_allow_html=True)

st.write("")

st.subheader('Null Hypothesis')
st.markdown("""
There is no significant difference in the average price between superhosts and non-superhosts.
""")

st.subheader('Shaphiro-Wilk Test')
st.markdown("""
- Results:
    - p-value for superhosts: 0.0
    - p-value for non-superhosts: 0.0
- Interpretation: 
    - A p-value of 0.0 evidence against the null hypothesis that the data follows a normal distribution.
""")
st.image('img/host_price_distribution.png', use_column_width=True)

st.subheader('Mann-Whitney Test')
st.markdown("""
- Results:
    - p-value: 1.4746533536159162e-10
- Interpretation: 
    - The extremely low p-value from the Mann-Whitney test indicates a significant difference between the prices of superhosts and non-superhosts. 
    - This suggests that the prices in these two groups are not only different, but that this difference is statistically significant, implying that the superhost status has a meaningful impact on pricing strategies in the Airbnb market.
""")
st.subheader('Conclusions')
st.markdown("""
Increasing number of superhosts is directly related to higher prices. Hence, the superhost status has a meaningful impact on pricing strategies in the Airbnb market.
""")
