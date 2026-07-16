# 🏠 House Price Prediction

A Machine Learning web application that predicts house prices based on property features. The application is built using **FastAPI** and a **Random Forest Regressor** model, providing fast and accurate predictions through a simple web interface.

---

## 🚀 Features

- Predict house prices instantly
- Fast and lightweight FastAPI backend
- Simple and responsive HTML interface
- Machine Learning model using Random Forest
- Easy to deploy and run locally

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Jinja2
- Python-Multipart
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
House-Price-Prediction/
│
├── app.py
├── house_price_rf.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

---

## 📊 Input Features

- Bedrooms
- Bathrooms
- Square Feet Living
- Square Feet Lot
- Floors
- Waterfront
- View
- Condition
- Square Feet Above
- Square Feet Basement
- Year Built
- Year Renovated
- Sale Year
- Sale Month

---

## 📈 Output

The application predicts the estimated house price based on the provided property details.

Example:

```
Predicted House Price: $496,773.08
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
```

### 2. Move into the project folder

```bash
cd House-Price-Prediction
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Open your browser:

```
http://127.0.0.1:8000
```

---

## 🤖 Machine Learning Model

- Algorithm: Random Forest Regressor
- Library: Scikit-learn
- Model Storage: Joblib

---

## 📦 Requirements

- Python 3.11 or later
- FastAPI
- Uvicorn
- Jinja2
- Python-Multipart
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📜 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Luna**