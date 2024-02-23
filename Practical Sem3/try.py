import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import graphviz
from sklearn import tree

# Data from the user's image
data = {
    'age': [32, 25, 33, 26, 30, 25, 42, 38, 36, 29, 35, 28, 30, 38, 31],
    'apple_pie': [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    'potato_salad': [1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    'sushi': [1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0],
    'midwest': [1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define the features and the target
X = df[['age', 'apple_pie', 'potato_salad', 'sushi']]
y = df['midwest']

# Initialize the DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy')

# Fit the model
clf.fit(X, y)

# Visualize the tree
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=X.columns,  
                                class_names=['Not Midwest', 'Midwest'],
                                filled=True)

# Return the graphviz object
# graphviz.Source(dot_data)
graph = graphviz.Source(dot_data)
graph.render("decision_tree")

