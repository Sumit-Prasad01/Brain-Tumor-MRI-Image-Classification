# Brain Tumor MRI Image Classification with Transfer Learning

- GitHub Link - https://github.com/Sumit-Prasad01/Brain-Tumor-MRI-Image-Classification

This project uses deep learning to classify brain MRI images into four categories:

- Glioma
- Meningioma
- No Tumor
- Pituitary

We compare a custom-built CNN model with transfer learning models (e.g., ResNet50), using TensorFlow and Keras.

---

## 🧠 Features

- Custom CNN and fine-tuned Transfer Learning models
- Visual performance analysis (ROC, PR, F1 curves)
- Streamlit app for interactive predictions
- Git LFS to handle large model files

---

## 🗂️ Project Structure
``` 
brain-tumor-classification/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📁 data/
│   └── train/                    
│       ├── glioma/
│       ├── meningioma/
│       ├── notumor/
│       └── pituitary/
|   └── test/                    
│       ├── glioma/
│       ├── meningioma/
│       ├── notumor/
│       └── pituitary/
|   └── valid/                    
│       ├── glioma/
│       ├── meningioma/
│       ├── notumor/
│       └── pituitary/
│
├── 📁 notebooks/
│   ├── 1_data_exploration.ipynb
│   ├── 2_data_preprocessing.ipynb
│   ├── 3_Transfer_Learning.ipynb│   
│   └── 4_Model_Comparison.ipynb
│
├── 📁 models/
│   ├── Custom_CNN_Brain_Tumor_MRI.keras   # Custom Cnn model
│   └── best_model.Keras # Transfer Learning Model
│
├── 📁 app/
│   ├── streamlit_app.py        # Main web application
│   └── api.py               # FastApi Application
│
└── 📁 results/
    ├── confusion_matrices.png
    ├── training_plots.png
    └── model_comparison.csv
```

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/Brain-Tumor-MRI-Image-Classification.git
cd Brain-Tumor-MRI-Image-Classification
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

### 3. Download or Train Models

- Place trained models in `models/`
- Use Git LFS for large model tracking

### 4. Run Streamlit App

```bash
cd streamlit_app
streamlit run app.py
```

---

## 📊 Evaluation Summary

| Metric         | Custom CNN | Transfer Learning |
| -------------- | ---------- | ----------------- |
| Accuracy       | 92%        | **93.9%**         |
| AUC            | ~0.99      | ~0.5–0.6          |
| Precision (AP) | High       | Low               |
| F1 Score       | Strong     | Weak for Glioma   |

✅ Despite slightly lower accuracy, **Custom CNN** generalizes better class-wise. Use **Transfer Learning** if you only care about raw accuracy.

---

## 📌 Requirements

- Python 3.8+
- TensorFlow 2.x
- Streamlit
- Matplotlib, Seaborn, Scikit-learn

Install with:

```bash
pip install -r requirements.txt
```

---

## 📥 Sample Prediction

Upload an image and get:

- Predicted class
- Confidence score
- Bar chart of probabilities

---

