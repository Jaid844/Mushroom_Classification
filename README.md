
# Mushroom Classification
This project focuses on the classification of mushrooms into edible or poisonous categories. It utilizes machine learning algorithms to build a model that can predict the edibility of a given mushroom based on its characteristics.
The deployment link is available in render and the link is 
https://mushrrom2.onrender.com
but the UI design is limited ,works well with postman calls

## Dataset
The dataset used for training and testing the mushroom classification model is sourced from the UCI Machine Learning Repository. It contains various attributes of mushrooms along with their corresponding class labels (edible or poisonous). The dataset is preprocessed and cleaned to ensure the quality of the data.
## Features
The features or attributes considered for mushroom classification include:

Cap shape,
Cap surface,
Cap color,
Bruises,
Odor,
Gill attachment,
Gill spacing,
Gill size,
Gill color,
Stalk shape,
Stalk surface above ring,
Stalk surface below ring,
Stalk color above ring,
Stalk color below ring,
Veil type,
Veil color,
Ring number,
Ring type,
Spore print color,
Population,
Habitat.
## Model Training
The mushroom classification model is trained using a supervised learning approach. The dataset is divided into a training set and a test set. Various machine learning algorithms, such as decision trees, or support vector machines, are implemented and evaluated to find the most accurate model for the given problem.

The training process involves:

Data preprocessing: Cleaning the dataset, handling missing values, and performing feature encoding or scaling if required.
Splitting the dataset: Dividing the dataset into training and test sets for model evaluation.
Model selection: Trying out different machine learning algorithms to identify the most suitable one for the mushroom classification task.
Model training: Training the chosen model using the training dataset.
Model evaluation: Assessing the performance of the trained model using evaluation metrics such as accuracy, precision, recall, or F1 score.
## USAGE
To use the mushroom classification model:

Ensure that the required dependencies (Python, scikit-learn, etc.) are installed.
Load the trained model from a saved model file or retrain the model using the provided code.
Prepare the input data by providing the necessary mushroom attributes.
Use the trained model to predict the edibility of the mushroom.
Analyze the prediction output, which will indicate whether the mushroom is classified as edible or poisonous.
Results
## Architecture![pipeline](https://github.com/Jaid844/InsuranceFraudDetector/assets/112820053/84ef6ccf-ff79-4e74-a124-280f0eaa0f11)
## Technology Used
Python ,Flask,scikit-learn,Gunicorn,Cassandra
## How to Get Started

## Clone the Project

You can also use this project in your system by following thses simple steps -:

```bash
  https://github.com/Jaid844/Mushroom_Classification.git
```

## Install the requirements -
```bash
pip install -r requirements.txt
```

## Run the main.py file
```bash
python main.py
```

## You are done Good to go
## Authors

- [Muhammad Jaid]()


## Deployment
The app is hosted in Render server
![app](https://github.com/Jaid844/InsuranceFraudDetector/assets/112820053/ef888e5a-534e-43f5-b034-c75fd005ffc3)
## Acknowledgements

 -UCI Machine Learning Repository for providing the mushroom    dataset.

-The scikit-learn library for its comprehensive machine learning capabilities.

-The open-source community for sharing knowledge and resources.

## Licence
This project is licensed under the MIT License, permitting open-source contributions and usage.

Feel free to tailor and expand upon this introduction based on the specific details and objectives of your mushroom classification project.
