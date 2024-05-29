import streamlit as st
import numpy as np
import pandas as pd
import json
import pickle

# Function to load location options from JSON file
def load_location_options(file_path):
    with open(file_path, 'r') as f:
        location_options = json.load(f)
    return location_options

# Function to load the model and feature matrix
def load_model_and_X(model_file, X_file):
    with open(model_file, 'rb') as f:
        lr = pickle.load(f)
    X = pd.read_csv(X_file)  # Adjust if your feature matrix is in a different format
    return lr, X

# Function to predict price using the model and user input
def predict_price(location, sqft, bath, bhk, X, lr):
    loc_index = np.where(X.columns == location)[0][0]

    x = np.zeros(len(X.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return lr.predict([x])[0]

# Main function for the Streamlit app
def main():
    st.title('Banglore House Price Prediction')

    # Display an image
    st.image('img.jpg', use_column_width=True)

    # Sidebar for user input
    with st.sidebar.header('House Features'):

        # Load location options from JSON
        location_options = load_location_options("location.json")

        # Location selectbox
        location = st.sidebar.selectbox('Location', location_options)

        # Input fields for house features
        sqft = st.sidebar.number_input('Sqft', min_value=100, max_value=10000, value=1000)
        bath = st.sidebar.number_input('Bathrooms', min_value=1, max_value=10, value=2)
        bhk = st.sidebar.number_input('BHK', min_value=1, max_value=10, value=2)

        # Load model and feature matrix
        lr, X = load_model_and_X("model.pkl", "input_dataframe.csv")

    # Prediction button and result display
    if st.sidebar.button('Predict'):
        with st.container():  # Create a container for visual layout
            st.write('Calculating Price...')  # Display the text
            st.spinner('')  # Add an empty spinner (visual effect)

        result = predict_price(location, sqft, bath, bhk, X, lr)
        st.success(f'Estimated Price: Rs.{result:.2f} Lakhs.')

if __name__ == '__main__':
    main()
