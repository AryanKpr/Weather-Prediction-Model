
import streamlit as st # type: ignore
import joblib # type: ignore
import numpy as np # type: ignore
import pandas as pd # type: ignore

model = joblib.load("weather_model.pkl")

st.set_page_config(page_title="Weather Prediction", page_icon="🌦️")

st.title("🌦️ Weather Prediction App")
st.write("Enter the weather parameters to predict the weather.")

prcp = st.number_input("Precipitation (prcp)")
snow = st.number_input("Snow")
snwd = st.number_input("Snow Depth")
tmax = st.number_input("Max Temperature")
tmin = st.number_input("Min Temperature")
if st.button("Predict Weather"):
    input_data = np.array([[prcp, snow, snwd, tmax, tmin]])


    prediction = model.predict(input_data)

    st.success(f"🌤️ Predicted Weather: **{prediction[0]}**")
