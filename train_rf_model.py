import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from feature_engineering import load_and_preprocess

df, features = load_and_preprocess("./datasets")
X, y = df[features], df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)
print(f"Test accuracy: {clf.score(X_test, y_test):.4f}")

with open("models/rf_model.pkl", "wb") as f:
    pickle.dump(clf, f)
