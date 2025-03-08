import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_shape=(128, 128, 1)):
    """
    Builds a CNN model for brain tumor classification.

    Parameters:
        - input_shape (tuple): Shape of the input images.

    Returns:
        - model (tf.keras.Model): Compiled CNN model.
    """
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),

        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),

        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(1, activation='sigmoid')  # Binary classification (Tumor / No Tumor)
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
