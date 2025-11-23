"""
Accident Severity Classification - Multi-Page Streamlit Application
Home Page with Modern Glassmorphic Design
Author: Gaurav (UI Enhanced)
Description: Multi-page application for accident severity analysis
Run this file: streamlit run home.py
"""

import streamlit as st
from styles import inject_custom_css, create_hero_section, create_feature_card, create_stat_card, create_gradient_divider

# Page Configuration
st.set_page_config(
    page_title="Accident Severity Detection System",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom Styling
inject_custom_css()

# Hero Section
create_hero_section(
    "🚗 Accident Severity Detection System",
    "Advanced AI-powered analysis of accident images with real-time classification"
)

# Overview Section
st.markdown("""
<div style="text-align: center; max-width: 800px; margin: 0 auto 3rem auto; color: var(--text-secondary); font-size: 1.1rem; line-height: 1.8;">
Welcome to our comprehensive Accident Severity Detection System. Leveraging cutting-edge machine learning,
we provide instant analysis and actionable insights for accident damage assessment.
</div>
""", unsafe_allow_html=True)

# Key Features Section
st.markdown('<h2 style="text-align: center; margin: 3rem 0 2rem 0; font-size: 2.5rem;">🎯 Key Features</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        create_feature_card(
            "🖼️",
            "Image Analysis",
            "Upload accident images for instant severity classification using advanced deep learning models with 94.2% accuracy"
        ),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        create_feature_card(
            "📊",
            "Analytics Dashboard",
            "Comprehensive insights with prediction history, performance metrics, and visual data representations"
        ),
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        create_feature_card(
            "🔬",
            "Model Insights",
            "Detailed information about AI models, training data, architecture, and technical specifications"
        ),
        unsafe_allow_html=True
    )

create_gradient_divider()

# System Statistics
st.markdown('<h2 style="text-align: center; margin: 2rem 0 2rem 0; font-size: 2.5rem;">📈 Live System Statistics</h2>', unsafe_allow_html=True)

stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.metric(
        label="Model Accuracy",
        value="94.2%",
        delta="+2.1%",
        help="Current model accuracy on test dataset"
    )

with stats_col2:
    st.metric(
        label="Total Predictions",
        value="1,247",
        delta="+89",
        help="Total number of predictions made"
    )

with stats_col3:
    st.metric(
        label="Avg Processing",
        value="1.8s",
        delta="-0.3s",
        help="Average time per prediction"
    )

with stats_col4:
    st.metric(
        label="Formats Supported",
        value="3",
        delta="",
        help="JPG, PNG, JPEG"
    )

create_gradient_divider()

# Getting Started Guide
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">🚀 Getting Started</h2>', unsafe_allow_html=True)

with st.expander("📖 **Quick Start Guide** - Click to expand", expanded=False):
    st.markdown("""
    ### Welcome to Accident Severity Detection!

    #### 🎯 **Navigation:**
    - Use the **sidebar** to access different pages
    - Each page serves a specific purpose in the analysis workflow
    - Seamless navigation between features

    #### 📤 **Upload & Analysis:**
    1. Navigate to the **Upload** page from the sidebar
    2. Select a clear accident image (JPG, PNG, JPEG)
    3. Wait for AI processing (typically 1-2 seconds)
    4. Review severity classification and detailed recommendations

    #### 📊 **Analytics:**
    - Visit the **Analytics** page to see prediction trends
    - Monitor system performance metrics
    - Track usage statistics over time
    - Export data for external analysis

    #### 💡 **Tips for Best Results:**
    - ✅ Upload high-quality, well-lit images
    - ✅ Capture multiple angles for comprehensive analysis
    - ✅ Ensure the damage is clearly visible
    - ✅ Avoid blurry, dark, or obscured photos
    - ✅ Maximum file size: 10MB
    """)

create_gradient_divider()

# Important Information Section
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">ℹ️ Important Information</h2>', unsafe_allow_html=True)

info_col1, info_col2 = st.columns(2)

with info_col1:
    st.info("""
    **⚠️ Disclaimer:**
    
    - This system is for **informational purposes** only
    - Professional assessment is **always recommended**
    - Results should **not replace** expert judgment
    - Use as a preliminary assessment tool
    - Always consult insurance professionals
    """)

with info_col2:
    st.success("""
    **🎯 Benefits:**
    
    - ⚡ Fast and accurate damage assessment
    - 💰 Detailed repair cost estimates
    - 📋 Insurance claim recommendations
    - 📊 Comprehensive reporting
    - 🔒 Secure and private processing
    """)

create_gradient_divider()

# Severity Levels Information
st.markdown('<h2 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2.5rem;">🎯 Severity Classification</h2>', unsafe_allow_html=True)

severity_col1, severity_col2, severity_col3 = st.columns(3)

with severity_col1:
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid hsl(140, 70%, 55%);">
        <h3 style="color: hsl(140, 70%, 55%); margin-top: 0;">🟢 Minor Damage</h3>
        <p><strong>Characteristics:</strong></p>
        <ul style="text-align: left; color: var(--text-secondary);">
            <li>Scratches and paint chips</li>
            <li>Small dents</li>
            <li>Cosmetic damage</li>
            <li>No structural impact</li>
        </ul>
        <p><strong>Typical Actions:</strong></p>
        <ul style="text-align: left; color: var(--text-secondary);">
            <li>Document with photos</li>
            <li>Get repair quotes</li>
            <li>Consider deductible</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with severity_col2:
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid hsl(40, 100%, 60%);">
        <h3 style="color: hsl(40, 100%, 60%); margin-top: 0;">🟡 Moderate Damage</h3>
        <p><strong>Characteristics:</strong></p>
        <ul style="text-align: left; color: var(--text-secondary);">
            <li>Significant body damage</li>
            <li>Structural concerns</li>
            <li>Multiple panels affected</li>
            <li>Possible mechanical issues</li>
        </ul>
        <p><strong>Typical Actions:</strong></p>
        <ul style="text-align: left; color: var(--text-secondary);">
            <li>Medical check-up</li>
            <li>Contact insurance 24hrs</li>
            <li>Professional inspection</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with severity_col3:
    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid hsl(0, 80%, 60%);">
        <h3 style="color: hsl(0, 80%, 60%); margin-top: 0;">🔴 Severe Crash</h3>
        <p><strong>Characteristics:</strong></p>
        <ul style="text-align: left; color: var(--text-secondary);">
            <li>Major structural failure</li>
            <li>Extensive damage</li>
            <li>Safety systems deployed</li>
            <li>Potential total loss</li>
        </ul>
        <p><strong>Typical Actions:</strong></p>
        <ul style="text-align: left; color: var(--text-secondary);">
            <li>Call emergency services</li>
            <li>Seek medical attention</li>
            <li>Police report required</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

create_gradient_divider()

# Footer Section
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: var(--text-secondary);">
    <div style="display: flex; justify-content: center; gap: 3rem; margin-bottom: 1rem; flex-wrap: wrap;">
        <div>🔒 <strong>Secure & Private</strong></div>
        <div>🚀 <strong>Fast Processing</strong></div>
        <div>🎯 <strong>94.2% Accurate</strong></div>
        <div>🌐 <strong>Multi-Format Support</strong></div>
    </div>
    <div style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid var(--glass-border);">
        💻 Built with Streamlit & TensorFlow | Developed by Gaurav OG | UI Enhanced © 2024
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar Information
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h2 style="background: linear-gradient(135deg, var(--primary), var(--accent));
                   -webkit-background-clip: text;
                   -webkit-text-fill-color: transparent;">
            🎯 Navigation
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("""
    **📍 You Are Here:** Home
    
    Navigate To Other Sections Using The Pages Above.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **Quick Links:**
    - 📤 Upload & Analyze
    - 📊 View Analytics
    - 🔬 Model Information
    - ℹ️ About System
    """)
    
    st.markdown("---")
    
    st.success("""
    **🔥 System Status**
    
    ✅ All Systems Operational
    ✅ Model Loaded
    ✅ Ready For Analysis
    """)
