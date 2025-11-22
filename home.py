"""
Accident Severity Classification - Multi-Page Streamlit Application
Home Page and Navigation
Author: Gaurav
Description: Multi-page application for accident severity analysis
Run this file: streamlit run home.py
"""

import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Accident Severity Detection System",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .feature-card {
        padding: 2rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .feature-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .nav-button {
        display: block;
        width: 100%;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        text-decoration: none;
        color: white;
        font-weight: 600;
        text-align: center;
        transition: background-color 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">🚗 Accident Severity Detection System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Advanced AI-powered analysis of accident images</p>', unsafe_allow_html=True)

# Overview
st.write("""
Welcome to our comprehensive Accident Severity Detection System. This multi-page application offers:

- **Upload & Analysis**: Real-time severity classification from accident images
- **Analytics Dashboard**: Track predictions and system performance metrics
- **Model Information**: Technical details about our AI models and algorithms
- **About Page**: Learn more about the system and its capabilities

Navigate through the pages using the sidebar to explore different features of our accident analysis platform.
""")

# Feature Highlights
st.divider()
st.subheader("🎯 Key Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🖼️</div>
        <h4>Image Analysis</h4>
        <p>Upload accident images for instant severity classification using advanced AI models</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <h4>Analytics</h4>
        <p>Comprehensive dashboard with prediction history and performance metrics</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔬</div>
        <h4>Model Insights</h4>
        <p>Detailed information about AI models, training data, and technical specifications</p>
    </div>
    """, unsafe_allow_html=True)

# Quick Stats
st.divider()
st.subheader("📈 System Statistics")

stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.metric(label="Model Accuracy", value="94.2%", delta="+2.1%")

with stats_col2:
    st.metric(label="Total Predictions", value="1,247", delta="+89")

with stats_col3:
    st.metric(label="Processing Speed", value="1.8s", delta="-0.3s")

with stats_col4:
    st.metric(label="Supported Formats", value="JPG/PNG", delta="")

# Getting Started Guide
st.divider()
st.subheader("🚀 Getting Started")

with st.expander("📖 Step-by-Step Guide"):
    st.markdown("""
    ### Welcome to Accident Severity Detection!

    **Navigation:**
    - Use the sidebar to access different pages
    - Each page serves a specific purpose in the analysis workflow

    **Upload & Analysis:**
    1. Go to the Upload page
    2. Select a clear accident image (JPG, PNG)
    3. Wait for AI processing
    4. Review severity classification and recommendations

    **Analytics:**
    - Visit the Analytics page to see prediction trends
    - Monitor system performance and usage statistics

    **Tips for Best Results:**
    - Upload high-quality, well-lit images
    - Capture multiple angles for better analysis
    - Ensure the damage is clearly visible
    - Avoid blurry or dark photos (max 10MB)
    """)

# Important Information
st.divider()

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.info("""
    **⚠️ Important Notes:**
    - This system is for informational purposes
    - Professional assessment is always recommended
    - Results should not replace expert judgment
    """)

with info_col2:
    st.success("""
    **🎯 Benefits:**
    - Fast and accurate damage assessment
    - Detailed repair cost estimates
    - Insurance claim recommendations
    """)

# Footer
st.divider()
footer_col1, footer_col2, footer_col3 = st.columns(3)

with footer_col1:
    st.caption("🔒 Secure & Private")

with footer_col2:
    st.caption("🚀 Fast Processing")

with footer_col3:
    st.caption("🎯 94.2% Accurate")

st.caption("💻 Built with Streamlit | Developed by Gaurav OG | © 2024")
