# 📈 Stock Trend Prediction

A Flask web application that uses an LSTM deep learning model to predict stock price trends. Enter any stock ticker to visualize Exponential Moving Averages (EMA) and compare predicted vs actual closing prices.

---

## 🖥️ Demo

| Feature | Description |
|--------|-------------|
| EMA 20 & 50 | Short-term trend chart |
| EMA 100 & 200 | Long-term trend chart |
| Prediction vs Actual | LSTM model output vs real closing price |
| CSV Download | Download the full historical dataset |

---

## 📁 Project Structure

```
Stock/
├── app.py                  # Flask backend
├── stock_dl_model.keras    # Pre-trained LSTM model
├── templates/
│   └── index.html          # Frontend UI
├── static/                 # Auto-generated chart images & CSVs
├── powergrid.csv           # Sample dataset
├── Stock_Prediction.ipynb  # Model training notebook
└── README.md
```

---

## ⚙️ Prerequisites

- **Python 3.9 – 3.13**
- **pip** (comes with Python)

---

## 🚀 Setup & Launch

### 1. Clone or download the project

Place the project folder anywhere on your machine (e.g. `Desktop/Stock`).

### 2. Install dependencies

Open a terminal in the project folder and run:

```bash
pip install flask numpy pandas matplotlib scikit-learn keras tensorflow yfinance
```

### 3. Run the app

```bash
python app.py
```

You should see:

```
* Running on http://127.0.0.1:5000
```

### 4. Open in browser

Navigate to 👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧪 Usage

1. Enter a **stock ticker** in the input field (e.g. `POWERGRID.NS`, `TCS.NS`, `RELIANCE.NS`, `AAPL`)
2. Click **Submit**
3. Wait for the app to download data and run the model (~10–30 seconds)
4. View the **EMA charts** and **Prediction vs Original** graph
5. Download the full **CSV dataset** using the green button

> **Tip:** Use the `.NS` suffix for Indian NSE stocks (e.g. `INFY.NS`, `HDFCBANK.NS`).  
> For US stocks, just use the ticker as-is (e.g. `AAPL`, `TSLA`, `MSFT`).

---

## 🐛 Known Warnings (Safe to Ignore)

| Warning | Reason | Impact |
|---------|--------|--------|
| `oneDNN custom operations are on` | TensorFlow info log | None |
| `TensorFlow GPU support is not available on native Windows` | No GPU acceleration | Runs on CPU, slightly slower |
| `Skipping variable loading for optimizer 'rm_sprop'` | Model was saved with a different optimizer state | None — predictions are unaffected |

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web server |
| `numpy` | Numerical operations |
| `pandas` | Data manipulation |
| `matplotlib` | Chart generation |
| `scikit-learn` | Data scaling (MinMaxScaler) |
| `keras` / `tensorflow` | LSTM model loading & prediction |
| `yfinance` | Downloading live stock data |

---

## 🔧 Troubleshooting

**Port already in use:**
```bash
# Find and kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Module not found error:**
```bash
pip install <missing-module-name>
```

**No charts displayed after submit:**  
Make sure the `static/` folder exists in the project root. It is created automatically on first run, but you can also create it manually:
```bash
mkdir static
```

---

## 📝 Notes

- Stock data is fetched from **Yahoo Finance** via `yfinance` — an internet connection is required when submitting a stock.
- The model was trained on data from **Jan 2000 to Oct 2024**.
- The app runs in **debug mode** by default (suitable for local development only).
