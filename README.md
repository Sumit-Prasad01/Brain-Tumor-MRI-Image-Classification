# Brain-Tumor-MRI-Image-Classification
## Folder Structure -
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