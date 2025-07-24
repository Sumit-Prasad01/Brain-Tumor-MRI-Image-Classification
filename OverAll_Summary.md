# Brain Tumor MRI Image Classification – Overall Summary
### Brain tumor classification using MRI images is a critical application of deep learning in medical imaging. Tumors in the brain, such as glioma, meningioma, and pituitary tumors, can have vastly different prognoses and treatment strategies. Hence, accurately classifying these types through non-invasive methods like MRI scans is of great clinical importance. Manual diagnosis by radiologists can be time-consuming and prone to inter-observer variability. Deep learning offers a promising solution to automate and improve the accuracy and speed of tumor classification.

### In this project, we address the challenge of classifying brain MRI images into four categories: glioma, meningioma, no tumor, and pituitary tumor. Two distinct modeling strategies were employed: a Custom Convolutional Neural Network (CNN) and a Transfer Learning approach using ResNet50. The goal was not only to achieve high accuracy but also to understand which approach generalizes better across class distributions and clinical conditions.

## Dataset and Preprocessing
### The dataset comprises T1-weighted contrast-enhanced MRI scans, organized into training, validation, and testing sets. Preprocessing steps included resizing images to a uniform dimension, normalization, and batch loading using TensorFlow’s image_dataset_from_directory() method. Data augmentation techniques such as horizontal flipping, rotation, and zooming were applied during training to improve generalization.

### Model Architectures
- 1. Custom CNN:
A handcrafted CNN was designed with multiple convolutional, max pooling, and dropout layers followed by dense layers. The architecture was tuned to extract meaningful spatial features specific to brain tumor patterns. It was trained from scratch, allowing it to learn highly dataset-specific features.

- 2. Transfer Learning (ResNet50):
ResNet50, a pre-trained model on ImageNet, was fine-tuned by replacing the top layers and training only the final few layers. This approach leverages generic image features learned from large-scale natural image datasets and adapts them to the medical imaging domain.

## Evaluation Metrics and Results
### Both models were evaluated on the test set using key performance metrics including accuracy, AUC (Area Under the ROC Curve), precision-recall curves, and F1 score vs threshold curves.

### Custom CNN achieved an overall accuracy of ~92% with near-perfect AUC (~0.99) and high average precision scores across all four classes.

### Transfer Learning achieved a higher accuracy of 93.9%, but suffered from lower AUCs (~0.5–0.6) and significantly poorer precision-recall values, particularly for glioma and no tumor classes.

## Analysis
### Although the transfer learning model had a slightly higher accuracy, deeper analysis revealed it struggled with class imbalance and failed to provide reliable probabilistic outputs. Its ROC curves were close to random guessing lines, and precision dropped significantly at higher recall values.

### In contrast, the custom CNN demonstrated robust and balanced performance across all evaluation metrics. Its ROC and PR curves confirmed its ability to discriminate between classes and maintain precision under varying thresholds.

### This reinforces the idea that transfer learning may not always outperform task-specific custom models, especially when domain-specific features differ significantly from the pre-training dataset (e.g., ImageNet).

## Conclusion
### This project highlights that in medical imaging tasks like brain tumor classification, performance should be evaluated beyond overall accuracy. Although transfer learning offers a fast starting point, custom CNNs tailored to the dataset can yield more interpretable and balanced performance. Ultimately, the custom CNN emerged as the better choice for this task due to its strong class-wise performance and generalization ability.

## Additionally, a Streamlit app was developed to demonstrate the prediction capability in real-time, allowing users to upload MRI images and receive classification outputs along with confidence scores and visualizations.

## This work paves the way for deploying AI-assisted diagnostic tools in clinical settings, enhancing early tumor detection and supporting medical professionals in decision-making.