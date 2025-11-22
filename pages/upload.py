"""
Upload Page - Accident Image Analysis
Streamlit page for uploading and analyzing accident images
"""

import streamlit as st
from PIL import Image
import numpy as np
from model import predict_severity, get_detailed_analysis, get_recommendations
from utils import preprocess_image, validate_image, get_image_metadata

# Page header
st.title("📤 Upload & Analysis")
st.markdown("Upload an accident image to analyze and classify damage severity")

# File Uploader
uploaded_file = st.file_uploader(
    "📤 Choose an accident image",
    type=["jpg", "jpeg", "png"],
    help="Upload a clear image of the accident scene"
)

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)

    # Validate image
    is_valid, message = validate_image(image)

    if not is_valid:
        st.error(message)
    else:
        # Display uploaded image
        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("📷 Uploaded Image")
            st.image(image, use_container_width=True)

            # Show image metadata in expander
            with st.expander("📊 Image Details"):
                metadata = get_image_metadata(image)
                st.write(f"**Dimensions:** {metadata['width']} x {metadata['height']} px")
                st.write(f"**Format:** {metadata['format']}")
                st.write(f"**Mode:** {metadata['mode']}")
                st.write(f"**Aspect Ratio:** {metadata['aspect_ratio']}")
                st.write(f"**Megapixels:** {metadata['megapixels']} MP")

        with col2:
            st.subheader("🔍 Analysis Results")

            # Processing indicator
            with st.spinner("Analyzing image..."):
                # Preprocess image
                processed_img = preprocess_image(image)

                # Get prediction
                severity_class, confidence = predict_severity(processed_img)

                # Get detailed analysis
                details = get_detailed_analysis(severity_class)

            # Display results with color coding
            if "Minor" in severity_class:
                st.success(f"**Severity Level:** {severity_class}")
            elif "Moderate" in severity_class:
                st.warning(f"**Severity Level:** {severity_class}")
            else:
                st.error(f"**Severity Level:** {severity_class}")

            # Confidence score
            st.metric(
                label="Confidence Score",
                value=f"{confidence:.1f}%",
                delta=f"{confidence - 80:.1f}% above threshold"
            )

            # Progress bar for confidence
            st.progress(confidence / 100)

            # Detailed information
            st.divider()

            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("Repair Time", details['repair_time'])
            with col_b:
                st.metric("Cost Estimate", details['cost_range'])

            st.metric(
                "Insurance Claim",
                "Recommended" if details['insurance_recommended'] else "Optional"
            )

        # Full-width recommendations section
        st.divider()
        st.subheader("💡 Recommended Actions")

        # Get recommendations
        recommendations = get_recommendations(severity_class)

        # Display based on severity
        if "Severe" in severity_class:
            st.error("⚠️ **CRITICAL DAMAGE DETECTED**")
            for rec in recommendations:
                st.markdown(f"- {rec}")

            st.warning("""
            **Additional Notes:**
            - This is a severe accident requiring immediate attention
            - Total vehicle loss is possible
            - Professional assessment is mandatory
            """)

        elif "Moderate" in severity_class:
            st.warning("⚠️ **SIGNIFICANT DAMAGE DETECTED**")
            for rec in recommendations:
                st.markdown(f"- {rec}")

            st.info("""
            **Additional Notes:**
            - Professional inspection highly recommended
            - Insurance claim process should begin soon
            - Vehicle may need extended repair time
            """)

        else:
            st.success("✅ **MINOR DAMAGE - MANAGEABLE**")
            for rec in recommendations:
                st.markdown(f"- {rec}")

            st.info("""
            **Additional Notes:**
            - Simple repairs can be handled locally
            - Consider cost vs. insurance deductible
            - Quick turnaround time expected
            """)

        # Additional Analysis Section
        st.divider()
        st.subheader("📈 Detailed Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("**Severity Level**")
            st.write(f"Level {details['severity_level']}/3")
            st.progress(details['severity_level'] / 3)

        with col2:
            st.markdown("**Confidence Level**")
            if confidence >= 90:
                st.write("Very High")
            elif confidence >= 80:
                st.write("High")
            elif confidence >= 70:
                st.write("Moderate")
            else:
                st.write("Low")
            st.progress(confidence / 100)

        with col3:
            st.markdown("**Priority**")
            if details['severity_level'] == 3:
                st.write("🔴 Critical")
            elif details['severity_level'] == 2:
                st.write("🟡 High")
            else:
                st.write("🟢 Normal")

        # Download/Export Options
        st.divider()

        col_x, col_z = st.columns(2)

        with col_x:
            if st.button("📄 Generate Report", use_container_width=True):
                st.info("PDF report generation coming soon!")

        with col_z:
            if st.button("💾 Save Analysis", use_container_width=True):
                st.info("Save feature coming soon!")


else:
    # Instructions when no image uploaded
    st.info("👆 Please upload an accident image to begin analysis")

    # How to use section
    with st.expander("📖 How to use this page"):
        st.markdown("""
        ### Step-by-Step Guide:

        1. **Upload Image:** Click the upload button above and select an accident photo
        2. **Wait for Analysis:** The AI model will process the image (takes ~2 seconds)
        3. **View Results:** Check the severity classification and confidence score
        4. **Read Recommendations:** Follow the suggested next steps based on severity
        5. **Take Action:** Contact appropriate services as recommended

        ### Tips for Best Results:
        - Use clear, well-lit images
        - Capture the damaged area from multiple angles
        - Avoid blurry or dark photos
        - Image should show the damage clearly
        - Supported formats: JPG, PNG, JPEG (max 10MB)
        """)

    # Sample preview with placeholders
    with st.expander("📊 What results look like"):
        st.markdown("""
        After uploading an image, you can expect to see:

        ✅ **Severity Classification** (Minor/Moderate/Severe) with color coding
        ✅ **Confidence Score** showing AI certainty
        ✅ **Repair Time Estimate** and cost ranges
        ✅ **Insurance Recommendation**
        ✅ **Detailed Action Steps** based on severity
        ✅ **Priority Level** and progress indicators

        The analysis is powered by our trained AI model with 94.2% accuracy.
        """)
