"""Fallback stub model for when a trained model file is missing.
Provides a simple `predict` method that returns dummy class probabilities.
"""
import random
import numpy as np
from datetime import datetime

# Reuse severity classes from main model for consistency
SEVERITY_CLASSES = ["🟢 Minor Damage", "🟡 Moderate Damage", "🔴 Severe Crash"]

class DummyModel:
    def __init__(self):
        # Any initialization logic can go here
        self.loaded_at = datetime.now()

    def predict(self, image_array):
        """Return dummy probability distribution for three classes.
        The output mimics TensorFlow's `model.predict` shape: (1, 3).
        """
        # Generate a random Dirichlet distribution to simulate probabilities
        probs = np.random.dirichlet(np.ones(3), size=1)
        return probs

def get_dummy_model():
    """Factory function returning a DummyModel instance.
    This mirrors the real `load_model` signature.
    """
    return DummyModel()
