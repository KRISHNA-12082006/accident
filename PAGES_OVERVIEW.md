# Pages Overview

This document provides an overview of all pages in the Accident Severity Detection System Streamlit application.

## Main Application (`app.py`)

**Purpose:** Main entry point for image upload and accident severity prediction

**Features:**
- Image upload interface (JPG, PNG, JPEG formats, max 10MB)
- Real-time image validation and metadata display
- AI-powered severity classification (Minor/Moderate/Severe)
- Confidence scoring and detailed analysis
- Repair time and cost estimates
- Insurance recommendations
- Priority-based recommendations

**Key Sections:**
- Sidebar: Quick stats and application info
- Main area: Image upload and analysis results
- Results display: Severity classification with color coding
- Recommendations: Action steps based on severity level
- Detailed analysis: Severity metrics and confidence levels

---

## About Page (`pages/about.py`)

**Purpose:** Comprehensive information about the system, technology, and team

**Features:**
- System description and key purposes
- Technical workflow visualization
- Technology stack details (Frontend, Backend, AI/ML, Infrastructure)
- Use cases and key features
- Performance benchmarks
- Security and privacy information
- Development team credits
- Contact information and support details
- Future roadmap

**Key Sections:**
- How It Works: Process flow and technical architecture
- Technology Stack: Detailed tech specifications
- Use Cases: Insurance, repair shops, authorities, individuals
- Performance Benchmarks: Accuracy, speed, and uptime metrics
- Roadmap: Q4 2024, Q1 2025, and long-term vision

---

## Model Information Page (`pages/model_info.py`)

**Purpose:** Technical specifications and performance metrics of the AI model

**Features:**
- **Fallback Mode Detection:** Displays warning if using dummy model instead of real TensorFlow model
- Model overview (name, architecture, framework, version)
- Architecture details (input shape, classes, parameters)
- Performance metrics (accuracy, precision, recall, F1-score)
- Training data information
- Classification class descriptions
- Model capabilities and limitations
- Technical implementation details
- Export functionality (JSON and CSV formats)

**Key Sections:**
- Fallback Warning: Shown when real model is not found
- Model Overview: Basic model information
- Architecture: Technical specifications
- Performance: Training and evaluation metrics
- Classes: Detailed severity level descriptions
- Export Options: Download model stats and prediction history

---

## Prediction History Page (`pages/prediction_history.py`)

**Purpose:** Dashboard showing analytics and history of all predictions made

**Features:**
- Key metrics display (total predictions, average confidence, dominant severity)
- Severity distribution visualization (pie chart)
- Timeline analysis (predictions over time)
- Recent predictions table with details
- Performance trends
- System health indicators
- Detailed statistics

**Key Sections:**
- Metrics: Total predictions, confidence, severity breakdown
- Visualizations: Charts showing distribution and trends
- Recent Predictions: Tabular view of latest analyses
- Performance Trends: Historical analysis patterns
- System Health: Operational metrics

---

## Analytics Page (`pages/analytics.py`)

**Purpose:** Placeholder page indicating rename to Prediction History

**Note:** This page now shows a simple message directing users to the "Prediction History" page, as the analytics functionality has been consolidated there.

---

## Model Fallback System

### Fallback Model (`fallback/model.py`)

**Purpose:** Provides dummy model when real TensorFlow model is not available

**Features:**
- `DummyModel` class that mimics TensorFlow model interface
- `get_dummy_model()` function for easy instantiation
- Random prediction generation for demonstration
- Same interface as real model for seamless fallback

### Fallback Analysis (`fallback/analysis.py`)

**Purpose:** Dummy analytics for fallback mode

**Functions:**
- `get_fallback_statistics()`: Returns fallback mode statistics
- `get_fallback_insights()`: Provides insights about fallback mode

### Fallback Export (`fallback/export.py`)

**Purpose:** Export functionality for fallback mode

**Functions:**
- `export_fallback_data(format)`: Export data in JSON or CSV format
- `create_fallback_report()`: Generate fallback status report

---

## Core Modules

### Model Module (`model.py`)

**Purpose:** Core ML model loading and prediction logic

**Key Functions:**
- `model_exists()`: Check if TensorFlow model file exists
- `load_model()`: Load real model or fallback to dummy
- `predict_severity(image)`: Get severity classification and confidence
- `get_class_probabilities(image)`: Get probability distribution
- `get_detailed_analysis(severity)`: Get detailed severity information
- `get_prediction_history(limit)`: Retrieve recent predictions
- `get_statistics()`: Calculate overall prediction statistics
- `model_info()`: Return model metadata
- `get_recommendations(severity)`: Get severity-specific recommendations

**Fallback Behavior:**
- Automatically checks for model file presence
- Falls back to dummy model if file not found or loading fails
- Continues to function with random predictions for demonstration

### Utils Module (`utils.py`)

**Purpose:** Image processing and validation utilities

**Key Functions:**
- `preprocess_image(image)`: Prepare image for model input
- `validate_image(image)`: Check image validity and constraints
- `get_image_metadata(image)`: Extract image properties
- `enhance_image(image)`: Apply image enhancements
- `create_thumbnail(image)`: Generate thumbnail version
- `calculate_image_stats(image)`: Compute image statistics

---

## Navigation Structure

The application uses Streamlit's multi-page structure:

1. **🏠 Home** (`app.py`) - Main prediction interface
2. **📋 About** (`pages/about.py`) - System information
3. **🔬 Model Information** (`pages/model_info.py`) - Technical details
4. **📊 Prediction History** (`pages/prediction_history.py`) - Analytics dashboard
5. **📊 Analytics** (`pages/analytics.py`) - Redirect to Prediction History

---

## Email Feature Removal

The email integration feature has been **completely removed** from the application:
- Removed from `pages/about.py` features list
- Removed from Q4 2024 roadmap
- Removed "Email Results" button from `app.py`
- No email-related code remains in the application

---

## Data Flow

1. **User uploads image** → `app.py`
2. **Image validation** → `utils.validate_image()`
3. **Image preprocessing** → `utils.preprocess_image()`
4. **Model loading** → `model.load_model()` (with fallback)
5. **Prediction** → `model.predict_severity()`
6. **Results display** → `app.py` with severity-based formatting
7. **History tracking** → `model.PREDICTION_HISTORY` global list
8. **Analytics** → `pages/prediction_history.py` displays aggregated data

---

## Key Design Patterns

1. **Fallback Pattern:** Graceful degradation when real model unavailable
2. **Global State:** Prediction history stored in module-level variable
3. **Lazy Loading:** Model loaded on first prediction, not on import
4. **Separation of Concerns:** Utils, model logic, and UI separated
5. **Progressive Enhancement:** Works with dummy model, better with real model

---

**Last Updated:** 2024-11-22
**Application Version:** 1.0.0
**Model Version:** v1.0.0
