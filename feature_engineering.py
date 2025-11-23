import pandas as pd

features = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets"
]

def load_and_preprocess(path):
    import os
    all_files = []
    if os.path.isdir(path):
        for fname in os.listdir(path):
            if fname.endswith('.csv'):
                all_files.append(os.path.join(path, fname))
    else:
        all_files = [path]

    dfs = [pd.read_csv(f) for f in all_files]
    df = pd.concat(dfs, ignore_index=True)
    df.columns = df.columns.str.strip()
    print("Loaded columns:", list(df.columns))
    target = "Label"
    df = df[features + [target]]
    df = df.dropna()
    # Binary labels: 1 = attack, 0 = benign
    df["Label"] = df["Label"].apply(lambda x: 0 if x == "BENIGN" else 1)
    return df, features
