import streamlit as st

homePage = st.Page("home.py", title="Home")
predictPage = st.Page("predict.py", title="Predictions")

pg = st.navigation([homePage, predictPage])

pg.run()