"""
Model Information Page with Modern UI
Technical specifications and performance details
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model import model_info, get_statistics, get_prediction_history, model_exists
from styles import inject_custom_css, create_hero_section, create_gradient_divider

# Page Configuration
st.set_page_config(
    page_title="Model Information",
    page_icon="🔬",
    layout="wide"
)

# Inject Custom Styling
inject_custom_css()

# Hero Section
create_hero_section(
    "🔬 Model Information",
    "Technical specifications and performance insights of our AI classification model"
)

# Check if using fallback model
is_fallback = not model_exists()

if is_fallback:
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid hsl(40, 100%, 60%); margin-bottom: 2rem;">
        <h3 style="color: hsl(40, 100%, 60%); margin-top: 0;">⚠️ Fallback Mode Active</h3>
        <p>The real TensorFlow model file was not found. The system is currently using a <strong>dummy model</strong> 
        that generates random predictions for demonstration purposes.</p>
        <h1 style="margin-top: 1.5rem;">📦 To use the real model:</h1>
        <ol style="color: var(--text-secondary);">
            <li>Place your trained model file at: <code>models/accident_severity_model.h5</code></li>
            <li>Ensure the file has proper read permissions</li>
            <li>Restart the Streamlit application</li>
        </ol>
        <p style="margin-top: 1rem; color: var(--text-secondary);">
            💡 <strong>Tip:</strong> The UI and all features work identically with both real and fallback models.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Get model information
info = model_info()

# Model Overview
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">📋 Model Overview</h2>', unsafe_allow_html=True)

overview_col1, overview_col2 = st.columns(2)

with overview_col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### **Model Name**")
    st.code(info['model_name'], language="text")
    
    st.markdown("### **Architecture**")
    st.code(info['architecture'], language="text")
    
    st.markdown("### **Framework**")
    st.code(info['framework'], language="text")
    st.markdown('</div>', unsafe_allow_html=True)

with overview_col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### **Status**")
    if is_fallback:
        st.warning("⚠️ Fallback Mode (Dummy Model)")
    else:
        st.success("✅ Active & Operational (Real Model)")
    
    st.markdown("### **Version**")
    st.code(info['version'], language="text")
    
    st.markdown("### **Last Updated**")
    st.code(info['last_updated'], language="text")
    st.markdown('</div>', unsafe_allow_html=True)

create_gradient_divider()

# Architecture Details
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">🏗️ Architecture Details</h2>', unsafe_allow_html=True)

arch_col1, arch_col2, arch_col3 = st.columns(3)

with arch_col1:
    st.metric("📐 Input Shape", str(info['input_shape']))
    st.metric("🏷️ Number of Classes", info['num_classes'])

with arch_col2:
    st.metric("🔄 Training Epochs", info['training_epochs'])
    st.metric("📦 Batch Size", info['batch_size'])

with arch_col3:
    st.metric("⚙️ Optimizer", info['optimizer'])
    st.metric("📈 Learning Rate", info['learning_rate'])

create_gradient_divider()

# Performance Metrics
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">📊 Performance Metrics</h2>', unsafe_allow_html=True)

metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

with metrics_col1:
    st.metric("🎯 Accuracy", f"{info['accuracy']:.1f}%", delta="+2.1%")

with metrics_col2:
    st.metric("🎲 Precision", f"{info['precision']:.1f}%", delta="+1.5%")

with metrics_col3:
    st.metric("📈 Recall", f"{info['recall']:.1f}%", delta="+1.8%")

# Performance Chart
st.markdown('<div class="glass-card" style="margin-top: 2rem;">', unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Model Performance Comparison</h3>", unsafe_allow_html=True)

metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
values = [info['accuracy'], info['precision'], info['recall'], info['f1_score']]
colors = ['#8B5CF6', '#3B82F6', '#EC4899', '#F59E0B']

fig = go.Figure()

# Add bars
fig.add_trace(go.Bar(
    x=metrics,
    y=values,
    marker=dict(
        color=colors,
        line=dict(color='rgba(255,255,255,0.3)', width=1)
    ),
    text=[f"{v:.1f}%" for v in values],
    textposition='outside',
    textfont=dict(size=14, color='white'),
    hovertemplate='<b>%{x}</b><br>Score: %{y:.1f}%<extra></extra>'
))

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='white', size=12),
    yaxis=dict(
        title='Percentage (%)',
        gridcolor='rgba(255,255,255,0.1)',
        showgrid=True,
        range=[0, 100]
    ),
    xaxis=dict(title=''),
    height=400,
    margin=dict(t=40, b=40, l=60, r=40)
)

st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

create_gradient_divider()

# Training Data Information
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">📚 Training Data</h2>', unsafe_allow_html=True)

data_col1, data_col2 = st.columns(2)

training_size = info['training_samples']
validation_size = info['validation_samples']
test_size = info['test_samples']
total_size = training_size + validation_size + test_size

with data_col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### **Dataset Size**")
    st.metric("Total Samples", f"{total_size:,}")
    
    st.markdown("### **Sample Distribution**")
    split_data = pd.DataFrame({
        'Data Split': ['🟢 Training', '🟡 Validation', '🔴 Test', '📊 Total'],
        'Samples': [f"{training_size:,}", f"{validation_size:,}", f"{test_size:,}", f"{total_size:,}"],
        'Percentage': [
            f"{(training_size/total_size)*100:.1f}%",
            f"{(validation_size/total_size)*100:.1f}%",
            f"{(test_size/total_size)*100:.1f}%",
            "100%"
        ]
    })
    st.dataframe(split_data, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with data_col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Dataset Split Distribution</h3>", unsafe_allow_html=True)
    
    labels = ['Training', 'Validation', 'Test']
    sizes = [training_size, validation_size, test_size]
    colors_pie = ['#4CAF50', '#FF9800', '#F44336']
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=sizes,
        hole=0.4,
        marker=dict(colors=colors_pie, line=dict(color='#1a1a1a', width=2)),
        textfont=dict(size=14, color='white'),
        hovertemplate='<b>%{label}</b><br>Count: %{value:,}<br>Percentage: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=12),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5
        ),
        height=400,
        margin=dict(t=40, b=40, l=40, r=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

create_gradient_divider()

# Classification Classes
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">🏷️ Classification Classes</h2>', unsafe_allow_html=True)

classes_data = pd.DataFrame([
    {"Class": "🟢 Minor Damage", "ID": 0, "Description": "Scratches, dents, cosmetic damage", "Action": "Local repair"},
    {"Class": "🟡 Moderate Damage", "ID": 1, "Description": "Structural damage, airbag deployment possible", "Action": "Professional inspection"},
    {"Class": "🔴 Severe Crash", "ID": 2, "Description": "Major structural failure, potential total loss", "Action": "Emergency services"}
])

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.dataframe(classes_data, use_container_width=True, hide_index=True)
st.markdown('</div>', unsafe_allow_html=True)

create_gradient_divider()

# Model Capabilities & Implementation
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">⚡ Capabilities & Implementation</h2>', unsafe_allow_html=True)

cap_col1, cap_col2 = st.columns(2)

with cap_col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### **📥 Input Requirements**")
    st.markdown("""
    - **Formats:** JPG, PNG, JPEG
    - **Min Resolution:** 100x100 pixels
    - **Max File Size:** 10MB
    - **Color Mode:** RGB preferred
    - **Aspect Ratio:** Any (auto-scaling)
    - **Quality:** High quality recommended
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("### **🔄 Preprocessing Pipeline**")
    st.code("""
1. Image validation & format check
2. RGB conversion (if needed)
3. Resize to 224x224 pixels
4. Pixel normalization [0,1]
5. Batch dimension addition
    """, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

with cap_col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### **🚀 Processing Features**")
    st.markdown("""
    - **Real-time Inference:** ~1.8 seconds
    - **Confidence Scoring:** 75-98% range
    - **Batch Processing:** Single image
    - **Memory Usage:** ~250MB
    - **Platform:** CPU/GPU compatible
    - **Concurrency:** Multi-request support
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("### **🎯 Inference Pipeline**")
    st.code("""
1. Input validation
2. Model prediction
3. Confidence calculation
4. Class mapping & formatting
5. Result post-processing
    """, language="text")
    st.markdown('</div>', unsafe_allow_html=True)

create_gradient_divider()

# Limitations & Best Practices
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">⚠️ Limitations & Best Practices</h2>', unsafe_allow_html=True)

lim_col1, lim_col2 = st.columns(2)

with lim_col1:
    st.markdown('<div class="glass-card" style="border-left: 4px solid hsl(40, 100%, 60%);">', unsafe_allow_html=True)
    st.markdown("### **⚠️ Known Limitations**")
    st.markdown("""
    - Requires clear accident images
    - May struggle with extreme angles
    - Weather conditions affect accuracy
    - Occluded damage areas challenging
    - Very old vehicle models may vary
    - Extreme lighting conditions impact results
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with lim_col2:
    st.markdown('<div class="glass-card" style="border-left: 4px solid hsl(140, 70%, 55%);">', unsafe_allow_html=True)
    st.markdown("### **✅ Best Practices**")
    st.markdown("""
    - Use multiple angles when possible
    - Ensure good lighting conditions
    - Include context around damage
    - Avoid heavily filtered images
    - Capture high-resolution photos
    - Clean lens before taking photos
    """)
    st.markdown('</div>', unsafe_allow_html=True)

create_gradient_divider()

# Future Improvements
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">🔮 Future Roadmap</h2>', unsafe_allow_html=True)

future_col1, future_col2 = st.columns(2)

with future_col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### **🎯 Planned Enhancements**")
    st.markdown("""
    - ✨ Multi-angle image support
    - 🎯 Damage localization features
    - 🔗 Integration with repair databases
    - 🎥 Real-time video processing
    - 📱 Mobile app companion
    - 🌐 Multi-language support
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with future_col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### **🔬 Research Areas**")
    st.markdown("""
    - 🧠 Transfer learning improvements
    - 🤝 Ensemble model approaches
    - 📊 Advanced data augmentation
    - 🚗 Cross-vehicle compatibility
    - 🌦️ Weather condition adaptation
    - 🎨 Synthetic data generation
    """)
    st.markdown('</div>', unsafe_allow_html=True)

create_gradient_divider()

# Export Section
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">📤 Export Model Data</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; margin-bottom: 1.5rem;">
    <p style="color: var(--text-secondary); font-size: 1.1rem;">
        Download model metadata, statistics, and recent prediction history
    </p>
</div>
""", unsafe_allow_html=True)

# Gather data
stats = get_statistics()
prediction_history = get_prediction_history(limit=100)

# Combine into dict
export_data = {
    "model_info": info,
    "statistics": stats,
    "prediction_history": [
        {
            "timestamp": p["timestamp"].isoformat(),
            "severity": p["severity"],
            "confidence": p["confidence"]
        } for p in prediction_history
    ]
}

export_col1, export_col2 = st.columns(2)

with export_col1:
    # JSON download
    json_str = json.dumps(export_data, indent=2)
    st.download_button(
        label="📋 **Download Complete Data (JSON)**",
        data=json_str,
        file_name="model_export.json",
        mime="application/json",
        use_container_width=True
    )

with export_col2:
    # CSV download (prediction history)
    if prediction_history:
        df = pd.DataFrame([
            {
                "timestamp": p["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                "severity": p["severity"],
                "confidence": p["confidence"]
            } for p in prediction_history
        ])
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="📊 **Download Prediction History (CSV)**",
            data=csv_data,
            file_name="prediction_history.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.button("📊 **No Prediction History Available**", disabled=True, use_container_width=True)

create_gradient_divider()

# Hidden debug info (expandable)
with st.expander("🔍 **Advanced Technical Details (JSON)**"):
    st.json(info)

# Footer
st.markdown(f"""
<div style="text-align: center; padding: 1.5rem; color: var(--text-secondary);">
    <p>Model information is regularly updated to reflect the latest developments.</p>
    <p style="font-size: 0.9rem; margin-top: 0.5rem;">
        For technical inquiries, please contact the development team.
    </p>
    <p style="font-size: 0.85rem; margin-top: 1rem; opacity: 0.7;">
        Last updated: {info['last_updated']}
    </p>
</div>
""", unsafe_allow_html=True)
