import joblib
import streamlit as st
import numpy as np
from scipy.special import inv_boxcox
from scipy import stats

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Define lambda values (replace with your actual lambda values)
lambda_price = -0.14547081211466042
lambda_sqft = -0.10374069909584327

# List of predefined locations
predefined_locations = [
    '7th Phase JP Nagar', '8th Phase JP Nagar', 'Akshaya Nagar', 'Banashankari',
    'Bannerghatta Road', 'Begur Road', 'Bellandur', 'Chandapura', 'Electronic City',
    'Electronic City Phase II', 'Electronics City Phase 1', 'Haralur Road', 'Harlur',
    'Hebbal', 'Hennur Road', 'Hoodi', 'Hormavu', 'Hosa Road', 'JP Nagar', 'Jakkur',
    'KR Puram', 'Kaggadasapura', 'Kanakpura Road', 'Kasavanhalli', 'Kengeri', 'Koramangala',
    'Kothanur', 'Marathahalli', 'Nagarbhavi', 'Old Madras Road', 'Raja Rajeshwari Nagar',
    'Rajaji Nagar', 'Ramamurthy Nagar', 'Sarjapur', 'Sarjapur Road', 'Thanisandra', 'Uttarahalli',
    'Varthur', 'Whitefield', 'Yelahanka', 'Yeshwanthpur'
]

def predict_house_price(new_data):
    total_sqft = new_data.get('total_sqft', 0)
    try:
        total_sqft = float(total_sqft)
        if total_sqft <= 0:
            raise ValueError("total_sqft must be a positive numerical value.")
    except ValueError:
        raise ValueError("total_sqft must be a positive numerical value.")

    # Apply Box-Cox transformation to total_sqft
    transformed_total_sqft = stats.boxcox(total_sqft + 1, lmbda=lambda_sqft)

    # Create a feature vector for the predefined locations
    location_features = [1 if new_data.get(loc, 0) else 0 for loc in predefined_locations]

    # Extract other features
    other_features = [
        new_data.get('bath', 0),
        new_data.get('balcony', 0),
        new_data.get('bhk', 0),
        *location_features,
        transformed_total_sqft
    ]

    # Create an array for the model input
    features_array = np.array(other_features).reshape(1, -1)

    # Standardize features
    features_scaled = scaler.transform(features_array)

    # Make prediction using the model
    y_pred_transformed = model.predict(features_scaled)

    # Back-transform the predicted price
    y_pred_original = inv_boxcox(y_pred_transformed[0], lambda_price)

    return y_pred_original

# Streamlit UI configuration
st.set_page_config(page_title="Banglore House Price Prediction", page_icon="🏠", layout="centered")

# Sidebar for inputs
st.sidebar.header("Enter Property Details as per your requirements:")
bath = st.sidebar.number_input('🚿 Number of Bathrooms', min_value=0, value=2)
balcony = st.sidebar.number_input('🏖 Number of Balconies', min_value=0, value=1)
bhk = st.sidebar.number_input('🛏 Number of BHK', min_value=0, value=2)
total_sqft = st.sidebar.number_input('📐 Total Square Feet', min_value=1, value=1000)
location = st.sidebar.selectbox('📍 Select Location', predefined_locations, index=0)

# Create new house dictionary
new_house = {
    'bath': bath,
    'balcony': balcony,
    'bhk': bhk,
    **dict.fromkeys(predefined_locations, 0),
    'total_sqft': total_sqft
}
new_house[location] = 1

# Display house image in the center
st.image('house.jpg', use_column_width=True,width=1200)

# Prediction and output
if st.sidebar.button('Predict House Price 🏡'):
    try:
        predicted_price = predict_house_price(new_house)
        st.markdown(f"<h2 style='text-align: center;'>🏠 Predicted House Price: ₹{predicted_price:.2f} lakhs</h2>", unsafe_allow_html=True)
    except ValueError as e:
        st.error(f"❌ Error: {e}")

# Add animations (e.g., fade-in effect)
st.markdown(
    """
    <style>
    .stImage {
        animation: fadeIn 2s;
    }
    h2 {
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)
