# EnviroScan — Real-Time Air Quality Monitoring & Source Prediction

EnviroScan is an interactive Streamlit dashboard that monitors air quality in real time, provides historical analysis, and predicts pollution sources using machine learning. The app integrates live AQI and weather data, visualizes results on maps and charts, and exports PDF/CSV reports.

## Key Features
- Real-time AQI from WAQI / OpenWeather (configurable)
- Historical AQI time series and downloadable CSV
- AI-powered source classification (Random Forest / XGBoost)
- Interactive Folium maps with station markers and heatmaps
- PDF report generation via ReportLab
- Light / Dark theme and responsive UI
- Fallback to synthetic data when APIs are unavailable (silent fallback)
- Caching to reduce API calls and improve performance

## Project structure
```
EnviroScan/
├── streamlit_dashboard.py      # Main Streamlit app (UI + views)
├── real_aqi_data.py           # Live AQI + weather API integration (WAQI/OpenWeather)
├── data_loader.py             # Data processing, feature engineering, ML utilities
├── enviroscan2.py             # Utilities / ngrok (if used)
├── requirements.txt
├── REAL_DATA_SETUP.md         # API key & setup instructions
├── USAGE.md
└── README.md
```

## Quick start (local)

1. Clone repo:
  ```bash
  git clone https://github.com/<your-username>/Amishi-Verma.git
  cd Amishi-Verma
  ```
2. Create venv and install:
  ```bash
  python -m venv venv
  # Windows
  venv\Scripts\activate
  # macOS / Linux
  source venv/bin/activate
  pip install -r requirements.txt
  ```
3. Configure API keys:
  - Preferred: use Streamlit secrets (recommended for cloud)
  - Or set keys in `real_aqi_data.py` or environment variables:
    ```python
    WAQI_TOKEN = "your_waqi_token_here"
    OPENWEATHER_API_KEY = "your_openweather_api_key_here"
    ```
4. Run the app:
  ```bash
  streamlit run streamlit_dashboard.py
  ```

## Real data configuration
- WAQI (World Air Quality Index): https://aqicn.org/api/ (AQI & station data)
- OpenWeather Air Pollution: https://openweathermap.org/api (air pollution endpoint)
- Use Streamlit Cloud secrets or environment variables for API keys:
  - `WAQI_TOKEN`
  - `OPENWEATHER_API_KEY`

## Deployment (Streamlit Cloud)
1. Make repository public (or grant Streamlit Cloud access to private repo).
2. On Streamlit Cloud, create new app → connect repo → set main file: `streamlit_dashboard.py`.
3. Add secrets via Settings → Secrets:
  ```toml
  WAQI_TOKEN = "your_waqi_token_here"
  OPENWEATHER_API_KEY = "your_openweather_api_key_here"
  ```
4. Deploy.

## Usage snippets
- Get live city AQI:
  ```python
  from real_aqi_data import RealAQIData
  api = RealAQIData()
  data = api.get_real_time_aqi_waqi("Delhi")
  ```
- Run ML workflow:
  ```python
  from data_loader import run_complete_workflow
  results = run_complete_workflow("Delhi")
  ```

## Notes & best practices
- Sensitive keys should never be committed. Use Streamlit secrets or environment variables.
- The app includes intelligent fallbacks — if API limits are hit, the dashboard uses cached or synthetic data silently (no demo labels).
- For production use add logging, rate-limit handling, and proper model persistence (models/ directory, .pkl files ignored by .gitignore).

## Contributing
- Fork → feature branch → PR. Keep secrets out of commits.

## License
Include your chosen license file (e.g., MIT) at project root.

---

**If you want, I can:**
- overwrite `README.md` with this content and push the change, and
- remove any remaining hardcoded API keys and ensure the app reads keys from Streamlit secrets / environment variables.
 
Which action should I take next? 