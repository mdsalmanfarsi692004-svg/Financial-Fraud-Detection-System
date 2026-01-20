# 🛡️ FraudGuard AI | Financial Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)

**FraudGuard AI** is a machine learning-based application designed to detect fraudulent financial transactions in real-time. It analyzes transaction patterns to classify them as **Safe** or **Fraudulent**.

🔗 **Live Demo:** [Click Here to View App] (https://financial-fraud-guard-ai.streamlit.app/)

---

## 📸 Screenshots

### 🏠 Home Page
<img width="1919" height="917" alt="Home Page" src="https://github.com/user-attachments/assets/ddff0f75-604d-47fe-9b2a-c7a920f7c585" />

### ✅ Safe Transaction Result
<img width="1891" height="917" alt="Safe Transaction" src="https://github.com/user-attachments/assets/ee57b0ea-cea9-46ea-8b69-281b62668ab0" />

### ⚠️ Fraud Detected Alert
<img width="1888" height="917" alt="Fraud Transaction" src="https://github.com/user-attachments/assets/096f8bb3-adce-4373-8b0e-361f4d7c680c" />

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

## 💻 How to Run Locally

Run the following commands in your terminal to set up the project:

```bash
# Clone the repository
git clone [https://github.com/your-username/FraudGuard-AI.git](https://github.com/your-username/FraudGuard-AI.git)

# Navigate to the directory
cd FraudGuard-AI

# Install dependencies
pip install -r requirements.txt

**Author**
Md Salman Farsi
# Run the app
streamlit run Fraud_Detection.py
