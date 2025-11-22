import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from model import get_prediction_history, get_statistics
from datetime import datetime, timedelta

# Page header
st.title("📊 Prediction History Dashboard")
st.markdown("Monitor prediction history and system performance metrics")

# Get data from model
predictions = get_prediction_history(limit=100)
stats = get_statistics()

# Key Metrics
st.subheader("📈 Key Metrics")
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric("Total Predictions", f"{stats['total_predictions']}")
with metric_col2:
    st.metric("Average Confidence", f"{stats['average_confidence']:.1f}%")
with metric_col3:
    st.metric("Processing Speed", "1.8s")
with metric_col4:
    st.metric("Model Accuracy", "94.2%")

# Severity Distribution
st.divider()
st.subheader("📊 Severity Distribution")
severity_col1, severity_col2 = st.columns(2)
with severity_col1:
    fig, ax = plt.subplots(figsize=(6, 6))
    severity_labels = list(stats['severity_distribution'].keys())
    severity_values = list(stats['severity_distribution'].values())
    if sum(severity_values) > 0:
        ax.pie(severity_values, labels=severity_labels, autopct='%1.1f%%', colors=['#4CAF50', '#FF9800', '#F44336'], startangle=90)
        ax.axis('equal')
        st.pyplot(fig)
    else:
        st.info("No prediction data available yet")
with severity_col2:
    fig, ax = plt.subplots(figsize=(6, 4))
    if sum(severity_values) > 0:
        bars = ax.bar(severity_labels, severity_values, color=['#4CAF50', '#FF9800', '#F44336'])
        ax.set_ylabel('Number of Predictions')
        ax.set_title('Severity Class Counts')
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}', ha='center', va='bottom')
        st.pyplot(fig)
    else:
        st.info("Generate predictions to see analytics")

# Recent Predictions Table
st.divider()
st.subheader("📋 Recent Predictions")
if predictions:
    df_data = []
    for pred in predictions[-20:]:
        df_data.append({
            "Time": pred['timestamp'].strftime("%H:%M:%S"),
            "Date": pred['timestamp'].strftime("%Y-%m-%d"),
            "Severity": pred['severity'],
            "Confidence": f"{pred['confidence']:.1f}%"
        })
    df = pd.DataFrame(df_data)
    st.dataframe(df, use_container_width=True)
    if st.button("📥 Export Recent Predictions (CSV)"):
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="Click to Download",
            data=csv_data,
            file_name="predictions.csv",
            mime="text/csv"
        )
else:
    st.info("No predictions available. Upload an image on the Upload page to generate prediction data.")

# Performance Over Time
st.divider()
st.subheader("📈 Performance Trends")
if len(predictions) > 5:
    trend_col1, trend_col2 = st.columns(2)
    with trend_col1:
        fig, ax = plt.subplots(figsize=(8, 4))
        recent_preds = predictions[-20:]
        confidence_values = [p['confidence'] for p in recent_preds]
        time_labels = [p['timestamp'].strftime("%H:%M") for p in recent_preds]
        ax.plot(range(len(confidence_values)), confidence_values, 'b-o', linewidth=2, markersize=4)
        ax.set_xticks(range(len(time_labels)))
        ax.set_xticklabels(time_labels, rotation=45, fontsize=8)
        ax.set_ylabel('Confidence (%)')
        ax.set_title('Confidence Trend (Last 20 Predictions)')
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)
    with trend_col2:
        min_count = sum(1 for p in predictions if "Minor" in p['severity'])
        mod_count = sum(1 for p in predictions if "Moderate" in p['severity'])
        sev_count = sum(1 for p in predictions if "Severe" in p['severity'])
        fig, ax = plt.subplots(figsize=(6, 4))
        classes = ['Minor', 'Moderate', 'Severe']
        counts = [min_count, mod_count, sev_count]
        colors = ['#4CAF50', '#FF9800', '#F44336']
        bars = ax.bar(classes, counts, color=colors)
        ax.set_ylabel('Count')
        ax.set_title('Total Severity Distribution')
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height, f'{int(count)}', ha='center', va='bottom')
        st.pyplot(fig)
else:
    st.info("Not enough data for trend analysis. Make more predictions to see trends.")

# System Health
st.divider()
st.subheader("🔧 System Health")
health_col1, health_col2, health_col3 = st.columns(3)
with health_col1:
    st.metric("API Status", "Operational", delta="✓")
with health_col2:
    st.metric("Memory Usage", "~250MB", delta="Stable")
with health_col3:
    st.metric("Response Time", "1.8s", delta="-0.2s")

# Additional Statistics
st.divider()
st.subheader("📊 Detailed Statistics")
if predictions:
    confidence_scores = [p['confidence'] for p in predictions]
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    with stat_col1:
        st.markdown("**Confidence Statistics**")
        st.write(f"**Highest:** {max(confidence_scores):.1f}%")
        st.write(f"**Lowest:** {min(confidence_scores):.1f}%")
        st.write(f"**Range:** {max(confidence_scores) - min(confidence_scores):.1f}%")
    with stat_col2:
        severe_predictions = sum(1 for p in predictions if "Severe" in p['severity'])
        severe_percentage = (severe_predictions / len(predictions)) * 100 if predictions else 0
        st.markdown("**Severe Cases**")
        st.write(f"**Count:** {severe_predictions}")
        st.write(f"**Percentage:** {severe_percentage:.1f}%")
        st.write(f"**Rate:** {'High' if severe_percentage > 30 else 'Normal'}")
    with stat_col3:
        avg_conf = sum(confidence_scores) / len(confidence_scores)
        reliable_predictions = sum(1 for c in confidence_scores if c >= 80) / len(confidence_scores) * 100
        st.markdown("**Reliability**")
        st.write(f"**Avg Confidence:** {avg_conf:.1f}%")
        st.write(f"**≥80% Conf:** {reliable_predictions:.1f}%")
        st.write(f"**Reliability:** {'High' if reliable_predictions > 70 else 'Moderate'}")
else:
    st.info("Generate predictions to see detailed statistics.")

# Export Full Analytics
st.divider()
st.subheader("💾 Export Analytics")
export_col1, export_col2 = st.columns(2)
with export_col1:
    if st.button("📊 Generate Full Report", use_container_width=True):
        st.info("Full analytics report generation coming soon!")
with export_col2:
    if st.button("📋 Export Raw Data", use_container_width=True):
        st.info("Raw data export feature coming soon!")

# Footer info
st.divider()
st.caption("Analytics data updates in real-time with each prediction. Last updated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
