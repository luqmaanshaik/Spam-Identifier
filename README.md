Spam Identifier With AI (S.I.W.A.)
Python Badge PyTorch Badge Scikit-Learn Badge License Badge

This project is a spam classifier that uses artificial intelligence to identify spam messages. It is implemented in Python, primarily utilizing the PyTorch and scikit-learn libraries for machine learning and natural language processing tasks.

Requirements
To run this project, you will need the following libraries:

torch
sklearn
csv
pandas
You can install them using !pip install torch scikit-learn pandas. However, all of them are pre-installed in Google Colab.

Dataset
This project uses two open-source datasets from Kaggle, marked as Small (469 KB) and Medium (10 MB).

Spam Email (Small)
Email Spam Dataset (Medium)
Model
The model used for this project is a simple neural network with two linear layers and a sigmoid activation function. The input size of the model depends on the number of features extracted from the text messages using CountVectorizer. The output size of the model is 1, which represents the probability of the message being spam.

Usage
To use this project, you can follow these steps:

Clone this repository to your local machine using git clone https://github.com/LyubomirT/spam-classifier.git.
Open the ML_Spam_Identifier.ipynb file in Google Colab or any other Jupyter notebook environment.
Upload the assets folder to your environment, and move its contents to the same directory as the notebook.
Run the cells in order to import the libraries, define the classes and functions, and train the model.
Save the trained model to your Google Drive or download it to your local machine.
Use the inference cell to test the model on any message you want. You can also change the model name, and accuracy in the cell.
Pre-trained Models
This notebook already contains two pre-trained examples, based on the "Small" and "Medium" datasets. The "spam_classifier_medium" model is suitable for long messages, and is very accurate, while the "spam_classifier_small" is better when it comes to short texts. Sometimes the AI gets it wrong though, it's not perfect.

Results
Here are some examples of predictions made by the model:

Message	Prediction	Confidence (that it is spam)	Model
BUY AN IPHONE NOW	Spam	75.556%	Medium
Hi, how are you?	Ham	0.057%	Small
You have won a free trip to Hawaii! Call now to claim your prize!	Spam	99.986%	Small
I'm sorry I missed your call earlier. Can we talk later? If you're comfortable, of course. Best Regards, Jared.	Ham	27.84%	Medium
