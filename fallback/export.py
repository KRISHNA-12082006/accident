"""
Fallback Export Module
Provides dummy export functionality when using the fallback model
"""

import json
from datetime import datetime

def export_fallback_data(format="json"):
    """Export fallback model information in specified format."""
    data = {
        "export_timestamp": datetime.now().isoformat(),
        "model_status": "Fallback Mode",
        "model_type": "Dummy Random Model",
        "note": "Real TensorFlow model not available",
        "instructions": "Place trained model in models/accident_severity_model.h5"
    }
    
    if format.lower() == "json":
        return json.dumps(data, indent=2)
    elif format.lower() == "csv":
        csv_lines = ["key,value"]
        for key, value in data.items():
            csv_lines.append(f'"{key}","{value}"')
        return "\n".join(csv_lines)
    else:
        return str(data)

def create_fallback_report():
    """Create a fallback status report."""
    report = {
        "title": "Fallback Model Status Report",
        "generated_at": datetime.now().strftime("%Y-%m-d %H:%M:%S"),
        "status": "Using Dummy Model",
        "reason": "TensorFlow model file not found",
        "expected_path": "models/accident_severity_model.h5",
        "current_behavior": "Random predictions for demonstration",
        "action_required": "Train and deploy real model for production use"
    }
    return report
