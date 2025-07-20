# Brain-Tumor-MRI-Image-Classification
``` 
brain-tumor-mri-classification/
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/                    # Original dataset
│   │   ├── glioma/
│   │   ├── meningioma/
│   │   ├── notumor/
│   │   └── pituitary/
│   └── processed/              # Preprocessed images (optional)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_custom_cnn_training.ipynb
│   ├── 04_transfer_learning.ipynb
│   └── 05_model_comparison.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── model_builder.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
│
├── models/
│   ├── custom_cnn.h5
│   ├── resnet50_transfer.h5
│   ├── mobilenetv2_transfer.h5
│   └── best_model.h5
│
├── results/
│   ├── training_history/
│   │   ├── custom_cnn_history.png
│   │   └── transfer_learning_history.png
│   ├── confusion_matrices/
│   │   ├── custom_cnn_cm.png
│   │   └── transfer_learning_cm.png
│   └── model_comparison.csv
│
├── streamlit_app/
│   ├── app.py                  # Main Streamlit application
│   ├── model_utils.py          # Model loading and prediction functions
│   └── assets/                 # Images, CSS, etc. for the app
│       └── sample_images/
│
└── docs/
    ├── project_report.md
    └── model_architecture.md
```