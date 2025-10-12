# 🌍 EnviroScan — Real-Time Air Quality Monitoring & Source Prediction

An intelligent, interactive Streamlit dashboard that monitors air quality in real time, provides historical analysis, and predicts pollution sources using advanced machine learning. Experience live AQI data, weather integration, and professional visualizations with export capabilities! 🚀

---

## ✨ Key Features

- 🌡️ **Real-time AQI** from WAQI & OpenWeather APIs (configurable)
- 📊 **Historical Analysis** with time series and downloadable CSV reports  
- 🤖 **AI-Powered Source Classification** using Random Forest & XGBoost
- 🗺️ **Interactive Maps** with Folium station markers and heatmaps
- 📄 **PDF Report Generation** via ReportLab for professional presentations
- 🎨 **Light/Dark Theme** with responsive, mobile-friendly UI
- ⚡ **Smart Fallback System** - seamless synthetic data when APIs unavailable
- 🚀 **Performance Optimized** with caching to reduce API calls

---

## 🗂️ Project Structure

```
📦 EnviroScan/
├── 🎯 streamlit_dashboard.py      # Main Streamlit app (UI + views)
├── 🌐 real_aqi_data.py           # Live AQI + weather API integration
├── 🔧 data_loader.py             # Data processing & ML utilities
├── 📋 requirements.txt           # Project dependencies
├── 📖 REAL_DATA_SETUP.md         # API setup & configuration guide
├── 📄 README.md                  # Project documentation
├── 🔐 LICENSE                    # MIT License
└── 🚫 .gitignore                 # Git ignore patterns
```

## 🚀 Quick Start (Local)

### 1️⃣ Clone Repository
```bash
git clone https://github.com/amishiverma/Amishi-Verma.git
cd Amishi-Verma
```

### 2️⃣ Setup Environment
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configure API Keys (Optional for Live Data)
Choose your preferred method:

**🔒 Streamlit Secrets (Recommended for Cloud):**
Create `.streamlit/secrets.toml`:
```toml
WAQI_TOKEN = "93a6a5ac6b2bba5e166206d19b918e6b747fe14f"  # Your actual token
OPENWEATHER_API_KEY = "your_openweather_key_here"        # Optional
```

**🌐 Environment Variables:**
```bash
# Windows
set WAQI_TOKEN=93a6a5ac6b2bba5e166206d19b918e6b747fe14f
set OPENWEATHER_API_KEY=your_openweather_key_here

# Linux/macOS  
export WAQI_TOKEN=93a6a5ac6b2bba5e166206d19b918e6b747fe14f
export OPENWEATHER_API_KEY=your_openweather_key_here
```

### 4️⃣ Launch Dashboard
```bash
streamlit run streamlit_dashboard.py
```
🎉 **Success!** Open your browser to `http://localhost:8501`

## 🌐 Real Data Configuration

### 📡 Supported APIs
- **🏭 WAQI (World Air Quality Index)**: [aqicn.org/api](https://aqicn.org/api/) - Global AQI & station data
- **🌤️ OpenWeather Air Pollution**: [openweathermap.org/api](https://openweathermap.org/api) - Weather & air quality

### 🔑 API Key Setup

**🚀 Quick WAQI Setup (2 minutes):**
1. Visit: [aqicn.org/api](https://aqicn.org/api/)
2. Click "Request API Token"
3. Fill simple form (name, email, usage description)
4. Get instant free token!

**Required environment variables:**
- `WAQI_TOKEN` - Your World Air Quality Index API token
- `OPENWEATHER_API_KEY` - Your OpenWeather API key (optional)

**Example token format:** `93a6a5ac6b2bba5e166206d19b918e6b747fe14f`

*💡 Don't have API keys? No problem! The dashboard gracefully falls back to realistic synthetic data.*

---

## ☁️ Cloud Deployment (Streamlit Cloud)

### 🎯 Quick Deploy Steps
1. **📂 Make Repository Public** (or grant Streamlit Cloud access)
2. **🔗 Connect to Streamlit Cloud**:
   - Visit [streamlit.io/cloud](https://streamlit.io/cloud)
   - Click "New app" → Connect GitHub
   - Select repository: `amishiverma/Amishi-Verma`
   - Main file: `streamlit_dashboard.py`
3. **🔐 Add Secrets** (Settings → Secrets):
   ```toml
   WAQI_TOKEN = "your_waqi_token_here"
   OPENWEATHER_API_KEY = "your_openweather_key_here"
   ```
4. **🚀 Deploy!** Your app will be live at `https://your-app-name.streamlit.app`

---

## 🎯 Dashboard Features & Usage

### 📊 **Three Main Views**
- **📈 Historical Analysis** - Time series charts and trend analysis
- **🔮 Prediction View** - ML-powered source classification and forecasting  
- **🌍 Real-Time AQI** - Live air quality data with interactive maps

### 🎛️ **Interactive Controls**
- **🌙 Theme Toggle** - Switch between light and dark modes
- **🏙️ City Selection** - Choose from 8+ major Indian cities
- **📥 Export Options** - Download PDF reports and CSV data
- **⚡ Real Data Toggle** - Switch between live APIs and synthetic data

### 🗺️ **Map Visualizations**
- Color-coded AQI markers with station details
- Interactive popups showing pollutant levels
- Responsive design for desktop and mobile

---

## 🤖 Machine Learning & APIs

### 🔬 **ML Models**
```python
# Get live city AQI data
from real_aqi_data import RealAQIData
api = RealAQIData()
data = api.get_real_time_aqi_waqi("Delhi")

# Run complete ML workflow  
from data_loader import run_complete_workflow
results = run_complete_workflow("Delhi")
```

### 🏗️ **Architecture**
- **Random Forest & XGBoost** for source classification
- **Feature Engineering** with spatial and temporal data
- **Intelligent Caching** with 5-minute TTL for API calls
- **Graceful Fallbacks** to synthetic data when APIs unavailable

---

## 📝 Notes & Best Practices

- 🔐 **Security**: API keys stored in Streamlit secrets/environment variables only
- ⚡ **Performance**: Intelligent caching reduces API calls and improves response time  
- 🛡️ **Reliability**: Fallback system ensures dashboard always displays meaningful data
- 📱 **Responsive**: Mobile-friendly design with touch-optimized controls

---

## 🤝 Contributing

1. **🍴 Fork** the repository
2. **🌿 Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **💾 Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **📤 Push** to branch (`git push origin feature/amazing-feature`)
5. **🔄 Open** a Pull Request

*🚫 Keep secrets out of commits! Use environment variables.*

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🎉 Ready to Monitor Air Quality?

**Get started in 3 commands:**
```bash
git clone https://github.com/amishiverma/Amishi-Verma.git
cd Amishi-Verma && pip install -r requirements.txt  
streamlit run streamlit_dashboard.py
```

**🌟 Star this repo if you find it useful!** 