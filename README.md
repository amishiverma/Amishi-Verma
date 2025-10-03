# EnviroScan: AI-Powered Air Quality Monitoring Dashboard

A comprehensive real-time air quality monitoring system with AI-powered pollution source identification. This project integrates live AQI data from global monitoring stations, provides interactive visualizations, PDF report generation, and implements machine learning algorithms for pollution source prediction and analysis.

## 🌟 Features

### Real-Time Air Quality Data
- **Live AQI Integration**: Real-time data from WAQI (World Air Quality Index) API
- **Global Coverage**: Access to thousands of monitoring stations worldwide
- **Weather Integration**: Temperature, humidity, and weather conditions via OpenWeather API
- **Smart Fallback**: Automatic fallback to synthetic data when APIs are unavailable
- **Data Caching**: Intelligent caching to prevent API rate limiting

### Interactive Dashboard
- **Multi-View Interface**: Historical AQI, Future Predictions, and Real-Time monitoring
- **PDF Report Generation**: Professional pollution reports with charts and data tables
- **CSV Data Export**: Download raw data for further analysis
- **Theme Support**: Light and dark mode with optimized visibility
- **Mobile Responsive**: Optimized for desktop and mobile viewing

### Advanced Visualizations
- **Interactive Maps**: Real-time AQI visualization with Folium integration
- **Time Series Charts**: Historical pollution trends with Plotly
- **Pollution Forecasts**: AI-powered predictions for future AQI levels
- **Station-Specific Data**: Detailed information for individual monitoring stations
- **Performance Optimized**: Anti-flicker technology for smooth real-time updates

### Machine Learning & Analytics
- **Multiple Model Training**: Random Forest, Logistic Regression, and Neural Network models
- **Source Identification**: AI-powered pollution source classification
- **Predictive Analytics**: Future AQI forecasting based on historical patterns
- **Data Processing**: Comprehensive data cleaning and feature engineering

## 🚀 Quick Start

### Prerequisites
```bash
pip install -r requirements.txt
```

### Launch the Dashboard
```bash
# Run the main Streamlit dashboard
streamlit run streamlit_dashboard.py
```

### Enable Real AQI Data (Optional)
1. Get free API keys:
   - [WAQI API](https://aqicn.org/api/) for air quality data
   - [OpenWeather API](https://openweathermap.org/api) for weather data (optional)

2. Configure API keys in `real_aqi_data.py`:
```python
WAQI_TOKEN = "your_waqi_token_here"
OPENWEATHER_API_KEY = "your_openweather_key_here"
```

3. Enable real data in the dashboard sidebar

### Basic Usage
```python
# Import data processing functions
from data_loader import run_complete_workflow

# Run the complete analysis workflow
results = run_complete_workflow("Delhi")

# Use real AQI data
from real_aqi_data import get_live_aqi_data
data = get_live_aqi_data("Delhi")
```

## 📁 Project Structure

```
EnviroScan/
├── streamlit_dashboard.py      # Main dashboard application
├── real_aqi_data.py           # Real AQI data integration
├── data_loader.py             # Data processing and ML models
├── enviroscan2.py             # Utility functions and ngrok setup
├── requirements.txt           # Python dependencies
├── REAL_DATA_SETUP.md        # API setup guide
├── USAGE.md                  # Usage instructions
└── README.md                 # This file
```

### Key Files
- **`streamlit_dashboard.py`**: Main web application with three views (Historical, Prediction, Real-time)
- **`real_aqi_data.py`**: API integration for live air quality data from WAQI and OpenWeather
- **`data_loader.py`**: Advanced data processing, ML models, and analysis functions
- **`REAL_DATA_SETUP.md`**: Step-by-step guide for setting up real AQI data APIs

### Running Individual Components

#### 1. Data Collection
```python
from enviroscan2_complete import fetch_openaq_data

# Fetch real data from OpenAQ API
data = fetch_openaq_data("Delhi")
```

#### 2. Data Processing
```python
from enviroscan2_complete import clean_pollution_data, feature_engineering

# Clean and process the data
cleaned_data = clean_pollution_data(raw_data)
featured_data = feature_engineering(cleaned_data)
```

#### 3. Source Labeling
```python
from enviroscan2_complete import label_sources

# Apply source labeling rules
labeled_data = label_sources(featured_data)
```

#### 4. Model Training
```python
from enviroscan2_complete import train_multiple_models, prepare_features

# Prepare features and train models
X, feature_names = prepare_features(labeled_data)
models = train_multiple_models(X_train, y_train, X_val, y_val)
```

#### 5. Visualization
```python
from enviroscan2_complete import create_pollution_heatmap, create_source_map

# Create interactive maps
heatmap = create_pollution_heatmap(data)
source_map = create_source_map(data)
```

## 📊 Workflow Steps

The complete workflow consists of 14 automated steps:

1. **Data Collection**: Fetch pollution measurements from APIs
2. **Data Cleaning**: Remove duplicates, handle missing values, filter outliers
3. **Feature Engineering**: Create temporal, spatial, and composite features
4. **Source Labeling**: Apply rule-based labeling with simulation for balance
5. **Dataset Splitting**: Create stratified train/validation/test splits
6. **Data Balancing**: Apply SMOTE for handling class imbalance
7. **Model Training**: Train multiple ML models with hyperparameter tuning
8. **Model Evaluation**: Comprehensive performance assessment
9. **Visualization Creation**: Generate performance comparison charts
10. **Model Saving**: Save the best performing model
11. **Predictions**: Make predictions on new data
12. **Geospatial Visualization**: Create interactive maps and heatmaps
13. **Insights Generation**: Extract key patterns and statistics
14. **Dashboard Creation**: Generate interactive Streamlit dashboard

## 🏭 Pollution Source Categories

The system identifies six main pollution source categories:

- **Vehicular**: Traffic-related emissions (high NO2, near roads, rush hours)
- **Industrial**: Factory and industrial emissions (high SO2, near industrial areas)
- **Agricultural**: Farming and biomass burning (high PM2.5, seasonal patterns)
- **Residential**: Household activities and heating
- **Natural**: Background pollution in remote areas
- **Mixed**: Combined sources with unclear primary contributor

## 📈 Model Performance

The system trains and compares three machine learning models:

| Model | Typical Accuracy | F1-Score | Best Use Case |
|-------|------------------|----------|---------------|
| Random Forest | 85-92% | 0.87-0.91 | Robust, interpretable |
| Logistic Regression | 78-85% | 0.80-0.86 | Fast, linear relationships |
| Neural Network | 82-89% | 0.84-0.88 | Complex patterns |

## 🗺️ Geospatial Features

### Interactive Maps
- **Pollution Heatmaps**: Visualize concentration gradients
- **Source Markers**: Color-coded by pollution source type
- **Multi-layer Views**: Toggle between different data layers
- **Popup Information**: Detailed data for each location

### Map Types
1. **Basic Heatmap**: Simple concentration visualization
2. **Source-Specific Map**: Categorized by pollution source
3. **Multi-Layer Map**: Comprehensive view with multiple data types

## 📱 Dashboard Features

### Three Main Views
1. **Historical AQI**: Analyze past air quality trends with interactive charts
2. **Future Prediction**: AI-powered forecasting for upcoming air quality
3. **Real-Time AQI**: Live monitoring with global station data

### Real-Time Monitoring
- Live AQI data from global monitoring stations
- Station-specific information with coordinates
- Weather integration (temperature, humidity, conditions)
- Auto-refresh functionality with configurable intervals
- Anti-flicker technology for smooth updates

### Interactive Elements
- City selection with global coverage
- Real/synthetic data toggle
- Theme switcher (light/dark mode)
- Interactive maps with zoom and clustering
- Time-based data filtering
- Station selection dropdown

### Export & Reporting
- **PDF Reports**: Professional pollution reports with:
  - Executive summary and recommendations
  - Data tables with pollution measurements
  - Charts and visualizations
  - Customizable report headers
- **CSV Export**: Raw data download for analysis
- **Interactive Maps**: Exportable HTML maps

### Performance Features
- **Data Caching**: Intelligent caching to reduce API calls
- **Error Handling**: Graceful fallback to synthetic data
- **Mobile Responsive**: Optimized for all device sizes
- **Fast Loading**: Optimized rendering and data processing

## 🛠️ Configuration

### Real AQI Data APIs
```python
# WAQI (World Air Quality Index) API
WAQI_TOKEN = "your_waqi_token_here"  # Get from https://aqicn.org/api/
WAQI_BASE_URL = "https://api.waqi.info"

# OpenWeather API (optional)
OPENWEATHER_API_KEY = "your_openweather_key_here"  # Get from https://openweathermap.org/api
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"
```

### Dashboard Configuration
```python
# Enable/disable real data in dashboard
USE_REAL_DATA = True  # Toggle in sidebar

# Data refresh intervals
REFRESH_INTERVAL = 300  # 5 minutes for real-time data
CACHE_TTL = 1800  # 30 minutes for cached data
```

### Model Parameters
```python
# Adjustable parameters in the code
RANDOM_FOREST_PARAMS = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 5, 10]
}

POLLUTION_THRESHOLDS = {
    'good': 50,
    'moderate': 100,
    'unhealthy': 150,
    'very_unhealthy': 200
}
```

## 📋 Requirements

### Core Dependencies
- streamlit >= 1.28.0 (web dashboard framework)
- pandas >= 1.5.0 (data manipulation)
- numpy >= 1.24.0 (numerical computing)
- plotly >= 5.15.0 (interactive charts)
- folium >= 0.14.0 (interactive maps)
- requests >= 2.31.0 (API integration)
- reportlab >= 4.0.0 (PDF generation)

### Machine Learning Dependencies
- scikit-learn >= 1.3.0 (ML models)
- imbalanced-learn >= 0.11.0 (SMOTE for data balancing)

### Optional Dependencies
- osmnx >= 1.6.0 (advanced geospatial features)
- geopy >= 2.3.0 (distance calculations)
- seaborn >= 0.12.0 (statistical visualizations)

## 🚀 Deployment

### Local Deployment
```bash
# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run streamlit_dashboard.py
```

### Streamlit Cloud Deployment
1. Fork this repository
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with `streamlit_dashboard.py` as the main file
4. Add API keys in Streamlit Cloud secrets:
   ```toml
   [secrets]
   WAQI_TOKEN = "your_waqi_token_here"
   OPENWEATHER_API_KEY = "your_openweather_key_here"
   ```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
CMD ["streamlit", "run", "streamlit_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🔍 Troubleshooting

### Common Issues

**1. Missing geospatial libraries**
```bash
# Install osmnx and geopy if needed
pip install osmnx geopy
```

**2. API connection issues**
- System automatically falls back to sample data
- Check internet connection and API keys

**3. Memory issues with large datasets**
- Reduce sample size in configuration
- Use data filtering options

**4. Dashboard not loading**
```bash
# Ensure Streamlit is properly installed
pip install --upgrade streamlit
```

## 📈 Performance Optimization

### For Large Datasets
- Enable data sampling in configuration
- Use chunked processing for memory efficiency
- Implement parallel processing for model training

### For Real-Time Applications
- Implement data caching
- Use incremental model updates
- Optimize map rendering with sampling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenAQ for providing pollution data API
- OpenWeatherMap for weather data
- Folium team for interactive mapping capabilities
- Streamlit team for the dashboard framework

## 📞 Support

For issues and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the documentation

## 🆕 Recent Updates

### Version 2.0.0 (October 2024)
- ✅ Real AQI data integration with WAQI API
- ✅ Professional PDF report generation
- ✅ Enhanced dashboard with three distinct views
- ✅ Weather data integration via OpenWeather API
- ✅ Anti-flicker real-time updates
- ✅ Improved theme support and accessibility
- ✅ Mobile-responsive design
- ✅ Performance optimization and caching

### Version 1.0.0 (September 2024)
- ✅ Initial release with synthetic data
- ✅ Machine learning model integration
- ✅ Basic dashboard functionality
- ✅ Geospatial visualization

---

**Last Updated**: October 2024  
**Version**: 2.0.0  
**Status**: Production Ready with Real Data Integration  
**Live Demo**: [Available on Streamlit Cloud]  
**Repository**: [GitHub](https://github.com/amishiverma/Amishi-Verma)