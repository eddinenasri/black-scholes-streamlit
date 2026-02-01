# 📈 Black–Scholes Option Pricer (Streamlit)

An interactive web application for pricing European call and put options using the **Black–Scholes model**, built with **Python, Streamlit, NumPy, SciPy, and Plotly**.

The app allows real-time exploration of option prices and visualizes how they evolve with respect to **spot price** and **volatility** using interactive heatmaps.

---

## 🚀 Features

- Black–Scholes pricing for **Call and Put options**
- Real-time parameter updates:
  - Spot price
  - Strike
  - Volatility
  - Risk-free rate
  - Time to maturity
- Interactive **2D heatmaps**:
  - Option price as a function of **Spot Price × Volatility**
  - Hover tooltips for precise numerical values
- Clean and intuitive UI built with Streamlit
- Plotly-powered visualizations (zoom, pan, hover)

---

## 🧮 Model

The app implements the standard Black–Scholes formulas:

- Call option price  
- Put option price  

Assumptions:
- European options
- Constant volatility
- No dividends
- Continuous trading

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – web application framework
- **NumPy** – numerical computations
- **SciPy** – cumulative normal distribution
- **Plotly** – interactive visualizations

---

## ▶️ Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/eddinenasri/black-scholes-streamlit.git
cd black-scholes-streamlit
'''

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
```bash
pip install -r requirements.txt

### 4. Run the app
```bash

streamlit run professional_black_scholes_go.py
