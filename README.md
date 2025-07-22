# Brain-Tumor-MRI-Image-Classification
## Folder Structure -
``` 
brain-tumor-classification/
│
├── 📄 README.md
├── 📄 requirements.txt
│
├── 📁 data/
│   └── raw/                    # Download dataset here
│       ├── glioma/
│       ├── meningioma/
│       ├── notumor/
│       └── pituitary/
│
├── 📁 notebooks/
│   ├── 1_data_exploration.ipynb
│   ├── 2_data_preprocessing.ipynb
│   ├── 3_custom_cnn.ipynb
│   ├── 4_transfer_learning.ipynb
│   └── 5_model_comparison.ipynb
│
├── 📁 models/
│   ├── custom_cnn_model.h5
│   ├── resnet50_model.h5
│   ├── mobilenet_model.h5
│   └── best_model.h5
│
├── 📁 app/
│   ├── streamlit_app.py        # Main web application
│   └── utils.py               # Helper functions for app
│
└── 📁 results/
    ├── confusion_matrices.png
    ├── training_plots.png
    └── model_comparison.csv
```