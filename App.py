import streamlit as st

homePage = st.Page("home.py", title="Home")
graphPage = st.Page("graph.py", title="Graphs")
predictPage = st.Page("predict.py", title="Predictions")

pg = st.navigation([homePage, graphPage, predictPage])

pg.run()