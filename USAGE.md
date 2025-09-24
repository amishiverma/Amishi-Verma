# EnviroScan Usage Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Complete System Test
```bash
python test_system.py
```

### 3. Run Main Analysis
```bash
python enviroscan2_complete.py
```

### 4. Launch Interactive Dashboard
```bash
python create_dashboard.py
streamlit run /tmp/pollution_dashboard.py
```

## Component Usage

### Data Processing
```python
from enviroscan2_complete import fetch_openaq_data, clean_pollution_data, feature_engineering

# Fetch data (with automatic fallback to sample data)
data = fetch_openaq_data("Delhi")

# Clean and process
cleaned = clean_pollution_data(data)
featured = feature_engineering(cleaned)
```

### Source Labeling
```python
from enviroscan2_complete import label_sources

# Apply intelligent source labeling
labeled_data = label_sources(featured_data)
print(labeled_data['source'].value_counts())
```

### Model Training
```python
from enviroscan2_complete import (
    prepare_features, 
    train_multiple_models, 
    evaluate_model_performance
)

# Prepare features and train models
X, feature_names = prepare_features(labeled_data)
models = train_multiple_models(X_train, y_train, X_val, y_val)
performance = evaluate_model_performance(models, X_test, y_test)
```

### Visualization
```python
from enviroscan2_complete import (
    create_pollution_heatmap,
    create_source_map,
    create_multi_layer_map
)

# Create interactive maps
heatmap = create_pollution_heatmap(data)
source_map = create_source_map(data) 
multi_map = create_multi_layer_map(data)
```

## Dashboard Features

The Streamlit dashboard provides:

- **Real-time Monitoring**: Current pollution status with AQI levels
- **Interactive Controls**: City selection, time range, source filtering
- **Visualization**: Trend charts, source distribution, hourly patterns
- **Interactive Maps**: Pollution heatmaps with source markers
- **Alerts**: Automated warnings based on pollution thresholds
- **Export**: Download data and reports in CSV/TXT formats

## Model Performance

Expected performance metrics:
- **Random Forest**: 85-92% accuracy, F1: 0.87-0.91
- **Logistic Regression**: 78-85% accuracy, F1: 0.80-0.86
- **Neural Network**: 82-89% accuracy, F1: 0.84-0.88

## Troubleshooting

### Common Issues

1. **Missing dependencies**: Run `pip install -r requirements.txt`
2. **API connection failures**: System automatically uses sample data
3. **Memory issues**: Reduce sample size in configuration
4. **Streamlit not loading**: Check port 8501 availability

### Performance Tips

- Use data sampling for large datasets
- Enable caching for repeated operations
- Optimize map rendering with point sampling

## Example Output

The system generates:
- Interactive HTML maps
- Performance visualization charts
- Model evaluation reports
- Downloadable pollution data

Run `test_system.py` to see example outputs in `/tmp/` directory.