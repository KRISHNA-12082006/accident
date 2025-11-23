"""
Analytics Page (Redirect to Prediction History)
"""

import streamlit as st
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from styles import inject_custom_css

# Inject styling
inject_custom_css()

st.markdown("""
<div class="glass-card" style="text-align: center; padding: 3rem 2rem;">
    <h1 style="font-size: 3rem; margin-bottom: 1rem;">📊</h1>
    <h2 class="gradient-text">Analytics Moved!</h2>
    <p style="color: var(--text-secondary); font-size: 1.1rem; margin: 2rem 0;">
        The Analytics page has been renamed to <strong>Prediction History</strong> for better clarity.<br>
        Please use the <strong>Prediction History</strong> page from the sidebar to access all analytics features.
    </p>
    <div style="margin-top: 2rem;">
        <p style="color: var(--text-secondary);">
            ℹ️ <strong>Note:</strong> The prediction history page includes:
        </p>
        <ul style="list-style: none; padding: 0; margin-top: 1rem; color: var(--text-secondary);">
            <li>📈 Performance metrics and KPIs</li>
            <li>📊 Interactive charts and visualizations</li>
            <li>📋 Recent predictions history</li>
            <li>💾 Data export capabilities</li>
        </ul>
    </div>
</div>
""", unsafe_allow_html=True)
