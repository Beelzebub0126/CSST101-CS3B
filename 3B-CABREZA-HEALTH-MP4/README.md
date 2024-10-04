# Bayesian Network for Healthcare Diagnosis

This project implements a **Bayesian Network** for diagnosing heart disease based on various health factors. The goal is to model relationships between risk factors and symptoms and use probabilistic reasoning to predict the likelihood of heart disease, chest pain, and abnormal ECG results.

## Project Overview

The **Bayesian Network** is built using the `pgmpy` library. The network includes the following variables:
- **Age**: (Young, Middle-aged, Old)
- **Smoking**: (Yes, No)
- **Exercise**: (Regular, None)
- **Cholesterol**: (High, Normal)
- **Blood Pressure**: (High, Normal)
- **Heart Disease**: (Yes, No)
- **Chest Pain**: (Yes, No)
- **ECG Result**: (Abnormal, Normal)

These variables model risk factors and symptoms for diagnosing heart disease. Based on known risk factors, the Bayesian Network calculates the probability of a person having heart disease, chest pain, or an abnormal ECG result.

### Project Components

The project is organized into several steps:
1. **Define the Network Structure**: A Bayesian Network is created to model the relationships between health factors such as age, smoking, exercise, cholesterol, and blood pressure.
2. **Define Conditional Probability Tables (CPTs)**: Hypothetical CPTs are defined for each variable using `pgmpy`'s `TabularCPD` to represent the dependencies between variables.
3. **Perform Inference**: The `VariableElimination` algorithm is used to calculate the probability of heart disease and other symptoms based on specific health factors.
4. **Simulate Data**: A synthetic healthcare dataset is generated with 1000 patients to simulate realistic data for parameter learning.
5. **Learn Parameters from Data**: Maximum Likelihood Estimation is applied to the synthetic dataset to estimate the CPTs for heart disease and related symptoms.
6. **Visualize the Network**: The network is visualized using `networkx` and `matplotlib`, displaying nodes and edges that represent the relationships between the variables.
7. **Sensitivity Analysis**: Sensitivity analysis is conducted to study the effect of smoking on the probability of heart disease.

### Detailed Description of the Code
Step 1: Define the Network Structure: The Bayesian Network structure models how different health factors affect the likelihood of heart disease. It includes dependencies like Age, Smoking, Exercise, Cholesterol, and BloodPressure influencing HeartDisease.

Step 2: Define Conditional Probability Tables (CPTs): CPTs for each variable in the Bayesian Network are defined based on hypothetical probability values. These tables express the likelihood of each variable's state given the states of its parents in the network.

Step 3: Perform Inference: Queries are run to determine the probability of heart disease and abnormal ECG results based on certain conditions, such as a patient being middle-aged, a smoker, having high cholesterol, and high blood pressure.

Step 4: Simulate Data: A dataset of 1000 synthetic patients is generated, simulating real-world data that includes attributes like age, smoking habits, exercise, and cholesterol levels. This dataset is used to train the Bayesian Network.

Step 5: Learn Parameters from Data: The synthetic dataset is used to estimate the CPTs for heart disease and related symptoms using Maximum Likelihood Estimation (MLE). This process adjusts the probabilities based on the generated data.

Step 6: Visualize the Network: The structure of the Bayesian Network is visualized using networkx. Nodes represent the variables, and edges represent the dependencies between them.

Step 7: Sensitivity Analysis: A sensitivity analysis is performed to analyze the effect of smoking on heart disease. The analysis compares the probabilities of heart disease for smokers and non-smokers.

Results
Heart Disease Inference: The Bayesian Network provides accurate probabilities for heart disease based on input health factors. It can predict the likelihood of heart disease for different combinations of risk factors such as age, smoking, and cholesterol.

Sensitivity Analysis: The model demonstrates that smokers have a significantly higher probability of heart disease compared to non-smokers, highlighting the impact of smoking on cardiovascular health.
