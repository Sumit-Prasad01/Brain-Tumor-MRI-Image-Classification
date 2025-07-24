import tensorflow as tf
import numpy as np
from PIL import Image
import io

CLASS_NAMES = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

async def load_model_and_predict(file, model_type):
    # Load model
    model_path = f"models/{'custom_cnn_model' if model_type == 'custom' else 'resnet50_transfer_model'}.keras"
    model = tf.keras.models.load_model(model_path)

    # Preprocess image
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    image = image.resize((224, 224))  # adjust to your model's input
    img_array = tf.keras.utils.img_to_array(image) / 255.0
    img_array = tf.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)[0]
    top_class = np.argmax(predictions)
    confidence = float(predictions[top_class])

    return {
        "predicted_class": CLASS_NAMES[top_class],
        "confidence": round(confidence, 3),
        "class_probabilities": dict(zip(CLASS_NAMES, map(float, predictions)))
    }
