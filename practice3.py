from sklearn.tree import DecisionTreeClassifier

X = [[60000], [70000], [20000], [30000]]
y = ["Yes", "Yes", "No", "No"]

model = DecisionTreeClassifier()

model.fit(X, y)

print(model.predict([[45000]]))