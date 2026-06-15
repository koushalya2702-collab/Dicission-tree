#Accuracy

from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

X = [[60000], [70000], [30000], [20000]]
y = ["Yes", "Yes", "No", "No"]

model = DecisionTreeClassifier()

model.fit(X, y)

pred = model.predict(X)

print("Accuracy:", accuracy_score(y, pred))