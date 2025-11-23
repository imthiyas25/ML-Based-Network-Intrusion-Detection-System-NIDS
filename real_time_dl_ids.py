import pandas as pd
import numpy as np
from scapy.all import sniff
from tensorflow.keras.models import load_model
from feature_engineering import features

model = load_model("../models/dl_model.h5")

def extract(pkt):
    # Dummy list -- you have to align with features and real data
    return [len(pkt), 0, 0, 0, 0]

def callback(pkt):
    feats = np.array([extract(pkt)])
    pred = model.predict(feats)
    if pred[0][0] > 0.5:
        print("Threat detected (Deep Learning):", pkt.summary())

if __name__ == "__main__":
    print("Starting real-time DL-based IDS...")
    sniff(prn=callback, count=100)
