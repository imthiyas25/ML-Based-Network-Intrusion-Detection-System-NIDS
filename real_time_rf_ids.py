import pickle
import pandas as pd
from scapy.all import sniff
from feature_engineering import features  # use the features from your data script

with open("../models/rf_model.pkl", "rb") as f:
    clf = pickle.load(f)

def extract(pkt):
    # Example: dummy values (replace extraction logic as per your real data/needs)
    return [len(pkt), 0, 0, 0, 0]

def callback(pkt):
    feats = extract(pkt)
    data = pd.DataFrame([feats], columns=features)
    pred = clf.predict(data)[0]
    output_line = f"Prediction: {pred} | Packet: {pkt.summary()}"
    print(output_line)
    with open("output.log", "a") as log_file:
        log_file.write(output_line + "\n")

if __name__ == "__main__":
    print("Starting real-time Random Forest-based IDS...")
    sniff(prn=callback, count=100)
