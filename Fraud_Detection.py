import streamlit as st
import pandas as pd
import joblib
import time

st.set_page_config(
    page_title="FraudGuard AI | Financial Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"  # Ye line sidebar ko khula rakhti hai
)

st.markdown("""
    <style>
    /* MainMenu hata diya lekin Header rehne diya taki Sidebar button dikhe */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    /* header {visibility: hidden;}  <-- YE LINE HATA DI HAI */
    
    div[data-testid="stAlert"] p, div[data-testid="stAlert"] svg {
        color: #ffffff !important;
        fill: #ffffff !important;
    }

    section[data-testid="stSidebar"] .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {
        text-align: center !important;
        width: 100%;
    }
    
    section[data-testid="stSidebar"] label {
        justify-content: center;
        display: flex;
        width: 100%;
    }

    .main .block-container h1, .main .block-container h3, .main .block-container h4, .main .block-container p {
        text-align: center !important;
    }
    
    .stNumberInput label {
        justify-content: center !important;
        display: flex;
        width: 100%;
    }
    
    /* CUSTOM BUTTON STYLING */
    div.stButton > button {
        background-color: #00C853; 
        color: white;
        border: none;
        padding: 12px 20px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
        transition: 0.3s;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
    }
    
    div.stButton > button:hover {
        background-color: #009624; 
        color: white;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

try:
    model = joblib.load("fraud_detection_pipeline.pkl")
except FileNotFoundError:
    st.error("🚨 Error: 'fraud_detection_pipeline.pkl' not found.")
    st.stop()

# --- SIDEBAR CODE ---
with st.sidebar:
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image("https://cdn-icons-png.flaticon.com/512/1161/1161388.png", width=120)
    
    st.markdown("<h1 style='text-align: center; margin-top: 0;'>FraudGuard AI</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<p style='text-align: center;'>Analyze financial transactions to detect potential fraud patterns.</p>", unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center;'>Transaction Details</h3>", unsafe_allow_html=True)
    
    transaction_type = st.selectbox(
        "Select Transaction Type", 
        ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
    )
    
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; font-size: 12px; white-space: nowrap; color: #888;'>Powered by Streamlit & Scikit-learn</div>", 
        unsafe_allow_html=True
    )

# --- MAIN PAGE CODE ---
st.markdown("<h1 style='text-align: center;'>🛡️ Financial Fraud Detection System</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>AI-Powered Security Analysis</h3>", unsafe_allow_html=True)

st.markdown("""
    <div style="
        background-color: #262730; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #4b4b4b; 
        text-align: center; 
        color: #ffffff;
        font-size: 16px;
        margin-bottom: 20px;">
        ℹ️ Please fill in the transaction details below and click <b>Analyze Transaction</b>.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("<h4 style='text-align: center;'>💰 Transaction Value</h4>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    amount = st.number_input("Amount ($)", min_value=0.0, value=1000.0, step=10.0)

st.markdown("<br>", unsafe_allow_html=True)

col_sender, col_receiver = st.columns(2)

with col_sender:
    st.markdown("<h4 style='text-align: center;'>📤 Sender Information</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px;'>Details of the account sending money</p>", unsafe_allow_html=True)
    oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
    newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)

with col_receiver:
    st.markdown("<h4 style='text-align: center;'>📥 Receiver Information</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px;'>Details of the account receiving money</p>", unsafe_allow_html=True)
    oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

st.markdown("<br>", unsafe_allow_html=True)

b1, b2, b3 = st.columns([1, 1, 1])
with b2:
    predict_btn = st.button("🔍 Analyze Transaction", use_container_width=True)

if predict_btn:
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])
    
    with st.spinner('Analyzing...'):
        time.sleep(1)
        prediction = model.predict(input_data)[0]

    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>📊 Analysis Result</h2>", unsafe_allow_html=True)

    if prediction == 1:
        st.markdown("""
            <div style="background-color:#5c1e1e; padding:20px; border-radius:10px; border:1px solid #ff4b4b; text-align: center; margin: auto; max-width: 600px;">
                <h3 style="color:#ff4b4b; margin:0;">⚠️ FRAUD DETECTED!</h3>
                <p style="color:white; font-weight:500; margin-top:10px;">Our AI model has flagged this transaction as <b>Suspicious</b>.</p>
                <hr style="border-top: 1px solid #ff4b4b; opacity: 0.5;">
                <h4 style="color:#ff4b4b; margin-top:15px;">Recommended Actions:</h4>
                <ul style="text-align: left; display: inline-block; margin-top: 10px; color: white;">
                    <li>Do not proceed with this transaction.</li>
                    <li>Freeze the sender's account immediately.</li>
                    <li>Verify customer identity (KYC).</li>
                    <li>Report to the security team.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background-color:#1e4620; padding:20px; border-radius:10px; border:1px solid #00c853; text-align: center; margin: auto; max-width: 600px;">
                <h3 style="color:#00c853; margin:0;">✅ SAFE TRANSACTION</h3>
                <p style="color:white; font-weight:500; margin-top:10px;">This transaction appears to be <b>Legitimate</b>.</p>
                <hr style="border-top: 1px solid #00c853; opacity: 0.5;">
                <h4 style="color:#00c853; margin-top:15px;">Recommendations:</h4>
                 <ul style="text-align: left; display: inline-block; margin-top: 10px; color: white;">
                    <li>Proceed with the transaction.</li>
                    <li>No further action required.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)