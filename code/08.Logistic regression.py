import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("code/08.insurance_data.csv")
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)

model = LogisticRegression()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)
model.predict_proba(X_test)

print(model.score(X_test,y_test))

