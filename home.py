import streamlit as st
import pickle

with open("pkl/metrics.pkl", 'rb') as file:
    metrics = pickle.load(file)

st.title("Fastball Prediction")

st.metric("Accuracy", f"{metrics['accuracy']:.2%}")
st.metric("Recall", f"{metrics['recall']:.2%}")
st.metric("f1", f"{metrics['f1']:.2%}")
st.markdown("#")
st.image("graphs/confusion_matrix.png", caption="Confusion Matrix for test data (1 is fastball 0 is offspeed/breaking)")
st.markdown("#")
st.image("graphs/feature_importance.png", caption="The importance of each feature used in the model")
st.markdown("#")
st.image("graphs/fastball_pie_chart.png", caption="Pie chart showing fastball vs offspeed/breaking")
st.markdown("#")
st.write(
"""
I set out on the challenge of trying to predict whether the next pitch in a MLB game would be a fastball or not using a random forest classifier.
This would be a very challenging task as when pitchers and catchers call pitches they are trying to be unpredictable,
so that they can catch the hitter off guard. My dataset was all pitches thrown in the 2024 season. As 
shown in the pie chart fastballs were thrown 54.9% of the time. The accuracy of my model was 62.29% which was notable 
improvement  over simply guessing fastball everytime. The model had an even better recall score of 67.75% which is good because 
in baseball you would prefer to guess fastball and then adjust for the offspeed/breaking. As we can see in the confusion matrix the
majority of the models misses are type 2 error and there are considerably less type 1 error. The model found that the most 
influential features in predicting the next pitch were the pitcher's fastball percentage on the seaon, the number of strikes in the count,
and the number of balls in the count.
"""
)