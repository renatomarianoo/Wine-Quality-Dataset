# Red Wine Quality Dataset

This project utilizes a dataset containing physiochemical data for the red variants of Portuguese "Vinho Verde" wine, available [here](https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009).

**Project Overview:**
- Dataset excludes grape types, wine brand, and selling price due to privacy and logistic concerns.
- Goal: Create models predicting wine quality and alcohol level based on physiochemical features.

**Key Findings:**
- Wine quality model achieved 82% accuracy but tended to categorize wines mostly as average.
- Challenges predicting Category 1 (Bad) and accuracy of 31% for Category 3 (Good).
- Potential model improvements using other types (e.g., Decision Tree, Random Forest) and considering the entire dataset without outlier removal.
- Data concentration in the middle category limits model expectations.

**Statistical Inference Analysis:**
- High alcohol level identified as an important parameter for a wine to be considered good.

**Alcohol Level Prediction Model:**
- Model predicting alcohol level based on physiochemical features performed well, with 72% of variance explained.

Given the concentrated nature of the data, model improvements may require further exploration of different algorithms and dataset considerations.