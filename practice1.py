from sklearn.tree import DecisionTreeClassifier

X=[[25],[35],[45],[20],[30]]
y=[0,1,1,0,1]

model=DecisionTreeClassifier()
model.fit(X,y)

prediction=model.predict([[40]])

print(prediction)