import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the best fine-tuned model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("../models/ResNet50_(Transfer_Learning)_fine_tuned_model.keras")
    return model

model = load_model()

# Define class names (based on your training order)
class_names = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# Set image size
IMAGE_SIZE = (224, 224)

st.title("Brain Tumor MRI Image Classification")
st.markdown("Upload an MRI image to predict the tumor class using a fine-tuned transfer learning model.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_container_width=True)

    # Preprocess the image
    image_resized = image.resize(IMAGE_SIZE)
    img_array = tf.keras.preprocessing.image.img_to_array(image_resized)
    img_array = tf.expand_dims(img_array, 0)  # Add batch dimension

    # Predict
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)

    st.markdown(f"### Prediction: `{predicted_class}`")
    st.markdown(f"### Confidence: `{confidence}%`")

    # Optional: Show probability bar chart
    st.subheader("Class Probabilities")
    fig, ax = plt.subplots()
    bars = ax.bar(class_names, predictions[0], color='skyblue')
    ax.set_ylabel("Probability")
    ax.set_ylim([0, 1])
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + 0.1, yval + 0.01, f'{yval:.2f}')
    st.pyplot(fig)
