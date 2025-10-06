# 🚀 EnviroScan Deployment Guide

Complete step-by-step guide to deploy your EnviroScan Air Quality Monitoring Dashboard.

## 📋 Pre-Deployment Checklist

✅ **Files Required:**
- `streamlit_dashboard.py` (Main application)
- `real_aqi_data.py` (API integration)
- `data_loader.py` (Data processing)
- `requirements.txt` (Dependencies)
- `README.md` (Documentation)

✅ **Dependencies Installed:**
- All packages from requirements.txt
- Python 3.8+ environment

## 🏠 Local Deployment

### Step 1: Install Dependencies
```bash
# Navigate to project directory
cd "C:\Users\Amishi Verma\OneDrive\Documents\EnviroScan\Amishi-Verma"

# Install all requirements
pip install -r requirements.txt
```

### Step 2: Configure API Keys (Optional for Real Data)
Edit `real_aqi_data.py`:
```python
# Line 15-16: Replace with your actual API keys
WAQI_TOKEN = "your_waqi_token_here"  # Get from https://aqicn.org/api/
OPENWEATHER_API_KEY = "your_openweather_key_here"  # Get from https://openweathermap.org/api
```

### Step 3: Launch Dashboard
```bash
streamlit run streamlit_dashboard.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

## ☁️ Streamlit Cloud Deployment

### Step 1: Prepare Repository
Your code is already on GitHub at: `https://github.com/amishiverma/Amishi-Verma`

### Step 2: Deploy to Streamlit Cloud
1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Connect your GitHub account
4. Select repository: `amishiverma/Amishi-Verma`
5. Set main file: `streamlit_dashboard.py`
6. Click "Deploy"

### Step 3: Add API Keys (Optional)
In Streamlit Cloud Advanced Settings:
```toml
[secrets]
WAQI_TOKEN = "your_waqi_token_here"
OPENWEATHER_API_KEY = "your_openweather_key_here"
```

## 🐳 Docker Deployment

### Step 1: Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run the application
CMD ["streamlit", "run", "streamlit_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Step 2: Create .dockerignore
```
__pycache__
*.pyc
*.pyo
*.pyd
.git
.gitignore
README.md
.env
.venv
```

### Step 3: Build and Run
```bash
# Build Docker image
docker build -t enviroscan-dashboard .

# Run container (with API keys as environment variables)
docker run -p 8501:8501 \
  -e WAQI_TOKEN="your_waqi_token_here" \
  -e OPENWEATHER_API_KEY="your_openweather_key_here" \
  enviroscan-dashboard
```

## 🌐 Heroku Deployment

### Step 1: Create Heroku App
```bash
# Install Heroku CLI first
heroku create enviroscan-dashboard
```

### Step 2: Create Procfile
```
web: sh setup.sh && streamlit run streamlit_dashboard.py --server.port=$PORT --server.address=0.0.0.0
```

### Step 3: Create setup.sh
```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

### Step 4: Deploy
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

## 🔧 Configuration Options

### Environment Variables
- `WAQI_TOKEN`: Your WAQI API token
- `OPENWEATHER_API_KEY`: Your OpenWeather API key
- `STREAMLIT_SERVER_PORT`: Port for the application (default: 8501)

### Dashboard Settings
Configure in the sidebar:
- **Theme**: Light/Dark mode toggle
- **Data Source**: Real AQI data vs Synthetic data
- **City Selection**: Choose from 8+ Indian cities
- **View Selection**: Historical/Prediction/Real-time

## 🧪 Testing Your Deployment

### 1. Basic Functionality Test
- ✅ Dashboard loads without errors
- ✅ All three views (Historical, Prediction, Real-time) work
- ✅ Theme toggle functions correctly
- ✅ City selection updates data

### 2. API Integration Test (if enabled)
- ✅ Enable "Use Real AQI Data" checkbox
- ✅ Real-time data loads in Real-Time AQI view
- ✅ Weather information displays correctly
- ✅ Fallback to synthetic data works if API fails

### 3. Export Functionality Test
- ✅ PDF report generation works
- ✅ CSV export downloads successfully
- ✅ Reports contain correct data and formatting

## 🚨 Troubleshooting

### Common Issues & Solutions

**1. Dashboard won't start**
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall streamlit
pip uninstall streamlit
pip install streamlit>=1.28.0
```

**2. Module import errors**
```bash
# Install missing packages
pip install -r requirements.txt --upgrade
```

**3. API errors**
- Check internet connection
- Verify API keys are correct
- Dashboard should fallback to synthetic data automatically

**4. Memory issues**
```bash
# Reduce data sampling in configuration
# Or increase system memory allocation
```

## 📊 Performance Monitoring

### Streamlit Cloud
- Monitor app usage in Streamlit Cloud dashboard
- Check logs for errors
- Monitor resource usage

### Local/Docker Deployment
```bash
# Check resource usage
docker stats enviroscan-dashboard

# View logs
docker logs enviroscan-dashboard
```

## 🔄 Updates & Maintenance

### Updating the Application
1. Make changes to your code
2. Commit and push to GitHub
3. Streamlit Cloud will auto-redeploy
4. For Docker: rebuild and restart container

### Monitoring API Usage
- WAQI API: Monitor usage at https://aqicn.org/api/
- OpenWeather API: Check usage at https://openweathermap.org/api

## 🎯 Production Recommendations

### For High Traffic
- Use caching extensively
- Implement rate limiting
- Monitor API quotas
- Consider paid API tiers

### For Enterprise Use
- Set up monitoring and alerting
- Implement user authentication
- Add database storage for historical data
- Set up automated backups

## 📞 Support

If you encounter issues:
1. Check this deployment guide
2. Review error logs
3. Test locally first
4. Check GitHub issues
5. Verify API status

---

**Deployment Guide Version**: 2.0.0  
**Last Updated**: October 2024  
**Compatible with**: EnviroScan v2.0.0+