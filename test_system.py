#!/usr/bin/env python3
"""
Test script for EnviroScan system
Run this to verify all components are working correctly
"""

import sys
import os
import warnings
warnings.filterwarnings('ignore')

def test_data_processing():
    """Test data processing functionality"""
    print("🧪 Testing Data Processing...")
    
    import numpy as np
    import pandas as pd
    
    # Test data creation
    np.random.seed(42)
    n_samples = 100
    
    data = {
        'parameter': np.random.choice(['pm25', 'no2', 'so2', 'co'], n_samples),
        'value': np.random.exponential(scale=30, size=n_samples),
        'latitude': 28.6139 + np.random.normal(0, 0.05, n_samples),
        'longitude': 77.2090 + np.random.normal(0, 0.05, n_samples),
        'date': pd.date_range('2024-01-01', periods=n_samples, freq='H')
    }
    
    df = pd.DataFrame(data)
    
    # Test pivot operation
    pivot_df = df.pivot_table(
        index=['latitude', 'longitude'],
        columns='parameter',
        values='value',
        aggfunc='mean'
    ).reset_index()
    
    # Test feature engineering
    pivot_df['pollution_index'] = (
        pivot_df.get('pm25', 0) * 0.4 +
        pivot_df.get('no2', 0) * 0.3 +
        pivot_df.get('so2', 0) * 0.2 +
        pivot_df.get('co', 0) * 0.1
    )
    
    print(f"✅ Data processing test passed - Shape: {pivot_df.shape}")
    return True

def test_machine_learning():
    """Test ML functionality"""
    print("🤖 Testing Machine Learning...")
    
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import numpy as np
    import pandas as pd
    
    # Create synthetic dataset
    np.random.seed(42)
    n_samples = 200
    
    data = {
        'PM2.5': np.random.exponential(scale=30, size=n_samples),
        'NO2': np.random.exponential(scale=25, size=n_samples),
        'SO2': np.random.exponential(scale=15, size=n_samples),
        'near_road': np.random.choice([0, 1], n_samples),
        'near_factory': np.random.choice([0, 1], n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Simple labeling
    df['source'] = 'Residential'
    df.loc[(df['NO2'] > df['NO2'].quantile(0.7)) & (df['near_road'] == 1), 'source'] = 'Vehicular'
    df.loc[(df['SO2'] > df['SO2'].quantile(0.6)) & (df['near_factory'] == 1), 'source'] = 'Industrial'
    
    # Train model
    features = ['PM2.5', 'NO2', 'SO2', 'near_road', 'near_factory']
    X = df[features]
    y = df['source']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"✅ ML test passed - Accuracy: {accuracy:.3f}")
    return accuracy > 0.7

def test_visualization():
    """Test visualization functionality"""
    print("🗺️ Testing Visualization...")
    
    import folium
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    
    # Create test data
    np.random.seed(42)
    n_samples = 20
    
    data = {
        'latitude': 28.6139 + np.random.normal(0, 0.02, n_samples),
        'longitude': 77.2090 + np.random.normal(0, 0.02, n_samples),
        'pollution': np.random.exponential(scale=30, size=n_samples),
        'source': np.random.choice(['Vehicular', 'Industrial', 'Residential'], n_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Test Folium map creation
    m = folium.Map(location=[28.6139, 77.2090], zoom_start=12)
    
    for idx, row in df.head(5).iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            popup=f"Source: {row['source']}",
            fill=True
        ).add_to(m)
    
    # Save test map
    m.save('/tmp/test_map_output.html')
    
    # Test matplotlib
    plt.figure(figsize=(8, 6))
    df['source'].value_counts().plot(kind='bar')
    plt.title('Source Distribution Test')
    plt.tight_layout()
    plt.savefig('/tmp/test_chart_output.png')
    plt.close()
    
    print("✅ Visualization test passed")
    return True

def test_dashboard_creation():
    """Test dashboard file creation"""
    print("📱 Testing Dashboard Creation...")
    
    from create_dashboard import create_dashboard_app
    
    app_code = create_dashboard_app()
    
    # Save dashboard
    with open('/tmp/test_dashboard.py', 'w') as f:
        f.write(app_code)
    
    # Check if file was created and has content
    if os.path.exists('/tmp/test_dashboard.py'):
        with open('/tmp/test_dashboard.py', 'r') as f:
            content = f.read()
            if len(content) > 1000:  # Should be substantial
                print("✅ Dashboard creation test passed")
                return True
    
    print("❌ Dashboard creation test failed")
    return False

def run_all_tests():
    """Run all tests"""
    print("🚀 Running EnviroScan System Tests")
    print("=" * 50)
    
    tests = [
        ("Data Processing", test_data_processing),
        ("Machine Learning", test_machine_learning),
        ("Visualization", test_visualization),
        ("Dashboard Creation", test_dashboard_creation)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
            if result:
                print(f"✅ {test_name}: PASSED")
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {str(e)}")
            results.append((test_name, False))
        
        print()
    
    # Summary
    print("=" * 50)
    print("📋 TEST SUMMARY")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"✅ Passed: {passed}/{total}")
    if passed == total:
        print("🎉 All tests passed! System is ready.")
        return True
    else:
        print("⚠️ Some tests failed. Check the output above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)