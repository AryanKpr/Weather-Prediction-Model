# Weather-Prediction-Model
Weather Prediction Model (Streamlit App)

This project is a machine learning–based weather prediction system with an interactive Streamlit frontend.  
It predicts future temperature values using historical weather data and regression techniques.

Live app: https://ak-weather-prediciton.streamlit.app/

Demo Screenshot:
<img width="2088" height="1476" alt="image" src="https://github.com/user-attachments/assets/7a0b264b-c6b8-46df-8cb9-f52599ca318a" />

Project Overview
The goal of this project is to:
- Analyze historical weather data
- Train a regression-based ML model
- Predict future weather metrics (temperature)
- Provide an easy-to-use web interface for predictions

The backend model is trained using scikit-learn, and the frontend is built using Streamlit.

Features
- Predicts temperature using historical weather parameters
- Ridge Regression model to handle multicollinearity
- Interactive web UI built with Streamlit
- Model persistence using Joblib
- Fast and lightweight deployment

Tech Stack
Machine Learning
  - Python
  - scikit-learn
  - NumPy
  - pandas

Model
- Linear Regression
- Features:
  - Precipitation 
  - Snow 
  - Snow Depth
  - Maximum Temperature
  - Minimum Temperature

Frontend
- The application uses Streamlit for frontend development and deployment. Streamlit enables an interactive web interface where users can input weather features and receive predictions from the model.

