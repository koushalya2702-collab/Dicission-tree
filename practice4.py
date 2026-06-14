# Decision Tree Basics

from sklearn.tree import DecisionTreeClassifier

X = [[60000], [70000], [30000], [20000]]
y = ["Yes", "Yes", "No", "No"]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[55000]]))

#Information Gain

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(criterion="entropy")

X = [[25],[30],[35], [45], [55]]
y = ["No","No","No", "Yes", "Yes"]

model.fit(X, y)

print(model.feature_importances_)