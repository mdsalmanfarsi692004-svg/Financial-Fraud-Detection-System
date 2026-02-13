# 🛡️ FraudGuard AI | Financial Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)

**FraudGuard AI** is a machine learning-based application designed to detect fraudulent financial transactions in real-time. It analyzes transaction patterns to classify them as **Safe** or **Fraudulent**.

🔗 **Live App:** [Click Here to View App] (https://financial-fraud-guard-ai.streamlit.app/)

🔗 **Live Video Link (Google Drive):** [Click Here to View Video] (https://drive.google.com/file/d/1WYBBzButugguU_FWv1bpgJUyAiIa9fBL/view?usp=drivesdk)
---

## 📸 Screenshots

### 🏠 Home Page
<img width="1885" height="879" alt="Screenshot 2026-01-23 222841" src="https://github.com/user-attachments/assets/0b947abe-bfe0-4278-9b22-40beb0e02251" />


### ✅ Safe Transaction Result
<img width="1886" height="857" alt="Screenshot 2026-01-23 223325" src="https://github.com/user-attachments/assets/0dede774-e755-4522-aea3-8115d90d0bd3" />


### ⚠️ Fraud Detected Alert
<img width="1877" height="886" alt="Screenshot 2026-01-23 223703" src="https://github.com/user-attachments/assets/4131f90e-6c2e-4354-9723-62fb7308ff68" />

---

## 🚀 Features
* **Real-time Analysis:** Instant prediction upon data entry.
* **User-Friendly UI:** Built with Streamlit for a clean, interactive experience.
* **Secure & Fast:** Uses a pre-trained ML pipeline (`joblib`) for quick inference.
* **Actionable Insights:** Provides specific recommendations for flagged transactions.

---

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Serialization:** Joblib

---

## 📂 Project Structure
text
├── images/             # Application screenshots and UI assets
├── notebooks/          # Data cleaning, EDA, and model training
├── reports/            # Technical report and project presentation
├── app.py              # Main Streamlit application
├── requirements.txt    # List of required Python packages
├── model.pkl           # Finalized fraud detection model
├── scaler.pkl          # Feature scaling object
└── sample_data.csv     # Anonymized transaction dataset
---

## 💻 How to Run Locally

Run the following commands in your terminal to set up the project:

```bash
# Clone the repository
git clone https://github.com/mdsalmanfarsi692004-svg/Financial-Fraud-Detection-System.git

# Navigate to the directory
cd Financial-Fraud-Detection-System

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run Fraud_Detection.py

#👨‍💻 Developed by
Md Salman Farsi for Unified Mentors Pvt. Ltd. Internship Project
