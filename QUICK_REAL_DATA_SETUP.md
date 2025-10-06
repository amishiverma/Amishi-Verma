# 🚀 Quick Real Data Setup (5 Minutes)

## Step 1: Get Free WAQI API Key
1. Go to: https://aqicn.org/api/
2. Click "Request API Token"
3. Fill the simple form (name, email, usage description)
4. You'll get a free token instantly!

## Step 2: Configure Your Token
Open `real_aqi_data.py` and replace:
```python
self.waqi_token = "demo"
```
With:
```python
self.waqi_token = "your_actual_token_here"
```

## Step 3: Enable Real Data
1. Open your dashboard at http://localhost:8501
2. In the sidebar, check ☑️ "Use Real AQI Data"
3. Navigate to "Real-Time AQI" view
4. Select any city to see live data!

## Optional: OpenWeather API
- Get free key from: https://openweathermap.org/api
- Replace `self.openweather_api_key = "demo"` with your key
- This adds weather data (temperature, humidity)

## 🎯 What You'll Get:
- ✅ Live AQI data from 1000+ global stations
- ✅ Real pollution measurements (PM2.5, PM10, NO2, SO2, CO, O3)
- ✅ Station-specific information with coordinates
- ✅ Historical trends and forecasts
- ✅ Weather integration (with OpenWeather key)

## 🔧 Troubleshooting:
- If API fails, dashboard automatically falls back to synthetic data
- Check console for any error messages
- Verify your internet connection

**Total setup time: < 5 minutes** 🚀