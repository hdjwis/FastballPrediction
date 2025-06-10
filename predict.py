import streamlit as st
import pickle
import pandas as pd


with open("pkl/model.pkl", 'rb') as file:
    model = pickle.load(file)

st.title("Prediction")
st.subheader("Enter a value for each spot")

balls = st.selectbox("# of balls", (0, 1, 2, 3))
strike = st.selectbox('# of strikes', (0, 1, 2))
runner_on_1b = st.selectbox('Is there a runner on 1st?', ('Yes', 'No'))
runner_on_2b = st.selectbox('Is there a runner on 2nd?', ('Yes', 'No'))
runner_on_3b = st.selectbox('Is there a runner on 3rd?', ('Yes', 'No'))
outs = st.selectbox('How many outs when the batter is up?', (0, 1, 2))
inning = st.text_input('What is the inning?')
n_thruorder = st.text_input('What time through the order is it for the pitcher?')
fastball_percentage = st.text_input('What percent of the time does the pitcher throw a fastball?')

if st.button('Predict') and inning and n_thruorder and fastball_percentage:         
    data =  pd.DataFrame(
            {
                        'balls' : [balls], 
                        'strikes' : [strike], 
                        'on_3b' : [1 if runner_on_3b == 'yes' else 0],
                        'on_2b' : [1 if runner_on_2b == 'yes' else 0],
                        'on_1b' : [1 if runner_on_1b == 'yes' else 0],   
                        'outs_when_up' : [outs], 
                        'inning' : [inning], 
                        'n_thruorder_pitcher' : [n_thruorder], 
                        'fastball_percentage' : [float(fastball_percentage)/100.0]
            }
            )
    pred = model.predict(data)
    pred = 'Fastball' if pred == 1 else 'Offspeed/Breaking' 
    st.write('Prediction: ' + pred)
