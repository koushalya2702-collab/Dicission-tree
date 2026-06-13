import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    'hours':[2,3,5,6,8],
    'pass':[0,0,1,1,1]
}

df = pd.DataFrame(data)

X = df[['hours']]
y = df['pass']

model = DecisionTreeClassifier()
model.fit(X,y)

print(model.predict([[4]]))