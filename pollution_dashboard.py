import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import folium
from streamlit_folium import st_folium
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="EnviroScan - Pollution Source Identifier",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .alert-high {
        background-color: #ffebee;
        border-left: 5px solid #f44336;
        padding: 1rem;
        margin: 1rem 0;
    }
    .alert-medium {
        background-color: #fff3e0;
        border-left: 5px solid #ff9800;
        padding: 1rem;
        margin: 1rem 0;
    }
    .alert-low {
        background-color: #e8f5e8;
        border-left: 5px solid #4caf50;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">🌍 EnviroScan Pollution Source Identifier</h1>', 
           unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.header("🔧 Configuration")

# City input
city = st.sidebar.text_input("📍 Enter City Name", value="Delhi", key="city_input")

# Coordinate inputs
st.sidebar.subheader("📍 Custom Coordinates (Optional)")
use_coordinates = st.sidebar.checkbox("Use custom coordinates")

if use_coordinates:
    latitude = st.sidebar.number_input("Latitude", value=28.6139, format="%.4f")
    longitude = st.sidebar.number_input("Longitude", value=77.2090, format="%.4f") 
else:
    latitude, longitude = 28.6139, 77.2090  # Default to Delhi

# Time range selection
st.sidebar.subheader("📅 Time Range")
time_range = st.sidebar.selectbox(
    "Select time period",
    ["Last 24 hours", "Last 7 days", "Last 30 days", "Custom range"]
)

# Pollution source filter
st.sidebar.subheader("🏭 Source Filter")
source_filter = st.sidebar.multiselect(
    "Select pollution sources",
    ["All", "Vehicular", "Industrial", "Agricultural", "Residential", "Natural"],
    default=["All"]
)

# Analysis button
analyze_button = st.sidebar.button("🔍 Analyze Pollution", type="primary")

@st.cache_data
def generate_sample_data(city_name, lat, lon, n_samples=200):
    """Generate sample pollution data for demonstration"""
    np.random.seed(42)
    
    # Generate timestamps
    end_time = datetime.now()
    start_time = end_time - timedelta(days=7)
    timestamps = pd.date_range(start_time, end_time, periods=n_samples)
    
    # Generate coordinates around the specified location
    lats = lat + np.random.normal(0, 0.05, n_samples)
    lons = lon + np.random.normal(0, 0.05, n_samples)
    
    # Generate pollution data with realistic patterns
    hours = [t.hour for t in timestamps]
    base_pm25 = 30 + 20 * np.sin(np.array(hours) * np.pi / 12)  # Daily pattern
    base_no2 = 25 + 15 * np.sin(np.array(hours) * np.pi / 12 + np.pi/4)
    
    data = {
        'timestamp': timestamps,
        'latitude': lats,
        'longitude': lons,
        'PM2.5': np.maximum(base_pm25 + np.random.normal(0, 10, n_samples), 0),
        'NO2': np.maximum(base_no2 + np.random.normal(0, 8, n_samples), 0),
        'SO2': np.maximum(np.random.exponential(15, n_samples), 0),
        'CO': np.maximum(np.random.exponential(1.2, n_samples), 0),
        'temperature': 25 + 10 * np.sin(np.array(hours) * np.pi / 12) + np.random.normal(0, 3, n_samples),
        'humidity': 60 + 20 * np.random.random(n_samples),
        'source': np.random.choice(['Vehicular', 'Industrial', 'Agricultural', 'Residential'], n_samples),
        'confidence': 0.7 + 0.3 * np.random.random(n_samples)
    }
    
    df = pd.DataFrame(data)
    df['pollution_index'] = (df['PM2.5'] * 0.4 + df['NO2'] * 0.3 + df['SO2'] * 0.2 + df['CO'] * 0.1)
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.day_name()
    
    return df

def get_aqi_level(pollution_index):
    """Determine AQI level and color"""
    if pollution_index <= 50:
        return "Good", "#4CAF50", "😊"
    elif pollution_index <= 100:
        return "Moderate", "#FFC107", "😐"  
    elif pollution_index <= 150:
        return "Unhealthy for Sensitive Groups", "#FF9800", "😷"
    elif pollution_index <= 200:
        return "Unhealthy", "#F44336", "😨"
    else:
        return "Very Unhealthy", "#9C27B0", "💀"

def create_alert(pollution_index, source):
    """Create pollution alert based on levels"""
    level, color, emoji = get_aqi_level(pollution_index)
    
    if pollution_index > 150:
        alert_class = "alert-high"
        urgency = "🚨 CRITICAL ALERT"
        recommendation = "Avoid outdoor activities. Use air purifiers indoors."
    elif pollution_index > 100:
        alert_class = "alert-medium"  
        urgency = "⚠️ WARNING"
        recommendation = "Limit prolonged outdoor exposure."
    else:
        alert_class = "alert-low"
        urgency = "✅ NORMAL"
        recommendation = "Air quality is acceptable for most people."
    
    alert_html = f"""
    <div class="{alert_class}">
        <h4>{urgency}</h4>
        <p><strong>Current AQI Level:</strong> {level} ({pollution_index:.1f}) {emoji}</p>
        <p><strong>Primary Source:</strong> {source}</p>
        <p><strong>Recommendation:</strong> {recommendation}</p>
    </div>
    """
    
    st.markdown(alert_html, unsafe_allow_html=True)

# Main analysis section
if analyze_button or city:
    with st.spinner(f"🔄 Analyzing pollution data for {city}..."):
        # Generate or load data
        df = generate_sample_data(city, latitude, longitude)
        
        # Apply source filter
        if "All" not in source_filter:
            df = df[df['source'].isin(source_filter)]
        
        # Current pollution status
        st.header("📊 Current Pollution Status")
        
        latest_data = df.iloc[-1]
        current_pollution = latest_data['pollution_index']
        primary_source = latest_data['source']
        
        # Create alert
        create_alert(current_pollution, primary_source)
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="🌫️ PM2.5",
                value=f"{latest_data['PM2.5']:.1f} µg/m³",
                delta=f"{np.random.uniform(-5, 5):.1f}"
            )
        
        with col2:
            st.metric(
                label="🚗 NO2", 
                value=f"{latest_data['NO2']:.1f} µg/m³",
                delta=f"{np.random.uniform(-3, 3):.1f}"
            )
        
        with col3:
            st.metric(
                label="🏭 SO2",
                value=f"{latest_data['SO2']:.1f} µg/m³", 
                delta=f"{np.random.uniform(-2, 2):.1f}"
            )
        
        with col4:
            st.metric(
                label="🔥 CO",
                value=f"{latest_data['CO']:.2f} mg/m³",
                delta=f"{np.random.uniform(-0.5, 0.5):.2f}"
            )
        
        # Charts section
        st.header("📈 Pollution Trends")
        
        # Time series chart
        fig_timeline = px.line(
            df, 
            x='timestamp', 
            y=['PM2.5', 'NO2', 'SO2'], 
            title="Pollutant Levels Over Time",
            color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
        )
        fig_timeline.update_layout(height=400)
        st.plotly_chart(fig_timeline, use_container_width=True)
        
        # Source distribution
        col1, col2 = st.columns(2)
        
        with col1:
            source_counts = df['source'].value_counts()
            fig_pie = px.pie(
                values=source_counts.values,
                names=source_counts.index,
                title="Pollution Source Distribution",
                color_discrete_sequence=px.colors.qualitative.Set3
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Hourly pollution pattern
            hourly_pollution = df.groupby('hour')['pollution_index'].mean().reset_index()
            fig_hourly = px.bar(
                hourly_pollution,
                x='hour',
                y='pollution_index', 
                title="Average Pollution by Hour",
                color='pollution_index',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig_hourly, use_container_width=True)
        
        # Interactive map
        st.header("🗺️ Interactive Pollution Map")
        
        # Create Folium map
        m = folium.Map(
            location=[latitude, longitude],
            zoom_start=11,
            tiles='OpenStreetMap'
        )
        
        # Add source-colored markers
        source_colors = {
            'Vehicular': 'red',
            'Industrial': 'darkred',
            'Agricultural': 'green', 
            'Residential': 'blue'
        }
        
        for idx, row in df.sample(min(50, len(df))).iterrows():
            popup_text = f"""
            <b>Source:</b> {row['source']}<br>
            <b>PM2.5:</b> {row['PM2.5']:.1f} µg/m³<br>
            <b>Pollution Index:</b> {row['pollution_index']:.1f}<br>
            <b>Confidence:</b> {row['confidence']:.2f}
            """
            
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=max(5, row['pollution_index'] / 10),
                popup=popup_text,
                color=source_colors.get(row['source'], 'gray'),
                fill=True,
                fillOpacity=0.7
            ).add_to(m)
        
        # Display map
        try:
            map_data = st_folium(m, width=700, height=500)
        except:
            st.write("Interactive map would be displayed here (requires streamlit-folium)")
        
        # Recommendations section
        st.header("💡 Recommendations")
        
        recommendations = []
        if current_pollution > 150:
            recommendations.extend([
                "🏠 Stay indoors and use air purifiers",
                "😷 Wear N95 masks when going outside", 
                "🚫 Avoid outdoor exercise",
                "🌬️ Keep windows closed"
            ])
        elif current_pollution > 100:
            recommendations.extend([
                "⏰ Limit outdoor activities during peak hours",
                "😷 Consider wearing masks outdoors",
                "🏃‍♂️ Reduce intense outdoor exercise"
            ])
        else:
            recommendations.extend([
                "✅ Air quality is generally acceptable",
                "🏃‍♂️ Outdoor activities are safe for most people",
                "🌅 Consider exercising in early morning hours"
            ])
        
        for rec in recommendations:
            st.write(f"• {rec}")
        
        # Download section
        st.header("📥 Download Reports")
        
        col1, col2 = st.columns(2)
        
        with col1:
            csv_data = df.to_csv(index=False)
            st.download_button(
                label="📊 Download Data (CSV)",
                data=csv_data,
                file_name=f"pollution_data_{city}_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        
        with col2:
            # Create summary report
            current_aqi_level = get_aqi_level(current_pollution)[0]
            summary_report = f"""Pollution Analysis Report - {city}
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Current Status:
- Pollution Index: {current_pollution:.1f}
- Primary Source: {primary_source}
- AQI Level: {current_aqi_level}

Key Statistics:
- Average PM2.5: {df['PM2.5'].mean():.1f} µg/m³
- Average NO2: {df['NO2'].mean():.1f} µg/m³
- Peak Pollution Hour: {df.groupby('hour')['pollution_index'].mean().idxmax()}
- Most Common Source: {df['source'].mode()[0]}
"""
            
            st.download_button(
                label="📄 Download Report (TXT)",
                data=summary_report,
                file_name=f"pollution_report_{city}_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain"
            )

else:
    # Welcome screen
    st.info("👈 Please enter a city name and click 'Analyze Pollution' to begin the analysis.")
    
    # Sample visualizations
    st.subheader("🌟 What You'll Get:")
    st.write("• **Real-time pollution monitoring** with AQI levels")
    st.write("• **Source identification** using AI models")  
    st.write("• **Interactive maps** with pollution hotspots")
    st.write("• **Trend analysis** and predictions")
    st.write("• **Health recommendations** based on pollution levels")
    st.write("• **Downloadable reports** for further analysis")

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #666;">'
    "🌍 EnviroScan - AI-Powered Pollution Source Identification System<br>"
    "Built with Streamlit • Data visualization with Plotly • Maps with Folium"
    "</div>", 
    unsafe_allow_html=True
)
