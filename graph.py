import streamlit as st
import pickle

with open("metrics.pkl", 'rb') as file:
    metrics = pickle.load(file)

st.title("Graphs")

st.metric("Accuracy", f"{metrics['accuracy']:.2%}")
st.metric("Recall", f"{metrics['recall']:.2%}")
st.metric("f1", f"{metrics['f1']:.2%}")
st.image("confusion_matrix.png", caption="Confusion Matrix for test data (1 is fastball 0 is offspeed/breaking)")
st.image("feature_importance.png", caption="The importance of each feature used in the model")
st.image("fastball_pie_chart.png", caption="Pie chart showing fastball vs offspeed/breaking")
