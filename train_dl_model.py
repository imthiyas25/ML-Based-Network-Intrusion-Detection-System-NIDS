from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from feature_engineering import load_and_preprocess

df, features = load_and_preprocess("./datasets")
X, y = df[features], df["Label"]

model = Sequential([
    Dense(32, activation="relu", input_shape=(len(features),)),
    Dense(16, activation="relu"),
    Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(X, y, epochs=10, batch_size=128, validation_split=0.2)
model.save("models/dl_model.h5")
