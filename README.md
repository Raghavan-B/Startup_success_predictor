# Startup Success Predictor

## Project Description

This project involves building a web application using Flask that predicts whether a startup will be acquired or closed based on various features. The prediction model is based on a dataset downloaded from Kaggle, and extensive data preprocessing, exploratory data analysis (EDA), and feature selection techniques were employed to build an accurate prediction model.


## Introduction

The Startup Success Predictor app uses a machine learning model to predict whether a startup will be acquired or closed based on various input features. The project includes data preprocessing, feature selection, model training, and the development of a Flask web application to provide a user-friendly interface for predictions.

## Dataset

The dataset used in this project was downloaded from [Kaggle](https://www.kaggle.com/datasets/manishkc06/startup-success-prediction). It contains information about various startups, including both numerical and categorical features.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Raghavan-B/Startup_success_predictor.git
   cd Startup_success_predictor
   ```

2. Create a virtual environment and activate it:
   ```bash
   conda create -p venv
   conda activate venv  
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your virtual environment is activated.

2. Run the Flask app:
   ```bash
   python run application.py
   ```

3. Open your web browser and go to `http://localhost:5000` to interact with the app.

## Model Training and Evaluation

The model training process involved the following steps:

1. **Data Preprocessing:** Cleaned the data and handled missing values.
2. **Exploratory Data Analysis (EDA):** Analyzed the data to understand patterns and relationships.
3. **Feature Selection:** Used correlation for numerical variables and Chi-square tests for categorical features to select the most relevant features. Checked for multicollinearity using Variance Inflation Factor (VIF).
4. **Feature Scaling:** Applied standard scaling to numerical features.
5. **Encoding:** Used label encoding for categorical features.
6. **Model Training:** Evaluated various classification models and selected the Gradient Boost model as the best-performing model.
7. **Model Tuning:** Fine-tuned the model using RandomizedSearchCV for optimal hyperparameters.
8. **Model Saving:** Saved the trained model for use in the Flask app.

## Feature Selection

After feature selection, the dataset was reduced from 31 features to 10 features plus the target feature. This was achieved using:

- Correlation analysis for numerical features.
- Chi-square tests for categorical features.
- Multicollinearity check using VIF.

## Flask App

The Flask web application provides a user-friendly interface to interact with the prediction model. Users can input the relevant features of their startup, and the app will predict whether the startup is likely to be acquired or closed.

---
