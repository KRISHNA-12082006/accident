"""
Fallback Analysis Module
Provides dummy analytics when using the fallback model
"""

def get_fallback_statistics():
    """Return dummy statistics for fallback model."""
    return {
        "fallback_mode": True,
        "model_type": "Dummy Model",
        "total_predictions": 0,
        "accuracy_note": "Using fallback random predictions",
        "message": "Real model not found - using dummy mode"
    }

def get_fallback_insights():
    """Return dummy insights for fallback model."""
    return {
        "insights": [
            "Real TensorFlow model not available",
            "Predictions are randomly generated",
            "Place model file in models/ directory",
            "Model file name: accident_severity_model.h5"
        ],
        "recommendations": [
            "Train and save your TensorFlow model",
            "Ensure model file exists in models directory",
            "Check model file permissions",
            "Verify TensorFlow installation"
        ]
    }
