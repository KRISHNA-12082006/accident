"""
Upload Page - Accident Image Analysis with Modern UI
Streamlit page for uploading and analyzing accident images
"""

import streamlit as st
from PIL import Image
import numpy as np
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model import predict_severity, get_detailed_analysis, get_recommendations
from utils import preprocess_image, validate_image, get_image_metadata
from styles import inject_custom_css, create_hero_section, create_gradient_divider

# Page Configuration
st.set_page_config(
    page_title="Upload & Analysis",
    page_icon="📤",
    layout="wide"
)

# Inject Custom Styling
inject_custom_css()

# Hero Section
create_hero_section(
    "📤 Upload & Analysis",
    "Upload accident images for instant AI-powered severity classification"
)

# File Uploader Section
st.markdown("""
<div style="max-width: 900px; margin: 0 auto;">
    <div style="text-align: center; margin-bottom: 2rem;">
        <p style="font-size: 1.1rem; color: var(--text-secondary);">
            Drop your accident image below or click to browse. Supported formats: JPG, PNG, JPEG (max 10MB)
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose an accident image",
    type=["jpg", "jpeg", "png"],
    help="Upload a clear image of the accident scene",
    label_visibility="collapsed"
)

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    
    # Validate image
    is_valid, message = validate_image(image)
    
    if not is_valid:
        st.error(f"❌ **Image Validation Failed:** {message}")
    else:
        # Display uploaded image and results
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("""
            <h3 style="margin-bottom: 1rem;">
                📷 <span class="gradient-text">Uploaded Image</span>
            </h3>
            """, unsafe_allow_html=True)
            
            # Display image with glass card effect
            st.markdown('<div class="glass-card" style="padding: 1rem;">', unsafe_allow_html=True)
            st.image(image, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Show image metadata in expander
            with st.expander("📊 **Image Details & Metadata**"):
                metadata = get_image_metadata(image)
                
                meta_col1, meta_col2 = st.columns(2)
                with meta_col1:
                    st.markdown(f"**📐 Dimensions:** `{metadata['width']} x {metadata['height']} px`")
                    st.markdown(f"**🖼️ Format:** `{metadata['format']}`")
                    st.markdown(f"**🎨 Mode:** `{metadata['mode']}`")
                with meta_col2:
                    st.markdown(f"**📏 Aspect Ratio:** `{metadata['aspect_ratio']}`")
                    st.markdown(f"**📊 Megapixels:** `{metadata['megapixels']} MP`")
                    st.markdown(f"**📦 File:** `{uploaded_file.name}`")
        
        with col2:
            st.markdown("""
            <h3 style="margin-bottom: 1rem;">
                🔍 <span class="gradient-text">Analysis Results</span>
            </h3>
            """, unsafe_allow_html=True)
            
            # Processing indicator with custom styling
            with st.spinner("🔄 Analyzing image with AI..."):
                # Preprocess image
                processed_img = preprocess_image(image)
                
                # Get prediction
                severity_class, confidence = predict_severity(processed_img)
                
                # Get detailed analysis
                details = get_detailed_analysis(severity_class)
            
            # Display results in glass card
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            
            # Display severity with color coding
            if "Minor" in severity_class:
                st.success(f"**Severity Classification:** {severity_class}")
                severity_color = "hsl(140, 70%, 55%)"
            elif "Moderate" in severity_class:
                st.warning(f"**Severity Classification:** {severity_class}")
                severity_color = "hsl(40, 100%, 60%)"
            else:
                st.error(f"**Severity Classification:** {severity_class}")
                severity_color = "hsl(0, 80%, 60%)"
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Confidence score with glowing progress bar
            st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
            st.metric(
                label="🎯 Confidence Score",
                value=f"{confidence:.1f}%",
                delta=f"{confidence - 80:.1f}% above threshold" if confidence >= 80 else f"{confidence - 80:.1f}%"
            )
            st.progress(confidence / 100)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Detailed metrics
            st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
            metric_col1, metric_col2 = st.columns(2)
            with metric_col1:
                st.metric("⏱️ Repair Time", details['repair_time'])
            with metric_col2:
                st.metric("💰 Cost Estimate", details['cost_range'])
            
            st.metric(
                "🏥 Insurance Claim",
                "✅ Recommended" if details['insurance_recommended'] else "⚠️ Optional"
            )
            st.markdown('</div>', unsafe_allow_html=True)
        
        create_gradient_divider()
        
        # Full-width recommendations section
        st.markdown("""
        <h3 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2rem;">
            💡 <span class="gradient-text">Recommended Actions</span>
        </h3>
        """, unsafe_allow_html=True)
        
        # Get recommendations
        recommendations = get_recommendations(severity_class)
        
        # Display based on severity in a glass card
        st.markdown(f'<div class="glass-card" style="border-left: 4px solid {severity_color};">', unsafe_allow_html=True)
        
        if "Severe" in severity_class:
            st.error("⚠️ **CRITICAL DAMAGE DETECTED**")
            st.markdown("**Immediate Actions Required:**")
            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"{i}. {rec}")
            
            st.warning("""
            **⚠️ Critical Notes:**
            - This is a severe accident requiring **immediate attention**
            - Total vehicle loss is **highly possible**
            - Professional assessment is **mandatory**
            - Contact emergency services if not already done
            - Begin insurance claim process **immediately**
            """)
        
        elif "Moderate" in severity_class:
            st.warning("⚠️ **SIGNIFICANT DAMAGE DETECTED**")
            st.markdown("**Recommended Actions:**")
            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"{i}. {rec}")
            
            st.info("""
            **📋 Important Notes:**
            - Professional inspection **highly recommended**
            - Insurance claim process should begin **within 24 hours**
            - Vehicle may need **extended repair time**
            - Consider rental vehicle during repairs
            - Document all damage thoroughly
            """)
        
        else:
            st.success("✅ **MINOR DAMAGE - MANAGEABLE**")
            st.markdown("**Suggested Next Steps:**")
            for i, rec in enumerate(recommendations, 1):
                st.markdown(f"{i}. {rec}")
            
            st.info("""
            **💡 Helpful Tips:**
            - Simple repairs can be handled at **local auto shops**
            - Consider repair cost vs. **insurance deductible**
            - Quick turnaround time expected (1-3 days)
            - Get multiple quotes for best pricing
            - May not need insurance involvement
            """)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        create_gradient_divider()
        
        # Detailed Analysis Section
        st.markdown("""
        <h3 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2rem;">
            📈 <span class="gradient-text">Detailed Analysis Breakdown</span>
        </h3>
        """, unsafe_allow_html=True)
        
        analysis_col1, analysis_col2, analysis_col3 = st.columns(3)
        
        with analysis_col1:
            st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
            st.markdown("### **Severity Level**")
            st.markdown(f"<h2 style='color: {severity_color};'>Level {details['severity_level']}/3</h2>", unsafe_allow_html=True)
            st.progress(details['severity_level'] / 3)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with analysis_col2:
            st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
            st.markdown("### **Confidence Level**")
            if confidence >= 90:
                conf_label = "Very High ⭐"
                conf_color = "hsl(140, 70%, 55%)"
            elif confidence >= 80:
                conf_label = "High ✓"
                conf_color = "hsl(140, 70%, 55%)"
            elif confidence >= 70:
                conf_label = "Moderate ~"
                conf_color = "hsl(40, 100%, 60%)"
            else:
                conf_label = "Low ⚠"
                conf_color = "hsl(0, 80%, 60%)"
            
            st.markdown(f"<h2 style='color: {conf_color};'>{conf_label}</h2>", unsafe_allow_html=True)
            st.progress(confidence / 100)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with analysis_col3:
            st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
            st.markdown("### **Priority**")
            if details['severity_level'] == 3:
                priority_label = "🔴 Critical"
                priority_color = "hsl(0, 80%, 60%)"
            elif details['severity_level'] == 2:
                priority_label = "🟡 High"
                priority_color = "hsl(40, 100%, 60%)"
            else:
                priority_label = "🟢 Normal"
                priority_color = "hsl(140, 70%, 55%)"
            
            st.markdown(f"<h2 style='color: {priority_color};'>{priority_label}</h2>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        create_gradient_divider()
        
        # Export Options
        st.markdown("""
        <h3 style="text-align: center; margin: 2rem 0 1.5rem 0; font-size: 2rem;">
            📋 <span class="gradient-text">Export & Save</span>
        </h3>
        """, unsafe_allow_html=True)
        
        export_col1, export_col2 = st.columns(2)
        
        with export_col1:
            if st.button("📄 Generate PDF Report", use_container_width=True):
                st.info("📄 PDF report generation feature coming soon! This will include full analysis, images, and recommendations.")
        
        with export_col2:
            if st.button("💾 Save to History", use_container_width=True):
                st.info("💾 Analysis will be saved to your prediction history. Feature coming soon!")

else:
    # Instructions when no image uploaded
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 3rem 2rem; margin: 2rem auto; max-width: 800px;">
        <div style="font-size: 4rem; margin-bottom: 1rem;">📤</div>
        <h3 style="margin-bottom: 1rem;">No Image Uploaded Yet</h3>
        <p style="color: var(--text-secondary); font-size: 1.1rem;">
            Click the upload area above or drag and drop an accident image to begin AI analysis
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # How to use section
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        with st.expander("📖 **How to Use This Page**"):
            st.markdown("""
            ### Step-by-Step Guide:
            
            1. **📤 Upload Image**
               - Click the upload button above
               - Select an accident photo from your device
               - Or drag and drop the image
            
            2. **⏳ Wait for Analysis**
               - AI model processes the image (~2 seconds)
               - Advanced deep learning algorithms at work
            
            3. **📊 View Results**
               - Review severity classification
               - Check confidence score
               - Examine detailed metrics
            
            4. **💡 Read Recommendations**
               - Follow suggested next steps
               - Based on damage severity
            
            5. **🎯 Take Action**
               - Contact appropriate services
               - Begin necessary procedures
            """)
    
    with col_info2:
        with st.expander("✨ **Tips for Best Results**"):
            st.markdown("""
            ### Optimize Your Analysis:
            
            ✅ **Image Quality:**
            - Use clear, well-lit images
            - Avoid blurry or dark photos
            - Ensure good focus on damage
            
            ✅ **Capture Angles:**
            - Multiple angles recommended
            - Show full extent of damage
            - Include context when possible
            
            ✅ **File Requirements:**
            - Formats: JPG, PNG, JPEG
            - Maximum size: 10MB
            - Minimum resolution: 224x224px
            
            ✅ **What to Show:**
            - Clear view of damaged areas
            - Structural damage visible
            - Vehicle identification possible
            """)
    
    create_gradient_divider()
    
    # Sample preview
    with st.expander("📊 **Preview: What Results Look Like**"):
        st.markdown("""
        ### After uploading, you'll see:
        
        🎯 **Severity Classification**
        - Minor/Moderate/Severe with color coding
        - Visual indicators for quick understanding
        
        📊 **Confidence Score**
        - AI certainty percentage
        - Interactive progress bar
        - Threshold comparisons
        
        💰 **Cost & Time Estimates**
        - Repair time projections
        - Cost range estimates
        - Insurance recommendations
        
        💡 **Action Steps**
        - Severity-based recommendations
        - Priority indicators
        - Detailed guidance
        
        📈 **Analysis Breakdown**
        - Severity level (1-3)
        - Confidence rating
        - Priority classification
        
        ---
        
        **Powered by our trained AI model with 94.2% accuracy**
        """)
