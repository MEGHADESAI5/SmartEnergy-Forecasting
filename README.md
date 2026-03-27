# ⚡ PowerPlant-Energy-Prediction-ANN

An end-to-end Machine Learning web application that predicts the electrical energy output of a Combined Cycle Power Plant using an Artificial Neural Network (ANN) regression model.

---

## 📌 Project Overview

This project focuses on building a predictive system that estimates power plant energy output based on environmental and operational parameters.

It combines:

* 🤖 Deep Learning (ANN)
* 🌐 Web Development (Flask)
* 🎨 Frontend UI (HTML, CSS)
* ☁️ Deployment-ready architecture

The application allows users to input real-time parameters and get instant predictions via a web interface.

---

## 📊 Dataset Information

The model is trained on the **Combined Cycle Power Plant Dataset**, which contains real-world data collected over several years.

### 🔹 Input Features:

* **AT** → Ambient Temperature
* **V** → Exhaust Vacuum
* **AP** → Ambient Pressure
* **RH** → Relative Humidity

### 🔹 Target:

* **PE** → Electrical Energy Output

---

## 🧠 Model Architecture

The prediction model is built using an Artificial Neural Network (ANN):

* Input Layer → 4 neurons
* Hidden Layer 1 → 6 neurons (ReLU)
* Hidden Layer 2 → 6 neurons (ReLU)
* Output Layer → 1 neuron (Regression Output)

The model captures nonlinear relationships between environmental factors and power output.

---

## ⚙️ Features

* 📈 Accurate energy output prediction using ANN
* 🌐 Interactive web interface using Flask
* ⚡ Real-time predictions from user input
* 🧹 Data preprocessing and normalization
* 📊 Model evaluation (MSE, RMSE, R² Score)
* 🎨 Clean and modern UI design

---

## 🛠️ Tech Stack

### 🔹 Machine Learning:

* Python
* PyTorch
* NumPy, Pandas

### 🔹 Web Development:

* Flask
* HTML5
* CSS3

### 🔹 Tools:

* Jupyter Notebook
* Git & GitHub
* Render (Deployment)

---

## 📁 Project Structure

```
PowerPlant-Energy-Prediction-ANN/
│
├── app.py                  # Flask application
├── best_model.pt          # Trained ANN model (weights)
├── full_model.pt          # Full saved model (optional)
├── powerplant_data.csv    # Dataset
├── requirements.txt       # Dependencies
│
├── templates/
│   └── index.html         # Frontend UI
│
├── static/
│   └── style.css          # Styling
│
└── PowerPlant_Project.ipynb  # Model training notebook
```

---

## 🚀 How to Run Locally

### 🔹 Step 1: Clone the repository

```bash
git clone https://github.com/MEGHADESAI5/SmartEnergy-Forecasting
cd SmartEnergy-Forecasting
```

### 🔹 Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Run the application

```bash
python app.py
```

### 🔹 Step 4: Open in browser

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

This project can be deployed using **Render** as a Web Service.

### Configuration:

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
python app.py
```

---

## 📈 Results

The ANN model achieves strong predictive performance by learning complex nonlinear relationships in the dataset.

* ✔ High accuracy
* ✔ Low prediction error
* ✔ Reliable for energy forecasting

---

## 🔮 Future Improvements

* Hyperparameter tuning for better accuracy
* Integration with real-time sensor data
* Advanced deep learning models
* API-based deployment
* Dashboard visualization

---

## 👨‍💻 Author

**Megha Desai**
CSE (AI & ML) Student

---

## ⭐ Support

If you found this project useful:

* ⭐ Star this repository
* 🍴 Fork it
* 📢 Share it

---

## 💡 Key Learning

This project demonstrates how to:

* Build and train ANN models
* Deploy ML models using Flask
* Convert ML projects into real-world applications

---

🚀 *From model → to deployment → to real-world application*

## 🌐 Live Demo  
https://smartenergy-forecasting-1.onrender.com


