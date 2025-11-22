# Models Directory

This directory is where the trained TensorFlow/Keras model files should be placed.

## Required Model File

Place your trained accident severity classification model here:

```
models/
├── accident_severity_model.h5  # <- Your trained model file goes here
└── README.md                   # <- This file
```

## Model Specifications

The application expects a TensorFlow/Keras model with the following specifications:

- **File Format**: `.h5` (HDF5 format)
- **Input Shape**: `(224, 224, 3)` - RGB images of 224x224 pixels
- **Output Shape**: `(3,)` - 3 classes representing severity levels
- **Classes**: `['Minor Damage', 'Moderate Damage', 'Severe Crash']`

## Model Training Notes

The model should be trained on accident images with:
- **Classes 0**: Minor Damage (scratches, dents, cosmetic damage)
- **Classes 1**: Moderate Damage (structural damage, airbag deployment)
- **Classes 2**: Severe Crash (major structural failure, potential total loss)

## Automatic Fallback

If no model file is found, the application will automatically fall back to dummy predictions for demonstration purposes. This allows the application to run and demonstrate its functionality even without a trained model.

## How to Setup Your Model

1. Train your TensorFlow/Keras model on accident image data
2. Save the model using `model.save('models/accident_severity_model.h5')`
3. Ensure the model architecture matches the expected input/output specifications
4. The application will automatically load the model on startup

## Troubleshooting

- **Model Loading Errors**: Check that TensorFlow/Keras is installed and compatible versions
- **Shape Mismatches**: Verify input shape is (224, 224, 3) and output is 3 classes
- **File Not Found**: Ensure the filename matches exactly: `accident_severity_model.h5`

The application will provide clear error messages if model loading fails and will fall back to dummy predictions.
