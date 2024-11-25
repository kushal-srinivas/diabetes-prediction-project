# -*- coding: utf-8 -*-
"""data_preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xXXuCg9huzoLTa1pW8LYS-rVioJfJTQb
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data("diabetes.csv"):
    """
    Load and preprocess the Diabetes dataset.
    :param file_path: Path to the CSV file containing the dataset.
    :return: Preprocessed training and testing data.
    """
    # Load the dataset
    data = pd.read_csv(file_path)

    # Split features and target
    X = data.iloc[:, :-1].values  # All columns except the last one
    y = data.iloc[:, -1].values   # The last column as target

    # Standardize the feature data
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

if _name_ == "_main_":
    # Example usage
    file_path = "diabetes.csv"  # Update with actual path to the dataset
    X_train, X_test, y_train, y_test = load_and_preprocess_data(file_path)
    print("Data preprocessing complete. Training and testing sets are ready.")